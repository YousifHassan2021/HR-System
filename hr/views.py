from django.shortcuts import render , redirect
from accounts.forms import UserProfileForm , UserForm , UserTrainingForm , UserPromotionForm , UserAssetsForm , UserTerminationForm
from settings import models as st_models
from settings import forms as st_forms
from django.shortcuts import get_object_or_404
from accounts import models
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib import messages
from . models import Announcement
from django.conf import settings
from utils.auth_decorators import hr_required 
from utils.ajax_form_save import save_form
from django.http import JsonResponse
from django.template.loader import render_to_string
from accounts.forms import UserForm , UserProfileForm , UserReplacementForm , UserOverTimeForm , PayslipFilterForm





def employee_create(request):
    employees = models.User.objects.all()
    data =  dict()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        userprofileform = UserProfileForm(request.POST)
        if userform.is_valid() and userprofileform.is_valid():
            print('in form')
            username = userform.cleaned_data['username']
            password = st_models.DefaultPassword.objects.last()
            models.User.objects.create(username=username , password=password)

            userprofile = userprofileform.save(commit=False)
            userprofile.user = models.User.objects.get(username=username)
            userprofile.save()

            data['form_is_valid'] = True
            employees = models.User.objects.all()
            data['model_list'] = render_to_string('includes/employee/employee_list.html',{'object_list':employees,'request':request})
        
        else:
            print('Not Valid')
            data['form_is_valid'] = False

    else:
        userform = UserForm()
        userprofileform = UserProfileForm()
        context = {'userform':userform , 'userprofileform' : userprofileform}
        data['html_form'] = render_to_string('includes/employee/employee_create.html',context,request=request)
    return JsonResponse(data)       






def employee_edit(request,id):
    print('In Edit')
    user = get_object_or_404(models.User,id=id)
    userprofile = get_object_or_404(models.UserProfile,user=user)
    data =  dict()
    if request.method == 'POST':
        print('In Post')
        userform = UserForm(request.POST,instance=user)
        userprofileform = UserProfileForm(request.POST,request.FILES,instance=userprofile)
        if  userform.is_valid() and userprofileform.is_valid():
            print('valid')
            userform.save()
            userprofileform.save()
            data['form_is_valid'] = True
            employees = models.User.objects.all()
            data['model_list'] = render_to_string('includes/employee/employee_list.html',{'object_list':employees,'request':request})
        
        else:
            print('Not Valid')
            data['form_is_valid'] = False

    else:
        userform = UserForm(instance =user)
        userprofileform = UserProfileForm(instance=userprofile)
        context = {'userprofileform' : userprofileform,'userform':userform}
        data['html_form'] = render_to_string('includes/employee/employee_update.html',context,request=request)
    return JsonResponse(data)   


# @hr_required
def employee_delete(request, id):
    user = get_object_or_404(models.User , id=id)
    data = dict()
    if request.method == 'POST':
        user.delete()
        data['form_is_valid'] = True
        employees = models.User.objects.all()
        data['model_list'] = render_to_string('includes/employee/employee_list.html',{'object_list':employees,'request':request})
        
    else:
        data['form_is_valid'] = False
        context = {'employee':user}
        data['html_form'] = render_to_string('includes/employee/employee_delete.html',context,request=request)
    return JsonResponse(data)



def employee_search(request):
    pass







#####################
@hr_required
def deparment_management(request):
    departments = st_models.Department_Section.objects.all()
    departments_count = st_models.Department_Section.objects.all().count()
    page = request.GET.get('page', 1)

    paginator = Paginator(departments, 5)
    try:
        departments = paginator.page(page)
    except PageNotAnInteger:
        departments = paginator.page(1)
    except EmptyPage:
        departments = paginator.page(paginator.num_pages)

    return render(request,'hr/departments.html',{'object_list':departments , 'depratments_count':departments_count})


