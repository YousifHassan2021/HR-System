from django.urls import path
from . import views
# from employee import views as em_views 

app_name = 'managers'


urlpatterns = [


    path('projects/add' , views.project_create , name='project_create'),
    path('projects/<int:id>/edit' , views.project_edit , name='project_edit'),
    path('projects/<int:id>/delete' , views.project_delete , name='project_delete'),
    path('projects/reports' , views.project_report , name='project_report'),



    path('clients/' , views.client_list , name='client_list'),
    path('clients/add' , views.client_create , name='client_create'),
    path('clients/<int:id>/edit' , views.client_edit , name='client_edit'),
    path('clients/<int:id>/delete' , views.client_delete , name='client_delete'),

]