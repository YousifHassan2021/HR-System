from django.urls import path
from . import views

app_name = 'employee'


urlpatterns = [
    path('holidays' , views.holydays , name='holidays'),
    # vacation
    path('my-attendance' , views.my_attendance , name='my_attendance'),
    path('salary' , views.my_salary_list , name='my_salary_list'),
    path('loan' , views.my_loan , name='my_loan'),

    # overtime
    path('month-overtime' , views.month_overtime , name='month_overtime'),
    path('all-overtime' , views.all_overtime , name='overtime'),
    path('overtime/<int:id>' , views.delete_overtime , name='delete_overtime'),


    # reports
    # client
    path('training' , views.my_training , name='training'),
    path('promotions' , views.my_promotions , name='promotions'),
    path('resign' , views.add_resign , name='resign'),
    path('resign/<int:id>' , views.delete_resign , name='delete_resign'),
    path('assets' , views.my_assets , name='assets'),
     
]

