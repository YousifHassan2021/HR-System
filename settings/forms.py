from django import forms 
from . import models
from django.forms.widgets import NumberInput
from django_countries.widgets import CountrySelectWidget


class DepartmentSectionForm(forms.ModelForm):
    class Meta:
        model = models.Department_Section
        fields = ['name',]


class JobTypeForm(forms.ModelForm):
    class Meta:
        model = models.JobType
        fields = ['name','department']


class TrainingCourseForm(forms.ModelForm):
    class Meta:
        model = models.TrainingCourse
        fields = ['name','description','status']

    
class AssetForm(forms.ModelForm):
    purchase_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    warranty_end = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Assets
        fields = '__all__'
        execlude = 'company'



class HolidayForm(forms.ModelForm):
    date_from = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    class Meta:
        model = models.Holiday
        fields = '__all__'
        execlude = 'company'


# class AssetConditionForm(forms.ModelForm):
#     class Meta:
#         model = models.AssetCondition
#         fields = '__all__'


# class AssetStatusForm(forms.ModelForm):
#     class Meta:
#         model = models.AssetStatus
#         fields = '__all__'


# class AtendanceTypesForm(forms.ModelForm):
#     class Meta:
#         model = models.AttendenceType
#         fields = '__all__'


# class BankNamesForm(forms.ModelForm):
#     class Meta:
#         model = models.BankName
#         fields = '__all__'

# class BranchForm(forms.ModelForm):
#     class Meta:
#         model = models.Branch
#         fields = '__all__'


# class CityForm(forms.ModelForm):
#     class Meta:
#         model = models.City
#         fields = '__all__'


# class CompanyForm(forms.ModelForm):
#     class Meta:
#         model = models.Company
#         fields = '__all__'


# # class LocalizationForm(forms.ModelForm):
# #     class Meta:
# #         model = models.
# #         fields = '__all__'

# class DefaultPasswordForm(forms.ModelForm):
#     class Meta:
#         model = models.DefaultPassword
#         fields = '__all__'


# class DiscountTypesForm(forms.ModelForm):
#     class Meta:
#         model = models.DiscountType
#         fields = '__all__'


# class EmployeeStatusForm(forms.ModelForm):
#     class Meta:
#         model = models.EmployeeStatus
#         fields = '__all__'


# class FollowerTypesForm(forms.ModelForm):
#     class Meta:
#         model = models.FollowerType
#         fields = '__all__'


# class InsuranceClassForm(forms.ModelForm):
#     class Meta:
#         model = models.InsuranceClass
#         fields = '__all__'


# class InsuranceCompanyForm(forms.ModelForm):
#     class Meta:
#         model = models.InsuranceCompany
#         fields = '__all__'

# class JobGradeForm(forms.ModelForm):
#     class Meta:
#         model = models.JobGrade
#         fields = '__all__'


# class ProjectPeriorityForm(forms.ModelForm):
#     class Meta:
#         model = models.ProjectPeriority
#         fields = '__all__'


# class ProjectStatusForm(forms.ModelForm):
#     class Meta:
#         model = models.ProjectStatus
#         fields = '__all__'


# class QualificationsForm(forms.ModelForm):
#     class Meta:
#         model = models.Qualifications
#         fields = '__all__'


# class ReasonToTerminateForm(forms.ModelForm):
#     class Meta:
#         model = models.ReasonToTerminate
#         fields = '__all__'


# class ReplacementPeriodsForm(forms.ModelForm):
#     class Meta:
#         model = models.ReplacementPeriod
#         fields = '__all__'


# class ReplacementTypesForm(forms.ModelForm):
#     class Meta:
#         model = models.AssetCondition
#         fields = '__all__'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = models.Company
        fields = ['company_name','address','country','email','phone_number','website_url','logo']
        widgets = {'country': CountrySelectWidget()}