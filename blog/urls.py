from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('articles/', views.articles_list_view, name='articles_list'),
    path('articles/<int:pk>/', views.article_detail_view, name='article_detail'),
]
