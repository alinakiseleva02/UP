# views.py
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Projects, Employees, Customers, Materials, Teams, Documents, ConstructionObjects

def projects_view(request):
    # Получаем поисковый запрос
    search_query = request.GET.get('search', '')
    
    # Получаем ВСЕ проекты для отображения
    all_projects = Projects.objects.all()
    
    # Получаем отфильтрованные проекты (для поиска)
    filtered_projects = all_projects
    
    # Если есть поисковый запрос, фильтруем проекты
    if search_query:
        filtered_projects = all_projects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(customer__company_name__icontains=search_query) |
            Q(employee__full_name__icontains=search_query)
        ).distinct()
    
    context = {
        'projects': filtered_projects,  # Показываем отфильтрованные или все проекты
        'search_query': search_query,
        'all_projects_count': all_projects.count(),  # Общее количество всех проектов
    }
    return render(request, 'projects.html', context)

def project_detail_view(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    
    # Получаем связанные объекты
    construction_objects = ConstructionObjects.objects.filter(project=project)
    documents = Documents.objects.filter(project=project)
    
    context = {
        'project': project,
        'construction_objects': construction_objects,
        'documents': documents,
    }
    return render(request, 'project_detail.html', context)

def index_view(request):
    # Получаем статистику для главной страницы
    projects_count = Projects.objects.count()
    employees_count = Employees.objects.count()
    customers_count = Customers.objects.count()
    
    context = {
        'projects_count': projects_count,
        'employees_count': employees_count,
        'customers_count': customers_count,
    }
    return render(request, 'index.html', context)

def materials_view(request):
    materials = Materials.objects.all()
    
    # Добавляем вычисляемое поле для общей стоимости
    for material in materials:
        material.total_value = material.unit_price * material.available_quantity
    
    context = {
        'materials': materials,
    }
    return render(request, 'materials.html', context)

def team_view(request):
    employees = Employees.objects.all()
    teams = Teams.objects.all()
    
    context = {
        'employees': employees,
        'teams': teams,
    }
    return render(request, 'team.html', context)

def contacts_view(request):
    return render(request, 'contacts.html')