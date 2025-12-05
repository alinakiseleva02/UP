from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects_page, name='projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('team/', views.team_page, name='team'),
    path('materials/', views.materials_page, name='materials'),
    path('contacts/', views.contacts_page, name='contacts'),
]