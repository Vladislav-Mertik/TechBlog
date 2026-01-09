from django.shortcuts import render
from .models import Article, Tag


def index_view(request):
    """Головна сторінка блогу"""
    articles = Article.objects.all()
    featured_articles = Article.objects.filter(is_featured=True)
    tags = Tag.objects.all()
    
    context = {
        'articles': articles,
        'featured_articles': featured_articles,
        'tags': tags,
        'current_page': 'index'
    }
    return render(request, 'blog/index.html', context)


def about_view(request):
    """Сторінка 'Про нас'"""
    team_members = [
        {'name': 'Іван Петренко', 'role': 'Lead Developer', 'bio': 'Спеціаліст з Python та Django'},
        {'name': 'Марія Коваленко', 'role': 'Designer', 'bio': 'UX/UI дизайнер з 5 років досвіду'},
        {'name': 'Олег Сідоренко', 'role': 'Content Manager', 'bio': 'Автор технічних статей'},
    ]
    
    context = {
        'team_members': team_members,
        'current_page': 'about'
    }
    return render(request, 'blog/about.html', context)


def contact_view(request):
    """Сторінка контактів"""
    contact_info = {
        'email': 'info@techblog.com',
        'phone': '+38 (097) 123-45-67',
        'address': 'Київ, вул. Хрещатик, 1',
        'working_hours': 'Пн-Пт: 9:00 - 18:00'
    }
    
    context = {
        'contact_info': contact_info,
        'current_page': 'contact'
    }
    return render(request, 'blog/contact.html', context)


def articles_list_view(request):
    """Список всіх статей"""
    articles = Article.objects.all()
    
    context = {
        'articles': articles,
        'current_page': 'articles'
    }
    return render(request, 'blog/articles_list.html', context)


def article_detail_view(request, pk):
    """Детальний перегляд статті"""
    article = Article.objects.get(pk=pk)
    article.views += 1
    article.save(update_fields=['views'])
    
    context = {
        'article': article,
        'current_page': 'articles'
    }
    return render(request, 'blog/article_detail.html', context)
