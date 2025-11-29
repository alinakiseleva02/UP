from django.db import models

from django.db import models

class Users(models.Model):
    name = models.CharField(verbose_name='Имя пользователя', max_length=20)
    surname = models.CharField('Фамилия', max_length=25)
    mail = models.EmailField('Email', unique=True)
    nickname = models.CharField('Никнейм', max_length=50, unique=True)
    registration_date = models.DateField('Дата регистрации', auto_now_add=True)
    is_active = models.BooleanField('Активен', default=True)
    last_login = models.DateTimeField('Поледний вход')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
 
    def __str__(self):
        return self.nickname

# Модели строительной системы

class Employees(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=50, verbose_name='Должность')
    department = models.CharField(max_length=50, verbose_name='Отдел')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    hire_date = models.DateField(verbose_name='Дата приема на работу')
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    
    def __str__(self):
        return self.full_name

class Customers(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    contact_person = models.CharField(max_length=100, verbose_name='Контактное лицо')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
    
    def __str__(self):
        return self.company_name

class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название проекта')
    construction_period = models.IntegerField(verbose_name='Срок строительства')
    budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Бюджет')
    start_date = models.DateField(verbose_name='Дата приема в работу')
    employee = models.ForeignKey(Employees, on_delete=models.PROTECT, verbose_name='Сотрудник')
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT, verbose_name='Заказчик')
    
    image = models.ImageField(
        upload_to='projects/', 
        verbose_name='Изображение проекта',
        blank=True, 
        null=True
    )
    description = models.TextField(verbose_name='Описание проекта', blank=True)
    
    def formatted_budget(self):
        return f"{self.budget:,.0f}".replace(',', ' ') + ' руб.'
    
    def formatted_start_date(self):
        """Форматирует дату в русском формате"""
        months = {
            1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
            5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
            9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
        }
        return f"{self.start_date.day} {months[self.start_date.month]} {self.start_date.year} г."
    
    def formatted_construction_period(self):
        """Форматирует срок строительства"""
        days = self.construction_period
        if days >= 30:
            months = days // 30
            remaining_days = days % 30
            if remaining_days > 0:
                return f"{months} мес. {remaining_days} дн."
            return f"{months} мес."
        return f"{days} дн."

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self):
        return self.name

class Materials(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название материала')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    available_quantity = models.IntegerField(verbose_name='Доступное количество')
    
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
    
    def __str__(self):
        return self.name 

class Teams(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, verbose_name='Сотрудник')
    specialty = models.CharField(max_length=100, verbose_name='Специальность команды')
    member_count = models.IntegerField(verbose_name='Количество членов в команде')
    
    class Meta:
        verbose_name = 'Бригада'
        verbose_name_plural = 'Бригады'
    
    def __str__(self):
        return f"Бригада {self.specialty}"

class Documents(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок документа')
    creation_date = models.DateField(verbose_name='Дата создания')
    file_link = models.URLField(verbose_name='Ссылка на файл')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проект')
    
    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
    
    def __str__(self):
        return self.title

class ConstructionObjects(models.Model):
    address = models.CharField(max_length=200, verbose_name='Адрес стройплощадки')
    construction_stage = models.CharField(max_length=100, verbose_name='Стадия строительства')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='Проект')
    
    class Meta:
        verbose_name = 'Строительство объекта'
        verbose_name_plural = 'Строительство объектов'
    
    def __str__(self):
        return f"{self.address} - {self.construction_stage}"

class MaterialUsage(models.Model):
    material = models.ForeignKey(Materials, on_delete=models.PROTECT, verbose_name='Материал')
    construction_object = models.ForeignKey(ConstructionObjects, on_delete=models.CASCADE, verbose_name='Строительство объекта')
    material_consumption = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Расход материала')
    
    class Meta:
        verbose_name = 'Использование материалов'
        verbose_name_plural = 'Использование материалов'
    
    def __str__(self):
        return f"{self.material} - {self.construction_object}" 

