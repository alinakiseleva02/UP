from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('projects/', views.projects_view, name='projects'),
    path('projects/<int:project_id>/', views.project_detail_view, name='project_detail'),
    path('materials/', views.materials_view, name='materials'),
    path('team/', views.team_view, name='team'),
    path('contacts/', views.contacts_view, name='contacts'),
]