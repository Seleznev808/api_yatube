# api_yatube
## Описание
API проекта Yatube. API доступен только аутентифицированным пользователям. В проекте используется аутентификация по JWT-токену. Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.
### Как запустить проект (для Windows)
Клонировать репозиторий на свой компьютер:
```
git clone git@github.com:Seleznev808/api_final_yatube.git
```
Перейти на него в командной строке и развернуть виртуальное окружение:
```
cd api_final_yatube
python -m venv venv
```
Активировать виртуальное окружение и установить зависимости:
```
source venv/Scripts/activate
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```
### Эндпоинты:

api/v1/jwt/create/ (POST): передаём логин и пароль, получаем токен.
api/v1/jwt/refresh/ (POST): обновить токен.
api/v1/jwt/verify/ (POST): проверить токен.
api/v1/posts/ (GET, POST): получаем список всех постов или создаём новый пост.
api/v1/posts/{post_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем пост по id.
api/v1/groups/ (GET): получаем список всех групп.
api/v1/groups/{group_id}/ (GET): получаем информацию о группе по id.
api/v1/posts/{post_id}/comments/ (GET, POST): получаем список всех комментариев поста с id=post_id или создаём новый, указав id поста, который хотим прокомментировать.
api/v1/posts/{post_id}/comments/{comment_id}/ (GET, PUT, PATCH, DELETE): получаем, редактируем или удаляем комментарий по id у поста с id=post_id.
api/v1/follow/ (GET, POST): получаем список подписок, подписываемся на пользователя. Анонимные запросы запрещены.

### Примеры запросов:
Получить список всех публикаций:
```
GET .../api/v1/posts/
```
Ответ:
```JSON
{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
    "results": [
        {}
    ]
}
```
Добавление новой публикации. Анонимные запросы запрещены:
```
POST .../api/v1/posts/
```
```JSON
{
    "text": "string",
    "image": "string",
    "group": 0
}
```
Ответ:
```JSON
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
```
Частичное обновление комментария к публикации по id. Обновить комментарий может только автор комментария. Анонимные запросы запрещены:
```
PATCH .../api/v1/posts/{post_id}/comments/{id}/
```
```JSON
{
    "text": "string",
}
```
Ответ:
```JSON
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```
### Автор
[Селезнев Василий](https://github.com/Seleznev808)
