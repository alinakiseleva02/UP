from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Projects, Employees, Materials, Teams, Customers, Documents, ConstructionObjects

def index(request):
    """Главная страница на основе вашего HTML"""
    context = {
        'projects_count': Projects.objects.count(),
        'employees_count': Employees.objects.count(),
        'customers_count': Customers.objects.count(),
    }
    return render(request, 'index.html', context)

def projects_page(request):
    """Страница проектов с поиском"""
    search_query = request.GET.get('search', '')
    projects = Projects.objects.select_related('customer', 'employee').all()
    
    if search_query:
        projects = projects.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(customer__company_name__icontains=search_query) |
            Q(employee__full_name__icontains=search_query)
        )
    
    return render(request, 'projects.html', {
        'projects': projects,
        'search_query': search_query
    })

def project_detail(request, project_id):
    """Детальная страница проекта"""
    project = get_object_or_404(
        Projects.objects.select_related('customer', 'employee'), 
        id=project_id
    )
    
    # Получаем связанные данные
    documents = Documents.objects.filter(project=project)
    construction_objects = ConstructionObjects.objects.filter(project=project)
    
    return render(request, 'project_detail.html', {
        'project': project,
        'documents': documents,
        'construction_objects': construction_objects
    })

def team_page(request):
    """Страница команды"""
    employees = Employees.objects.all()
    teams = Teams.objects.select_related('employee').all()
    return render(request, 'team.html', {
        'employees': employees,
        'teams': teams
    })

def materials_page(request):
    """Страница материалов"""
    materials = Materials.objects.all()
    return render(request, 'materials.html', {'materials': materials})

def contacts_page(request):
    """Страница контактов"""
    return render(request, 'contacts.html')