def department_create(request):
    departments = st_models.Department_Section.objects.all()
    if request.method == 'POST':
        form = st_forms.DepartmentSectionForm(request.POST)

    else:
        form = st_forms.DepartmentSectionForm()
    return save_form(request,form,departments,'includes/departments_list.html','includes/department_create.html')



def department_delete(request,id):
    department = get_object_or_404(st_models.Department_Section , id=id)
    data = dict()
    if request.method == 'POST':
        department.delete()
        data['form_is_valid'] = True
        departments = st_models.Department_Section.objects.all()
        data['model_list'] = render_to_string('includes/departments_list.html',{'object_list':departments})
        
    else:
        data['form_is_valid'] = False
        context = {'department':department}
        data['html_form'] = render_to_string('includes/department_delete.html',context,request=request)
    return JsonResponse(data)


def department_edit(request,id):
    department = get_object_or_404(st_models.Department_Section , id=id)
    departments = st_models.Department_Section.objects.all()
    if request.method == 'POST':
        form = st_forms.DepartmentSectionForm(request.POST , instance=department)

    else:
        form = st_forms.DepartmentSectionForm(instance=department)

    return save_form(request,form,departments,'includes/departments_list.html','includes/departments_update.html')


#####################

def job_management(request):
    jobs = st_models.JobType.objects.all()
    return render(request,'hr/jobs.html',{'object_list':jobs })


def job_create(request):
    jobs = st_models.JobType.objects.all()
    if request.method == 'POST':
        form = st_forms.JobTypeForm(request.POST)

    else:
        form = st_forms.JobTypeForm()
    return save_form(request,form,jobs,'includes/jobs_list.html','includes/job_create.html')


def job_delete(request,id):
    job = get_object_or_404(st_models.JobType , id=id)
    data = dict()
    if request.method == 'POST':
        job.delete()
        data['form_is_valid'] = True
        jobs = st_models.JobType.objects.all()
        data['model_list'] = render_to_string('includes/jobs_list.html',{'object_list':jobs})
        
    else:
        data['form_is_valid'] = False
        context = {'job':job}
        data['html_form'] = render_to_string('includes/job_delete.html',context,request=request)
    return JsonResponse(data)



    # messages.warning(request, 'Successfully Deleted ')
    # return redirect('/hr/jobs')


def job_edit(request,id):
    job = get_object_or_404(st_models.JobType , id=id)
    jobs = st_models.JobType.objects.all()
    if request.method == 'POST':
        form = st_forms.JobTypeForm(request.POST , instance=job)

    else:
        form = st_forms.JobTypeForm(instance=job)

    return save_form(request,form,jobs,'includes/jobs_list.html','includes/jobs_update.html')


############


def employee_salary_management(request):
    salary = models.UserSalary.objects.all()
    return render(request,'hr/salary.html',{'salaries':salary})

def employee_salary_detail(request):
    pass


def employee_salary_add(request):
    pass


def employee_salary_search(request):
    pass


########
def project_report_list(request):
    
    pass

def project_report_detail(request):
    pass


#####
def employee_info_report(request):
    employees = User.objects.all()
    return render(request,'hr/employee-reports.html',{'employees':employees})


def employee_report_filter(request):
    pass


def employee_report_export(request):
    pass


###
def employee_performance_indicator_list(request):
    pass


def employee_performance_indicator_edit(request):
    pass

def employee_performance_indicator_delete(request):
    pass


def employee_performance_indicator_add(request):
    pass



def employee_performance_review_add(request):
    pass



def employee_performance_apraisel_edit(request):
    pass

def employee_performance_apraisel_delete(request):
    pass


def employee_performance_apraisel_add(request):
    pass


#################
def training_management(request):
    trainings = models.UserTraining.objects.all()
    return render(request,'hr/training.html',{'object_list':trainings })




def training_create(request):
    trainings = models.UserTraining.objects.all()
    if request.method == 'POST':
        form = UserTrainingForm(request.POST)

    else:
        form = UserTrainingForm(request.POST)
    return save_form(request,form,trainings,'includes/training_list.html','includes/training_create.html')



