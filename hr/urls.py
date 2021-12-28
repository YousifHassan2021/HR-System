from django.urls import path
from . import views

app_name = 'hr'


urlpatterns = [


    path('employee/add' , views.employee_create , name='employee_create'),
    path('employee/<int:id>/edit' , views.employee_edit , name='employee_edit'),
    path('employee/<int:id>/delete' , views.employee_delete , name='employee_delete'),
    path('employees/attendance' , views.employees_attendance , name='employees_attendance'),
    path('employees/attendance/<int:id>' , views.employee_attendance , name='employee_attendance'),
    path('employee/reports' , views.employee_info_report , name='employee_info_report'),


    path('departments/' , views.deparment_management , name='department_list'),
    path('departments/add' , views.department_create , name='department_create'),
    path('departments/add' , views.department_create , name='department_create'),
    path('departments/<int:id>/edit' , views.department_edit , name='department_edit'),
    path('departments/<int:id>/delete' , views.department_delete , name='department_delete'),


    path('jobs/' , views.job_management , name='job_list'),
    path('jobs/add' , views.job_create , name='job_create'),
    path('jobs/<int:id>/edit' , views.job_edit , name='job_edit'),
    path('jobs/<int:id>/delete' , views.job_delete , name='job_delete'),


    path('salary/' , views.employee_salary_management , name='employee_salary_management'),


    ## training
    path('training/' , views.training_management , name='training_list'),
    path('training/add' , views.training_create , name='training_create'),
    path('training/<int:id>/edit' , views.training_edit , name='training_edit'),
    path('training/<int:id>/delete' , views.training_delete , name='training_delete'),
    path('training/<int:id>/status_change' , views.training_staus_update , name='training_staus_update'),
    
    ## training type
    path('training-type/' , views.training_type_management , name='training_type_list'),
    path('training-type/create' , views.training_type_create , name='training_type_create'),
    path('training-type/<int:id>/edit' , views.training_type_edit , name='training_type_edit'),
    path('training-type/<int:id>/delete' , views.training_type_delete , name='training_type_delete'),
    path('training-type/<int:id>/status_change' , views.training_type_staus_update , name='training_type_staus_update'),
    

    ## promotions
    path('promotions/' , views.promotion_management , name='promotion_list'),
    path('promotions/add' , views.promotion_create, name='promotion_create'),
    path('promotions/<int:id>/edit' , views.promotion_edit , name='promotion_edit'),
    path('promotions/<int:id>/delete' , views.promotion_delete , name='promotion_delete'),


    ## payroll
    path('payroll/adition' , views.payroll_addition , name='payroll_addition'),
    path('payroll/adition/create' , views.payroll_addition_create , name='payroll_addition_create'),
    path('payroll/adition/<int:id>/edit' , views.payroll_addition_edit , name='payroll_addition_edit'),
    path('payroll/adition/<int:id>/delete' , views.payroll_addition_delte , name='payroll_addition_delte'),


    path('payroll/overtime' , views.payroll_overtime , name='payroll_overtime'),
    path('payroll/overtime/create' , views.payroll_overtime_create , name='payroll_overtime_create'),
    path('payroll/overtime/<int:id>/edit' , views.payroll_overtime_edit , name='payroll_overtime_edit'),
    path('payroll/overtime/<int:id>/delete' , views.payroll_overtime_delete , name='payroll_overtime_delete'),

    path('payroll/payslip' , views.payslip_view , name='payroll_payslip'),

    ## promotions
    path('assets/' , views.asset_management , name='asset_list'),
    path('assets/add' , views.asset_create , name='asset_create'),
    path('assets/<int:id>/edit' , views.asset_edit , name='asset_edit'),
    path('assets/<int:id>/delete' , views.asset_delete , name='asset_delete'),




    path('termination/' , views.employee_termination , name='employee_termination'),
    path('termination/add' , views.employee_termination , name='employee_termination'),
    path('termination/<int:id>/delete' , views.employee_termination_delete , name='employee_termination_delete'),
    
    path('holidays/' , views.employee_holidays , name='employee_holidays'),
    path('holidays/add' , views.holiday_create , name='holiday_create'),
    path('holidays/<int:id>/delete' , views.holiday_delete , name='holiday_delete'),


    path('announcements' , views.all_anouncements , name='all_anouncements'),


    path('settings/company' , views.company_settings , name='company_settings')

]