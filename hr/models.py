from django.db import models
# Create your models here.
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
import settings.models as st_model


class Announcement(models.Model):
    company  = models.ForeignKey(st_model.Company, related_name='company_announcement', on_delete=models.CASCADE)
    title = models.CharField(_("Title"),max_length=200)
    message = models.TextField(_("Message"),max_length=1000)
    created_at = models.DateTimeField(_("Created At"),default=timezone.now) 
    watched = models.ManyToManyField(settings.AUTH_USER_MODEL ,verbose_name=_("Watched Users"), blank=True, null=True)


    def __str__(self):
        return self.title