def training_edit(request,id):
    training = get_object_or_404(models.UserTraining , id=id)
    trainings = models.UserTraining.objects.all()
    if request.method == 'POST':
        form = UserTrainingForm(request.POST , instance=training)

    else:
        form = UserTrainingForm(instance=training)

    return save_form(request,form,trainings,'includes/training_list.html','includes/training_update.html')



def training_staus_update(request):
    pass


def training_delete(request,id):
    training = get_object_or_404(models.UserTraining , id=id)
    data = dict()
    if request.method == 'POST':
        training.delete()
        data['form_is_valid'] = True
        trainings = models.UserTraining.objects.all()
        data['model_list'] = render_to_string('includes/training_list.html',{'object_list':trainings})
        
    else:
        data['form_is_valid'] = False
        context = {'training':training}
        data['html_form'] = render_to_string('includes/training_delete.html',context,request=request)
    return JsonResponse(data)


#################
def training_type_management(request):
    trainings_types = st_models.TrainingCourse.objects.all()
    return render(request,'hr/training-type.html',{'object_list' : trainings_types })



def training_type_create(request):
    trainings_types = st_models.TrainingCourse.objects.all()
    if request.method == 'POST':
        form = st_forms.TrainingCourseForm(request.POST)

    else:
        form = st_forms.TrainingCourseForm(request.POST)
    return save_form(request,form,trainings_types,'includes/training_type_list.html','includes/training_type_create.html')


def training_type_edit(request,id):
    trainings_type = get_object_or_404(st_models.TrainingCourse , id=id)
    trainings_types =  st_models.TrainingCourse.objects.all()
    if request.method == 'POST':
        form = st_forms.TrainingCourseForm(request.POST , instance=trainings_type)

    else:
        form = st_forms.TrainingCourseForm(instance=trainings_type)

    return save_form(request,form,trainings_types,'includes/training_type_list.html','includes/training_type_update.html')



def training_type_staus_update(request):
    pass


def training_type_delete(request,id):
    training_type = get_object_or_404(st_models.TrainingCourse , id=id)
    data = dict()
    if request.method == 'POST':
        training_type.delete()
        data['form_is_valid'] = True
        trainings_types = st_models.TrainingCourse.objects.all()
        messages.warning(request, 'Successfully Deleted ')
        data['model_list'] = render_to_string('includes/training_type_list.html',{'object_list':trainings_types})
        
    else:
        data['form_is_valid'] = False
        context = {'training':training_type}
        data['html_form'] = render_to_string('includes/training_type_delete.html',context,request=request)
    return JsonResponse(data)

#################
def promotion_management(request):
    promotions = models.UserPromotion.objects.all()
    return render(request,'hr/promotion.html',{'object_list' :promotions})


def promotion_create(request):
    promotions = models.UserPromotion.objects.all()
    if request.method == 'POST':
        form = UserPromotionForm(request.POST)

    else:
        form = UserPromotionForm()
    return save_form(request,form,promotions,'includes/promotion_list.html','includes/promotion_create.html')



def promotion_edit(request,id):
    promotion = get_object_or_404(models.UserPromotion , id=id)
    promotions = models.UserPromotion.objects.all()
    if request.method == 'POST':
        form = UserPromotionForm(request.POST , instance=promotion)

    else:
        form = UserPromotionForm(instance=promotion)

    return save_form(request,form,promotions,'includes/promotion_list.html','includes/promotion_update.html')



def promotion_delete(request,id):
    promotion = get_object_or_404(models.UserPromotion , id=id)
    data = dict()
    if request.method == 'POST':
        promotion.delete()
        data['form_is_valid'] = True
        promotions = models.UserPromotion.objects.all()
        data['model_list'] = render_to_string('includes/promotion_list.html',{'object_list':promotions})
        
    else:
        data['form_is_valid'] = False
        context = {'promotion':promotion}
        data['html_form'] = render_to_string('includes/promotion_delete.html',context,request=request)
    return JsonResponse(data)


