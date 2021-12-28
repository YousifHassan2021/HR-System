from django import forms 
from . import models 
from django.forms.widgets import NumberInput




class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Project
        exclude = ['manager',]



class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = '__all__'