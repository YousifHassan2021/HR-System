from django.shortcuts import render , redirect
from . import models
from django.views.generic import CreateView , ListView
from django.views.generic.edit import DeleteView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from utils.auth_decorators import hr_required 
from django.utils.decorators import method_decorator


def handel404(request,exception):
    return render(request,'404.html',status=404)


def handel500(request):
    return render(request,'500.html',status=500)




@method_decorator(hr_required, name='dispatch')
class AssetConditionListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.AssetCondition
    fields= ['name',]
    success_url = '/settings/asset-condition'
    template_name = 'settings/asset_condition.html'
    success_message='Successfully Added a New Condition'


@hr_required
def asset_Condition_delete(request,id):
    object = get_object_or_404(models.AssetCondition , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/asset-condition')



@method_decorator(hr_required, name='dispatch')
class AssetStatusListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.AssetStatus
    fields= ['name',]
    success_url = '/settings/asset-status'
    template_name = 'settings/asset_status.html'
    success_message='Successfully Added a New Status'

@hr_required
def asset_status_delete(request,id):
    object = get_object_or_404(models.AssetStatus , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/asset-status')



@method_decorator(hr_required, name='dispatch')
class AttendanceTypesListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.AttendenceType
    fields= ['name',]
    success_url = '/settings/attendance-types'
    template_name = 'settings/attendance_types.html'
    success_message='Successfully Added a New Type'

@hr_required
def attendance_types_delete(request,id):
    object = get_object_or_404(models.AssetStatus , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/attendance-types')


@method_decorator(hr_required, name='dispatch')
class BankNamesListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.BankName
    fields= ['name',]
    success_url = '/settings/bank-names'
    template_name = 'settings/bank_names.html'
    success_message='Successfully Added a New Bank '

@hr_required
def bank_names_delete(request,id):
    object = get_object_or_404(models.BankName , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/bank-names')


@method_decorator(hr_required, name='dispatch')
class BranchesListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.Branch
    fields= ['name','city']
    success_url = '/settings/branch'
    template_name = 'settings/branch.html'
    success_message='Successfully Added a New Branch'

@hr_required
def branch_delete(request,id):
    object = get_object_or_404(models.Branch , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/branch')


@method_decorator(hr_required, name='dispatch')
class CityListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.City
    fields= ['name',]
    success_url = '/settings/city'
    template_name = 'settings/city.html'
    success_message='Successfully Added a New City'

@hr_required
def city_delete(request,id):
    object = get_object_or_404(models.City , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/city')


@method_decorator(hr_required, name='dispatch')
class DiscountTypesListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.DiscountType
    fields= ['name',]
    success_url = '/settings/discount-types'
    template_name = 'settings/discount_types.html'
    success_message='Successfully Added a New Type'

@hr_required
def discount_types_delete(request,id):
    object = get_object_or_404(models.DiscountType , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/discount-types')



@method_decorator(hr_required, name='dispatch')
class EmployeeStatusListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.EmployeeStatus
    fields= ['name',]
    success_url = '/settings/employee-status'
    template_name = 'settings/employee_status.html'
    success_message='Successfully Added a New Status'

@hr_required
def employee_status_delete(request,id):
    object = get_object_or_404(models.EmployeeStatus , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/employee-status')




@method_decorator(hr_required, name='dispatch')
class FollowerTypesListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.FollowerType
    fields= ['name',]
    success_url = '/settings/follower-types'
    template_name = 'settings/follower_type.html'
    success_message='Successfully Added a New Type'

@hr_required
def follower_type_delete(request,id):
    object = get_object_or_404(models.FollowerType , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/follower-types')



@method_decorator(hr_required, name='dispatch')
class InsuranceClassListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.InsuranceClass
    fields= ['name',]
    success_url = '/settings/insurance-class'
    template_name = 'settings/insurance_class.html'
    success_message='Successfully Added a New Class'

@hr_required
def insurance_class_delete(request,id):
    object = get_object_or_404(models.InsuranceClass , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/insurance-class')





@method_decorator(hr_required, name='dispatch')
class InsuranceCompanyListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.InsuranceCompany
    fields= ['name',]
    success_url = '/settings/insurance-company'
    template_name = 'settings/insurance_company.html'
    success_message='Successfully Added a New Company'

@hr_required
def insurance_company_delete(request,id):
    object = get_object_or_404(models.InsuranceCompany , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/insuranceocpmany')




@method_decorator(hr_required, name='dispatch')
class JobGradeListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.JobGrade
    fields= ['name',]
    success_url = '/settings/job-grade'
    template_name = 'settings/job_grade.html'
    success_message='Successfully Added a New Grade'

@hr_required
def job_grade_delete(request,id):
    object = get_object_or_404(models.JobGrade , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/job-grade')






@method_decorator(hr_required, name='dispatch')
class ProjectPeriorityListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.ProjectPeriority
    fields= ['name',]
    success_url = '/settings/project-periority'
    template_name = 'settings/project_periority.html'
    success_message='Successfully Added a New Periority'

@hr_required
def project_periority_delete(request,id):
    object = get_object_or_404(models.ProjectPeriority , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/project-periority')







@method_decorator(hr_required, name='dispatch')
class ProjectStatusListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.ProjectStatus
    fields= ['name',]
    success_url = '/settings/project-status'
    template_name = 'settings/project_status.html'
    success_message='Successfully Added a New Status'

@hr_required
def project_status_delete(request,id):
    object = get_object_or_404(models.ProjectStatus , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/project-status')



@method_decorator(hr_required, name='dispatch')
class QualificationListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.Qualifications
    fields= ['name',]
    success_url = '/settings/qualifications'
    template_name = 'settings/qualifications.html'
    success_message='Successfully Added a New Qualification'

@hr_required
def qualifications_delete(request,id):
    object = get_object_or_404(models.Qualifications , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/qualifications')



@method_decorator(hr_required, name='dispatch')
class ReasonToTerminateListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.ReasonToTerminate
    fields= ['name',]
    success_url = '/settings/reason-to-terminate'
    template_name = 'settings/reason_to_terminate.html'
    success_message='Successfully Added a New reason'

@hr_required
def reason_to_terminate_delete(request,id):
    object = get_object_or_404(models.ReasonToTerminate , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/reason-to-terminate')



@method_decorator(hr_required, name='dispatch')
class ReplacementPeriodListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.ReplacementPeriod
    fields= ['name',]
    success_url = '/settings/replacement-period'
    template_name = 'settings/replacement_period.html'
    success_message='Successfully Added a New Period'

@hr_required
def replacement_period_delete(request,id):
    object = get_object_or_404(models.ReplacementPeriod , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/replacement-period')





@method_decorator(hr_required, name='dispatch')
class ReplacementTypeListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.ReplacementType
    fields= ['name',]
    success_url = '/settings/replacement-type'
    template_name = 'settings/replacement_type.html'
    success_message='Successfully Added a New Type'

@hr_required
def replacement_type_delete(request,id):
    object = get_object_or_404(models.ReplacementType , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/replacement-type')


@method_decorator(hr_required, name='dispatch')
class SalaryPayTypesListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.SalaryPayType
    fields= ['name',]
    success_url = '/settings/salary-pay-types'
    template_name = 'settings/salary_pay_types.html'
    success_message='Successfully Added a New Type'

@hr_required
def salary_pay_types_delete(request,id):
    object = get_object_or_404(models.SalaryPayType , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/salary-pay-types')


@method_decorator(hr_required, name='dispatch')
class SalaryTypeListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.SalaryType
    fields= ['name',]
    success_url = '/settings/salary-type'
    template_name = 'settings/salary_type.html'
    success_message='Successfully Added a New Type'

@hr_required
def salary_type_delete(request,id):
    object = get_object_or_404(models.SalaryType , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/salary-type')


@method_decorator(hr_required, name='dispatch')
class TcketTypeListCreateView(SuccessMessageMixin,CreateView , ListView):
    model = models.TicketType
    fields= ['name',]
    success_url = '/settings/ticket-type'
    template_name = 'settings/ticket_type.html'
    success_message='Successfully Added a New Type'


@hr_required
def ticket_type_delete(request,id):
    object = get_object_or_404(models.TicketType , id=id)
    object.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/settings/ticket-type')
