from django import forms 
from . import models
from django.forms.widgets import NumberInput
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class UserProfileForm(forms.ModelForm):
    id_create_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    id_end_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    passport_issue_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    passport_end_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    id_card_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    # join_date = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = models.UserProfile
       # fields = '__all__'
        exclude = ('user','image','file')



class UserTrainingForm(forms.ModelForm):
    start_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = models.UserTraining
        fields = '__all__'


class UserPromotionForm(forms.ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = models.UserPromotion
        fields = '__all__'



class UserAssetsForm(forms.ModelForm):
    class Meta:
        model = models.UserAssets
        # fields = '__all__'
        exclude = ['asset',]


class UserTerminationForm(forms.ModelForm):
    termination_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    notice_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = models.UserTermination
        fields = '__all__'



class OvertimeForm(forms.ModelForm):
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = models.UserOverTime
        fields = ['overhours','date','description']



class UserResignForm(forms.ModelForm):
    class Meta : 
        model = models.UserResign
        fields = ['reason','termination_date']


class UserReplacementForm(forms.ModelForm):
    class Meta:
        model = models.UserReplacements
        fields = ['user','replacement_type','percentage','money','category','replacement_for','notes']


class UserOverTimeForm(forms.ModelForm):
    class Meta:
        model = models.UserOverTime
        fields = '__all__'
        exclude = ('total_over_time_hours',)



from datetime import datetime

def possible_years(first_year_in_scroll, last_year_in_scroll):
    p_year = []
    for i in range(first_year_in_scroll, last_year_in_scroll, -1):
        p_year_tuple = str(i), i
        p_year.append(p_year_tuple)
    return p_year


MONTH_CHOICES =(
    ("1", "January"),
    ("2", "February"),
    ("3", "March"),
    ("4", "April "),
    ("5", "May"),
    ("6", "June"),
    ("7", "July"),
    ("8", "August"),
    ("9", "September"),
    ("10", "October"),
    ("11", "November"),
    ("12", "December")
)

class PayslipFilterForm(forms.Form):
    users = forms.ModelChoiceField(queryset=User.objects.all())
    month  = forms.ChoiceField(choices = MONTH_CHOICES)
    year = forms.ChoiceField(choices=possible_years(((datetime.now()).year), 2020),label='Year')