#######
def employee_termination_add(request):
    pass


def asset_management(request):
    assets = models.UserAssets.objects.all()
    return render(request,'hr/assets.html',{'object_list':assets})



def asset_create(request):
    data = dict()
    if request.method == 'POST':
        form1 = UserAssetsForm(request.POST)
        form2 = st_forms.AssetForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            form2.save()
            myform = form1.save(commit=False)
            myform.asset = st_models.Assets.objects.last()
            myform.save()
            assets = models.UserAssets.objects.all()
            data['form_is_valid'] = True
            data['model_list'] = render_to_string('includes/asset_list.html',{'object_list':assets})
        
        else:
            data['form_is_valid'] = False

    else:
        form1 = UserAssetsForm()
        form2 = st_forms.AssetForm()
        context = {'form1':form1 , 'form2':form2}
        data['html_form'] = render_to_string('includes/asset_create.html',context,request=request)

    return JsonResponse(data)
    # return save_form(request,form,departments,'includes/departments_list.html','includes/department_create.html')






def asset_delete(request,id):
    asset = get_object_or_404(models.UserAssets , id=id)
    data = dict()
    if request.method == 'POST':
        st_asset = get_object_or_404(st_models.Assets , id=asset.asset.id)
        st_asset.delete()
        asset.delete()
        data['form_is_valid'] = True
        assets = models.UserAssets.objects.all()
        data['model_list'] = render_to_string('includes/asset_list.html',{'object_list':assets})
        
    else:
        data['form_is_valid'] = False
        context = {'asset':asset}
        data['html_form'] = render_to_string('includes/asset_delete.html',context,request=request)
    return JsonResponse(data)


def asset_edit(request,id):
    user_asset = get_object_or_404(models.UserAssets , id=id)

    data = dict()
    if request.method == 'POST':
        form1 = UserAssetsForm(request.POST,instance=user_asset)
        form2 = st_forms.AssetForm(request.POST,instance=user_asset.asset)
        if form1.is_valid() and form2.is_valid():
            form2.save()
            form1.save()
            assets = models.UserAssets.objects.all()
            data['form_is_valid'] = True
            data['model_list'] = render_to_string('includes/asset_list.html',{'object_list':assets})
        
        else:
            data['form_is_valid'] = False

    else:
        form1 = UserAssetsForm(instance=user_asset)
        form2 = st_forms.AssetForm(instance=user_asset.asset)
        context = {'form1':form1 , 'form2':form2}
        data['html_form'] = render_to_string('includes/asset_update.html',context,request=request)

    return JsonResponse(data)


def asset_search(request):
    pass


######
def company_settings_add(request):
    pass



## termination 
def employee_termination(request):
    terminations = models.UserTermination.objects.all()

    if request.method == 'POST':
        form = UserTerminationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Added a New Termination')

    else:
        form = UserTerminationForm()

    return render(request,'hr/termination.html',{'form' : form ,'terminations' :terminations })




def employee_termination_delete(request,id):
    termination = get_object_or_404(models.UserTermination , id=id)
    termination.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/hr/termination')


## holiday
def employee_holidays(request):
    today = datetime.datetime.now()
    holidays = st_models.Holiday.objects.filter(date_from__year=today.year)
    return render(request,'hr/holidays.html',{'object_list':holidays , 'year':today.year})



def holiday_create(request):
    holidays = st_models.Holiday.objects.all()
    if request.method == 'POST':
        form = st_forms.HolidayForm(request.POST)

    else:
        form = st_forms.HolidayForm()
    return save_form(request,form,holidays,'includes/holiday_list.html','includes/holiday_create.html')



def holiday_delete(request,id):
    holiday = get_object_or_404(st_models.Holiday , id=id)
    data = dict()
    if request.method == 'POST':
        holiday.delete()
        data['form_is_valid'] = True
        holidays = st_models.Holiday.objects.all()
        data['model_list'] = render_to_string('includes/holiday_list.html',{'object_list':holidays})
        
    else:
        data['form_is_valid'] = False
        context = {'holiday':holiday}
        data['html_form'] = render_to_string('includes/holiday_delete.html',context,request=request)
    return JsonResponse(data)







