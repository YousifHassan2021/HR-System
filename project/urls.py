"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path , include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from settings.views import handel500

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('' , include('website.urls',namespace='website')),
    path('' , include('accounts.urls',namespace='accounts')),
    path('' , include('hr.urls',namespace='hr')),
    path('' , include('employee.urls',namespace='employee')),
    path('' , include('managers.urls',namespace='manager')),
    path('settings/' , include('settings.urls',namespace='setings')),
    path('500' , handel500, name='500_error'),

]



handler404= "settings.views.handel404"
handler500= "settings.views.handel500"


if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
