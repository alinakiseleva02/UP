from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects_page, name='projects'),
    path('team/', views.team_page, name='team'),
    path('materials/', views.materials_page, name='materials'),
    path('contacts/', views.contacts_page, name='contacts'),
]