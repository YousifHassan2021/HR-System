from django.urls import path 
from .views import home , about , contact , new_company

app_name = 'website'


urlpatterns = [
    path('',home,name='home'),
    path('about' ,about,name='about' ),
    path('contact' ,contact,name='contact' ),
    path('new-company/register' , new_company,name='new_company'),

]
