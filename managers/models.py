from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from settings import models as st_model
from django.conf import settings

# Create your models here.


class Client(models.Model):
   company  = models.ForeignKey(st_model.Company, related_name='company_client', on_delete=models.CASCADE)
   name =  models.CharField(_("name"), max_length=100)
   mobile_number = models.CharField(max_length=18 , verbose_name=_('Mobile Number'), blank=True, null=True)
   email = models.EmailField(_("email"), max_length=254 , blank=True, null=True)
   address = models.CharField(max_length=200 , verbose_name=_('Address'), blank=True, null=True)

   def __str__(self):
     return self.name




class Project(models.Model):
    company  = models.ForeignKey(st_model.Company, related_name='company_project', on_delete=models.CASCADE)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Manager'), related_name='project_manager', on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=50)
    description = models.TextField(_("Description"))
    start_date = models.DateField(_("Start Date"), default=timezone.now)
    end_date = models.DateField(_("End Date"), default=timezone.now)
    piriority = models.ForeignKey(st_model.ProjectPeriority, verbose_name=_('Perioirty'), related_name='project_pirority', on_delete=models.CASCADE)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Leader') ,related_name='leader_user', on_delete=models.CASCADE)
    team = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name=_("Team"),blank=True, null=True)
    attachment = models.FileField(_("Attachment"), upload_to='projects/')
    client = models.ForeignKey(Client, verbose_name=_('Client'), related_name='project_client', on_delete=models.CASCADE)
    status = models.ForeignKey(st_model.ProjectStatus, verbose_name=_('Status'), related_name='project_status', on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class ProjectTask(models.Model):
    project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_task', on_delete=models.CASCADE)
    tile = models.CharField(max_length=200, verbose_name=_('Title'))
    description = models.TextField(_("Description"))
    due_date = models.DateField(_("Due Date"), default=timezone.now)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Employee'),related_name='task_employee', on_delete=models.CASCADE)
    status = models.ForeignKey(st_model.TaskStatus, verbose_name=_('Status'), related_name='task_status', on_delete=models.CASCADE)
    


# class Team(models.Model):
#     name = models.CharField(max_length=200)