from typing import Any, Dict, List, Mapping, Optional, Tuple

from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context: Mapping[str, Any], menu_name: str) -> Dict[str, Any]:
    """Кастомный тег для отрисовки древовидного меню.

    Условия:
    - Ровно один запрос к БД (используется единичный queryset по названию меню)
    - Развернуты предки активного пункта и первый уровень детей активного пункта
    - Активность определяется по request.path
    """
    request = context['request']

    # Ровно один запрос к БД
    items = list(
        MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    )

    # Подготовка быстрых индексов и вычисление URL/активности
    id_to_item = {}
    active_item = None
    for item in items:
        item.url_resolved = item.get_absolute_url()
        item.is_active = (request.path == item.url_resolved)
        id_to_item[item.id] = item
        if item.is_active:
            active_item = item

    # Дерево parent_id -> [items]
    parent_id_to_children = {}
    for item in items:
        parent_id_to_children.setdefault(item.parent_id, []).append(item)

    # Найти множество id, которые должны быть развернуты: предки активного + сам активный
    # Разворачиваем только предков активного узла (не включая сам активный)
    expanded_ids = []
    if active_item is not None:
        current = id_to_item.get(active_item.parent_id)
        while current is not None:
            expanded_ids.append(current.id)
            current = id_to_item.get(current.parent_id)

    # Построение структуры (node, children)
    def build_menu_structure(parent_id: Optional[int]) -> List[Tuple[MenuItem, List[Tuple[MenuItem, Any]]]]:
        children = parent_id_to_children.get(parent_id, [])
        branch = []
        for node in children:
            node_children = build_menu_structure(node.id)
            branch.append((node, node_children))
        return branch

    menu_structure = build_menu_structure(None)

    return {
        'menu_structure': menu_structure,
        'expanded_ids': expanded_ids,  # список id узлов, чьи дети следует показать
    }