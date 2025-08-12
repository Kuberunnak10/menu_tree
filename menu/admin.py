from django.contrib import admin
from menu.models import MenuItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """Админ-панель для модели MenuItem."""
    list_display = ['title', 'menu_name', 'parent']
    list_filter = ['menu_name']