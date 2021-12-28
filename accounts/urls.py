from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('dashboard' , views.dashboard , name='dashboard'),
    path('profile/' , views.profile , name='profile'),
    path('projects' , views.project_list , name='projects'),
    path('projects/<int:id>' , views.project_detail , name='project_detail'),

    path('employees/' , views.employee_management , name='employee_list'),
    path('employees/export/excel' , views.employee_export_excel , name='employee_export_excel'),
    path('employee/<int:id>' , views.employee_detail,name='employee_detail'),
    # path('employees/attendance' , views.employees_attendance , name='employees_attendance'),
    # path('employees/attendance/<int:id>' , views.employee_attendance , name='employee_attendance'),
    
]

