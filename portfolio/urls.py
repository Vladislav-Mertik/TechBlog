from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.portfolio_home_view, name='home'),
    path('projects/', views.projects_view, name='projects'),
    path('skills/', views.skills_view, name='skills'),
]
