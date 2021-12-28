from django.shortcuts import render
from managers.models import Project , Client
from managers.forms import ProjectForm
from django.contrib import messages
from django.shortcuts  import get_object_or_404
from .models import User , UserAttendance , UserProfile , UserJob , UserContact , UserSalary , UserSocialInsurance , UserMedicalInsurance , UserFollowers
import datetime
import settings.models as st_models
from .forms import UserForm , UserProfileForm
from django.http import HttpResponse
import xlwt
from django.contrib.auth.decorators import login_required
from django.db.models import Count

@login_required
def dashboard(request):
    if request.user.is_hr:
        projects_count = Project.objects.all().count()
        clients_count = Client.objects.all().count()
        employee_count= User.objects.all().count()
        pending_requests_count = ''


        # context['categories'] = Category.objects.all().annotate(post_count=Count('post_category'))

        # section = st_models.Department_Section.objects.all().annotate(employee_count=Count('user_department_section'))

        # section_data = [{'y':i.name,'a':i.employee_count} for i in section]

        # print(section_data)


        dataset = st_models.Department_Section.objects.values('name').annotate(employee_count=Count('user_department_section'))

        print(dataset)

        context = {
            'projects_count' : projects_count , 
            'clients_count' : clients_count , 
            'employee_count' : employee_count , 
            'pending_requests_count' : pending_requests_count , 
            'data' : dataset

        }

        return render(request,'hr/dashboard.html',context)


    elif request.user.is_manager:
        return render(request,'managers/dashboard.html',{})

    
    else:
        return render(request,'employee/dashboard.html',{})




#### user
def profile(request):
    user_profile = get_object_or_404(UserProfile , user=request.user)
    # user_contact = get_object_or_404(UserContact , user=request.user)
    # user_job = get_object_or_404(UserJob, user=request.user)
    # user_salary = get_object_or_404(UserSalary, user=request.user)
    # social_insurance = get_object_or_404(UserSocialInsurance , user=request.user)
    # media_insuarance = get_object_or_404(UserMedicalInsurance , user=request.user)
    # user_followers = UserFollowers.objects.filter(user=request.user)

    return render(request,'accounts/profile.html',{
        'user_profile' : user_profile , 
        # 'user_contact' : user_contact , 
        # 'user_job' : user_job , 
        # 'user_salary' : user_salary , 
        # 'social_insurance' : social_insurance , 
        # 'media_insuarance' : media_insuarance , 
        # 'user_followers' : user_followers
    })




@login_required
def project_list(request):
    projects = Project.objects.filter(manager=request.user)
    return render(request,'accounts/projects.html',{'object_list':projects})


@login_required
def project_detail(request,id):
    project = get_object_or_404(Project , id=id)
    return render(request,'accounts/project-view.html',{'project':project})


@login_required
def employee_management(request):
    if request.user.is_hr:
        employees = User.objects.all()

    elif request.user.is_manager:
        employees = User.objects.all()  ## filter by current manager
 
    return render(request,'accounts/employees.html',{'object_list':employees})



@login_required
def employee_detail(request,id):
    user_profile = get_object_or_404(UserProfile , user=request.user)
    return render(request,'accounts/profile.html',{'user_profile':user_profile})


@login_required
def employee_export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['content-Disposition'] = 'attachement; filename=employees' + str(datetime.datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    sheet1 = wb.add_sheet('Employees')
    font_style = xlwt.XFStyle()
    font_style.font.blod=True  

    # row_num = 0
    # columns = ['ar_name' , 'en_name']

    # for col_num in range(len(columns)):
    #     ws.write(row_num , col_num , columns[col_num] , font_style)

    # employees = User.objects.all()
    # for row in employees:
    #     row_num += 1

    #     print(row)

    #     for col_num in range(len(row)):
    #         ws.write(row_num,col_num,str(row[col_num]),font_style)


    sheet1.write(0,1, "ar name")
    sheet1.write(0,2,"en name")


    ''' export : 
        - name  -job title  -hire date  -job_id  -department  -manager'''

    row_number = 2
    employees = UserProfile.objects.all().values_list('ar_name','en_name','job_number')
    for row in employees :
        column_num = 1
        for item in row :
            sheet1.write(row_number,column_num,str(item) )
            column_num = column_num + 1
        row_number = row_number + 1

    wb.save(response)
    return response




