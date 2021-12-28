from django.shortcuts import render , redirect
from . import models 
from django.shortcuts  import get_object_or_404
from . import forms 
from django.contrib import messages
from accounts.models import User
from utils.ajax_form_save import save_form
from django.http import JsonResponse
from django.template.loader import render_to_string





def project_create(request):
    projects = models.Project.objects.all()
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST ,request.FILES)

    else:
        form = forms.ProjectForm()
    return save_form(request,form,projects,'includes/project_list.html','includes/project_create.html')



def project_edit(request,id):
    project = get_object_or_404(models.Project , id=id)
    projects = models.Project.objects.all()
    if request.method == 'POST':
        form = forms.ProjectForm(request.POST ,request.FILES , instance=project)

    else:
        form = forms.ProjectForm(instance=project)

    return save_form(request,form,projects,'includes/project_list.html','includes/project_update.html')


def project_delete(request,id):
    project = get_object_or_404(models.Project , id=id)
    data = dict()
    if request.method == 'POST':
        project.delete()
        data['form_is_valid'] = True
        projects = models.Project.objects.all()
        data['model_list'] = render_to_string('includes/project_list.html',{'object_list':projects})
        
    else:
        data['form_is_valid'] = False
        context = {'project':project}
        data['html_form'] = render_to_string('includes/project_delete.html',context,request=request)
    return JsonResponse(data)



def project_report(request):
    projects = models.Project.objects.all()   # filter bu current manager
    return render(request,'managers/project-reports.html',{'projects':projects})






def client_list(request):
    clients = models.Client.objects.all()
    return render(request,'managers/clients.html',{'object_list':clients})



def client_create(request):
    clients = models.Client.objects.all()
    if request.method == 'POST':
        form = forms.ClientForm(request.POST)

    else:
        form = forms.ClientForm()
    return save_form(request,form,clients,'includes/client_list.html','includes/client_create.html')



def client_edit(request,id):
    client = get_object_or_404(models.Client , id=id)
    clients = models.Client.objects.all()
    if request.method == 'POST':
        form = forms.ClientForm(request.POST , instance=client)

    else:
        form = forms.ClientForm(instance=client)

    return save_form(request,form,clients,'includes/client_list.html','includes/client_update.html')


def client_delete(request,id):
    client = get_object_or_404(models.Client , id=id)
    data = dict()
    if request.method == 'POST':
        client.delete()
        data['form_is_valid'] = True
        clients = models.Client.objects.all()
        data['model_list'] = render_to_string('includes/client_list.html',{'object_list':clients})
        
    else:
        data['form_is_valid'] = False
        context = {'client':client}
        data['html_form'] = render_to_string('includes/client_delete.html',context,request=request)
    return JsonResponse(data)
