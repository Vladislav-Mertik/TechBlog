from django.shortcuts import render


def portfolio_home_view(request):
    """Головна сторінка портфоліо"""
    portfolio_data = {
        'name': 'Александр Дмитренко',
        'title': 'Full-Stack веб-розробник',
        'bio': 'Професійний розробник з більш ніж 5 років досвіду у створенні веб-приложень. Спеціалізуюся на Python та Django.',
        'image': '/static/img/profile.jpg',
        'email': 'alex@example.com',
        'current_page': 'home'
    }
    
    return render(request, 'portfolio/home.html', portfolio_data)


def projects_view(request):
    """Сторінка проектів"""
    projects = [
        {
            'id': 1,
            'name': 'E-Commerce Platform',
            'description': 'Повнофункціональний інтернет-магазин з системою управління замовленнями',
            'status': 'completed',
            'technologies': ['Django', 'PostgreSQL', 'Stripe API', 'React'],
            'link': 'https://example.com/ecommerce'
        },
        {
            'id': 2,
            'name': 'Task Management System',
            'description': 'Система управління завданнями для команд з реал-тайм обновленнями',
            'status': 'in_progress',
            'technologies': ['Django', 'WebSocket', 'Vue.js', 'Redis'],
            'link': '#'
        },
        {
            'id': 3,
            'name': 'Analytics Dashboard',
            'description': 'Інтерактивна панель аналітики з графіками та звітами',
            'status': 'completed',
            'technologies': ['Django', 'Chart.js', 'PostgreSQL'],
            'link': 'https://example.com/analytics'
        },
        {
            'id': 4,
            'name': 'Social Network API',
            'description': 'REST API для соціальної мережі з аутентифікацією та нотифікаціями',
            'status': 'in_progress',
            'technologies': ['Django REST', 'JWT', 'Celery'],
            'link': '#'
        },
        {
            'id': 5,
            'name': 'AI Chatbot',
            'description': 'Чат-бот на основі AI для обслуговування клієнтів',
            'status': 'planning',
            'technologies': ['Django', 'OpenAI API', 'NLP'],
            'link': '#'
        }
    ]
    
    context = {
        'projects': projects,
        'current_page': 'projects'
    }
    return render(request, 'portfolio/projects.html', context)


def skills_view(request):
    """Сторінка навичок"""
    skills = [
        {
            'category': 'Backend',
            'items': [
                {'name': 'Python', 'level': 95},
                {'name': 'Django', 'level': 90},
                {'name': 'REST API', 'level': 88},
                {'name': 'PostgreSQL', 'level': 85},
            ]
        },
        {
            'category': 'Frontend',
            'items': [
                {'name': 'HTML/CSS', 'level': 90},
                {'name': 'JavaScript', 'level': 85},
                {'name': 'React', 'level': 80},
                {'name': 'Vue.js', 'level': 75},
            ]
        },
        {
            'category': 'DevOps',
            'items': [
                {'name': 'Docker', 'level': 80},
                {'name': 'Git', 'level': 95},
                {'name': 'Linux', 'level': 85},
                {'name': 'AWS', 'level': 70},
            ]
        },
        {
            'category': 'Tools',
            'items': [
                {'name': 'VS Code', 'level': 95},
                {'name': 'Jira', 'level': 80},
                {'name': 'Figma', 'level': 75},
                {'name': 'Jenkins', 'level': 70},
            ]
        }
    ]
    
    context = {
        'skills': skills,
        'current_page': 'skills'
    }
    return render(request, 'portfolio/skills.html', context)
