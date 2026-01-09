#!/usr/bin/env python
import os
import django
from datetime import datetime, timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Tag, Article
from library_system.models import Author, Book, Reader, Loan

print("Clearing existing data...")
Tag.objects.all().delete()
Article.objects.all().delete()
Author.objects.all().delete()
Book.objects.all().delete()
Reader.objects.all().delete()
Loan.objects.all().delete()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print("✓ Superuser 'admin' created (password: admin123)")

print("\n--- Creating Tags ---")
tags_data = [
    {'name': 'Python', 'color': '#3776ab'},
    {'name': 'Django', 'color': '#092e20'},
    {'name': 'JavaScript', 'color': '#f7df1e'},
    {'name': 'React', 'color': '#61dafb'},
    {'name': 'Frontend', 'color': '#ff6b6b'},
    {'name': 'Backend', 'color': '#4ecdc4'},
]

tags = {}
for tag_data in tags_data:
    tag = Tag.objects.create(**tag_data)
    tags[tag.name] = tag
    print(f"✓ Tag created: {tag.name}")

print("\n--- Creating Articles ---")
admin_user = User.objects.get(username='admin')

articles_data = [
    {
        'title': 'Вступ до Django',
        'content': '''Django - це високорівневий веб-фреймворк на Python, який дозволяє швидко розробляти масштабовані веб-додатки.

Основні переваги Django:
• Включений ORM для роботи з базами даних
• Вбудована система адміністрування
• Безпека на рівні фреймворку
• Масштабованість

Django слідує за принципом "batteries included" (батарейки включені), що означає, що він надає все необхідне для розробки веб-додатків з коробки.

Цей фреймворк підтримує MVC архітектуру (Model-View-Controller), що дозволяє розробникам організувати код ефективно.''',
        'is_featured': True,
        'views': 150,
        'likes': 35,
        'tags': ['Django', 'Python', 'Backend']
    },
    {
        'title': 'React для новачків',
        'content': '''React - це JavaScript бібліотека для створення користувацьких інтерфейсів.

Ключові концепції React:
1. Компоненти - переиспользуемые UI елементи
2. JSX - синтаксис для запису HTML-подібного коду в JavaScript
3. Стан (State) - внутрішні дані компонента
4. Props - передача даних від батьків до дітей

React використовує віртуальний DOM для оптимізації оновлень інтерфейсу. Це дозволяє розробляти високопродуктивні веб-додатки.

Екосистема React включає множество бібліотек для маршрутизації, управління станом та інших завдань.''',
        'is_featured': True,
        'views': 200,
        'likes': 58,
        'tags': ['React', 'JavaScript', 'Frontend']
    },
    {
        'title': 'Python для веб-розробки',
        'content': '''Python - це один із найпопулярніших мовень програмування для веб-розробки.

Фреймворки Python для веб-розробки:
- Django - повнофункціональний фреймворк
- Flask - мініміалістичний фреймворк
- FastAPI - сучасний та швидкий фреймворк

Python знаходить застосування як у frontend, так і у backend розробці. З допомогою бібліотек як Selenium можна автоматизувати тестування веб-додатків.

Популярність Python в даній сфері пояснюється його простотою та потужністю.''',
        'is_featured': False,
        'views': 120,
        'likes': 42,
        'tags': ['Python', 'Backend']
    },
    {
        'title': 'JavaScript: особливості та гідності',
        'content': '''JavaScript - це язык программирования, який працює в браузері та на серверів (Node.js).

Основні особливості JavaScript:
• Динамічна типізація
• Функціональне програмування
• Асинхронне програмування (Promises, async/await)
• Великий екосистема npm пакетів

JavaScript постійно розвивається, щороку з\'являються нові стандарти ES (ECMAScript). 

Для розробки з JavaScript часто використовуються фреймворки як Vue.js, Angular та інші.''',
        'is_featured': False,
        'views': 175,
        'likes': 52,
        'tags': ['JavaScript', 'Frontend']
    },
    {
        'title': 'Best practices в веб-розробці',
        'content': '''Професійна веб-розробка вимагає дотримання певних практик:

1. Безпека:
   - Валідація вхідних даних
   - Захист від XSS та CSRF атак
   - Шифрування чутливих даних

2. Продуктивність:
   - Оптимізація сайту для швидкості
   - Кешування
   - Мініфікація CSS/JS

3. Якість коду:
   - Написання тестів
   - Code review
   - Документування

4. Масштабованість:
   - Правильна архітектура
   - Використання кешуючих систем
   - Балансування навантаження

Дотримання цих практик допомагає розробляти надійні та ефективні веб-додатки.''',
        'is_featured': True,
        'views': 250,
        'likes': 75,
        'tags': ['Frontend', 'Backend', 'Python']
    },
    {
        'title': 'Введення в REST API',
        'content': '''REST (Representational State Transfer) - це архітектурний стиль для розробки веб-сервісів.

HTTP методи у REST:
- GET - отримання даних
- POST - створення нових даних
- PUT - оновлення даних
- DELETE - видалення даних

REST використовує стандартні HTTP статус коди:
- 200 OK - успішний запит
- 201 Created - ресурс створений
- 400 Bad Request - помилка у запиті
- 404 Not Found - ресурс не знайден
- 500 Internal Server Error - помилка сервера

REST API - це потужний спосіб комунікації між клієнтом та сервером. Django REST Framework - це чудова бібліотека для розробки REST API з Django.''',
        'is_featured': False,
        'views': 190,
        'likes': 48,
        'tags': ['Django', 'Backend', 'Python']
    }
]