def all_anouncements(request):
    announcements = Announcement.objects.all()
    return render(request,'hr/activities.html',{'announcements':announcements})



# @login_required
def employees_attendance(request):
    today = datetime.date.today()
    attendance = models.UserAttendance.objects.filter(time_in__year=today.year,
                           time_in__month=today.month)

    print(attendance)

    return render(request,'hr/employess_attendance.html',{'attendance':attendance})

# @login_required
def employee_attendance(request,id):
    return render(request,'hr/employee_attendance.html',{})



### Payrolls
def payroll_overtime(request):
    overtime = models.UserOverTime.objects.all()
    return render(request,'hr/payroll-overtime.html',{'object_list':overtime})

def payroll_overtime_create(request):
    additionss = models.UserOverTime.objects.all()
    if request.method == 'POST':
        form = UserOverTimeForm(request.POST)
    else:
        form = UserOverTimeForm()
    return save_form(request,form,additionss,'includes/payroll_overtime_list.html','includes/payroll_overtime_create.html')


def payroll_overtime_edit(request,id):
    overtime = get_object_or_404(models.UserOverTime , id=id)
    overtimes = models.UserOverTime.objects.all()
    if request.method == 'POST':
        form = UserOverTimeForm(request.POST , instance=overtime)

    else:
        form = UserOverTimeForm(instance=overtime)
    return save_form(request,form,overtimes,'includes/payroll_overtime_list.html','includes/payroll_overtime_update.html')


def payroll_overtime_delete(request,id):
    overtime = get_object_or_404(models.UserOverTime , id=id)
    data = dict()
    if request.method == 'POST':
        overtime.delete()
        data['form_is_valid'] = True
        overtimes = models.UserOverTime.objects.all()
        data['model_list'] = render_to_string('includes/payroll_overtime_list.html',{'object_list':overtimes})
        
    else:
        data['form_is_valid'] = False
        context = {'overtime':overtime}
        data['html_form'] = render_to_string('includes/payroll_overtime_delete.html',context,request=request)
    return JsonResponse(data)



def payroll_addition(request):
    additions = models.UserReplacements.objects.all()
    return render(request,'hr/payroll-addition.html',{'object_list':additions})

def payroll_addition_create(request):
    additionss = models.UserReplacements.objects.all()
    if request.method == 'POST':
        form = UserReplacementForm(request.POST)
    else:
        form = UserReplacementForm()
    return save_form(request,form,additionss,'includes/payroll_addition_list.html','includes/payroll_addition_create.html')


def payroll_addition_edit(request,id):
    addition = get_object_or_404(models.UserReplacements , id=id)
    additions = models.UserReplacements.objects.all()
    if request.method == 'POST':
        form = UserReplacementForm(request.POST , instance=addition)

    else:
        form = UserReplacementForm(instance=addition)
    return save_form(request,form,additions,'includes/payroll_addition_list.html','includes/payroll_addition_update.html')


def payroll_addition_delte(request,id):
    addition = get_object_or_404(models.UserReplacements , id=id)
    data = dict()
    if request.method == 'POST':
        addition.delete()
        data['form_is_valid'] = True
        additions = models.UserReplacements.objects.all()
        data['model_list'] = render_to_string('includes/payroll_addition_list.html',{'object_list':additions})
        
    else:
        data['form_is_valid'] = False
        context = {'addition':addition}
        data['html_form'] = render_to_string('includes/payroll_addition_delete.html',context,request=request)
    return JsonResponse(data)





def payslip_view(request):
    if request.method == 'POST':
        form = PayslipFilterForm()

    else:
        form = PayslipFilterForm()
    return render(request,'hr/salary-detail.html',{'form':form})

#### settings

def company_settings(request):
    
    return render(request,'hr/company-settings.html',{})




