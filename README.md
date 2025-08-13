# Menu Tree

Django приложение для реализации древовидного меню.

## Технологии

- **Django** - веб-фреймворк
- **PostgreSQL 15** - база данных
- **Docker & Docker Compose** - контейнеризация
- **Python 3.11** - язык программирования
- **psycopg2** - драйвер PostgreSQL для Python

## Запуск с помощью Docker

### 1. Клонируйте проект с GitHub
```bash
git clone https://github.com/Kuberunnak10/menu_tree.git
cd menu_tree
```

### 2. Создайте .env файл или измените название у .test-env


### 2. Запустите проект
```bash
docker-compose up --build
```

### 3. Примените миграции (автоматически)
Миграции применяются автоматически при запуске контейнера.

## Данные для админки

### Войдите в админку
- URL: `http://localhost:8000/admin/`
- Логин: `admin`
- Пароль: `admin`

### Добавьте пункты меню:

**1. Главная**
- Title: `Главная`
- Menu name: `main_menu`
- URL name: `home`
- Parent: -

**2. О нас**
- Title: `О нас`
- Menu name: `main_menu`
- URL name: `about`
- Parent: -

**3. Карьера**
- Title: `Карьера`
- Menu name: `main_menu`
- URL name: `careers`
- Parent: -

**4. Наша команда**
- Title: `Наша команда`
- Menu name: `main_menu`
- URL name: `our_team`
- Parent: `О нас`


## Главная страница

`http://localhost:8000/home/`