for article_data in articles_data:
    tags_list = article_data.pop('tags')
    article = Article.objects.create(author=admin_user, **article_data)
    for tag_name in tags_list:
        article.tags.add(tags[tag_name])
    print(f"✓ Article created: {article.title}")

print("\n--- Creating Authors ---")
authors_data = [
    {'name': 'Джордж Мартін', 'country': 'США', 'birth_year': 1948},
    {'name': 'Джоан Ролінг', 'country': 'Велика Британія', 'birth_year': 1965},
    {'name': 'Лев Толстой', 'country': 'Росія', 'birth_year': 1828},
]

authors = {}
for author_data in authors_data:
    author = Author.objects.create(**author_data)
    authors[author.name] = author
    print(f"✓ Author created: {author.name}")

print("\n--- Creating Books ---")
books_data = [
    {
        'title': 'Гра престолів',
        'author': authors['Джордж Мартін'],
        'isbn': '9780553573404',
        'pages': 694,
        'publication_year': 1996,
        'is_available': True
    },
    {
        'title': 'Зіткнення королів',
        'author': authors['Джордж Мартін'],
        'isbn': '9780553573415',
        'pages': 761,
        'publication_year': 1998,
        'is_available': True
    },
    {
        'title': 'Гарі Поттер та філософський камінь',
        'author': authors['Джоан Ролінг'],
        'isbn': '9780747532699',
        'pages': 223,
        'publication_year': 1997,
        'is_available': False
    },
    {
        'title': 'Гарі Поттер та таємна кімната',
        'author': authors['Джоан Ролінг'],
        'isbn': '9780747538493',
        'pages': 251,
        'publication_year': 1998,
        'is_available': True
    },
    {
        'title': 'Війна і мир',
        'author': authors['Лев Толстой'],
        'isbn': '9785170926244',
        'pages': 1440,
        'publication_year': 1869,
        'is_available': True
    },
]

books = {}
for book_data in books_data:
    book = Book.objects.create(**book_data)
    books[book.title] = book
    status = "доступна" if book.is_available else "видана"
    print(f"✓ Book created: {book.title} ({status})")

print("\n--- Creating Readers ---")
readers_data = [
    {'name': 'Петро Іванов', 'email': 'petro@example.com'},
    {'name': 'Марія Петренко', 'email': 'maria@example.com'},
    {'name': 'Олег Сідоренко', 'email': 'oleg@example.com'},
]

readers = {}
for reader_data in readers_data:
    reader = Reader.objects.create(**reader_data)
    readers[reader.name] = reader
    print(f"✓ Reader created: {reader.name}")

print("\n--- Creating Loans ---")
loans_data = [
    {
        'reader': readers['Петро Іванов'],
        'book': books['Гра престолів'],
        'return_date': None
    },
    {
        'reader': readers['Марія Петренко'],
        'book': books['Гарі Поттер та філософський камінь'],
        'return_date': None
    },
    {
        'reader': readers['Олег Сідоренко'],
        'book': books['Війна і мир'],
        'return_date': (datetime.now() - timedelta(days=5)).date()
    },
    {
        'reader': readers['Петро Іванов'],
        'book': books['Гарі Поттер та таємна кімната'],
        'return_date': None
    },
]

for loan_data in loans_data:
    loan = Loan.objects.create(**loan_data)
    status = "активна позика" if not loan.return_date else "повернута"
    print(f"✓ Loan created: {loan.reader.name} -> {loan.book.title} ({status})")

print("\n" + "="*50)
print("✓ Database successfully populated with test data!")
print("="*50)
