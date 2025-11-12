from django.shortcuts import render
from .models import Projects, Employees, Materials, Teams, Customers

def index(request):
    """Главная страница на основе вашего HTML"""
    context = {
        'projects_count': Projects.objects.count(),
        'employees_count': Employees.objects.count(),
        'customers_count': Customers.objects.count(),
    }
    return render(request, 'index.html', context)

def projects_page(request):
    """НОВАЯ СТРАНИЦА 1 - Проекты"""
    projects = Projects.objects.select_related('customer', 'employee').all()
    return render(request, 'projects.html', {'projects': projects})

def team_page(request):
    """НОВАЯ СТРАНИЦА 2 - Команда"""
    employees = Employees.objects.all()
    teams = Teams.objects.select_related('employee').all()
    return render(request, 'team.html', {
        'employees': employees,
        'teams': teams
    })

def materials_page(request):
    """НОВАЯ СТРАНИЦА 3 - Материалы"""
    materials = Materials.objects.all()
    return render(request, 'materials.html', {'materials': materials})

def contacts_page(request):
    """Страница контактов"""
    return render(request, 'contacts.html')