from django.shortcuts import render , redirect
from accounts import models , forms
from settings import models as st_models
import datetime
from django.db.models import Sum
from collections import Counter
from django.shortcuts  import get_object_or_404
from django.contrib import messages
import managers.models as mn_models
from django.contrib.auth.decorators import login_required
# Create your views here.

def holydays(request):
    today = datetime.datetime.now()
    holidays = st_models.Holiday.objects.filter(date_from__year=today.year)
    return render(request,'employee/holidays.html',{'holidays':holidays , 'today_year' : today.year})


def add_vacation(request):
    messages.success(request, 'Successfully Added a New Vacation')



def my_attendance(request):
    
    return render(request,'employee/attendance-employee.html',{})



def month_overtime(request):
    today = datetime.date.today()
    overtime = models.UserOverTime.objects.filter(user=request.user , date__month=today.month)
    # accepted_overtime = models.UserOverTime.objects.filter(user=request.user , status='Approved' , date__month=today.month).aggregate(Sum('overhours'))
    # rejected_overtime = models.UserOverTime.objects.filter(user=request.user , status='Rejected'  , date__month=today.month).aggregate(Sum('overhours'))
    # pending_overtime = models.UserOverTime.objects.filter(user=request.user , status='Pending', date__month=today.month).aggregate(Sum('overhours'))
    # total = Counter(accepted_overtime)  + Counter(rejected_overtime) + Counter(pending_overtime)
    
    accepted_overtime = models.UserOverTime.objects.filter(user=request.user , status='Approved', date__month=today.month).count()
    rejected_overtime = models.UserOverTime.objects.filter(user=request.user , status='Rejected', date__month=today.month).count()
    pending_overtime = models.UserOverTime.objects.filter(user=request.user , status='Pending', date__month=today.month).count()
    total = models.UserOverTime.objects.filter(user=request.user , status='Approved' , date__month=today.month).aggregate(Sum('overhours'))

    if request.method == 'POST':
        form = forms.OvertimeForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()
            messages.success(request, 'Successfully Added a New overtime')

    else:
        form = forms.OvertimeForm()
    return render(request,'employee/overtime.html',{
        'overtime' : overtime ,
        'form': form ,
        'accepted_overtime': accepted_overtime , 
        'rejected_overtime' : rejected_overtime , 
        'pending_overtime' : pending_overtime,
        'total' : total
        })


def all_overtime(request):
    today = datetime.date.today()
    overtime = models.UserOverTime.objects.filter(user=request.user)
    accepted_overtime = models.UserOverTime.objects.filter(user=request.user , status='Approved').count()
    rejected_overtime = models.UserOverTime.objects.filter(user=request.user , status='Rejected').count()
    pending_overtime = models.UserOverTime.objects.filter(user=request.user , status='Pending').count()
    total = models.UserOverTime.objects.filter(user=request.user , status='Approved' ).aggregate(Sum('overhours'))

    return render(request,'employee/all-overtime.html',{
        'overtime' : overtime ,
        'accepted_overtime': accepted_overtime , 
        'rejected_overtime' : rejected_overtime , 
        'pending_overtime' : pending_overtime,
        'total' : total
        })



def edit_overtime(request):
    pass


def delete_overtime(request,id):
    overtime = get_object_or_404(models.UserOverTime , id=id)
    overtime.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/employee/month-overtime')




def my_salary_list(request):
    
    return render(request,'employee/salary-view.html',{})



def project_report_list(request):
    pass

def project_report_detail(request):
    pass



def cliet_info(request):
    pass


def my_performance_review(request):
    pass



def my_performance_review_approve(request):
    pass



def my_performance_appraisel_review(request):
    pass



def my_performance_review_appraisel_approve(request):
    pass



def my_training(request):
    my_training = models.UserTraining.objects.filter(employees__id=request.user.id)
    return render(request,'employee/training.html',{'my_training': my_training})


def my_promotions(request):
    my_promotions = models.UserPromotion.objects.filter(user=request.user)
    return render(request,'employee/promotion.html',{'my_promotions':my_promotions})


def add_resign(request):
    my_resigns = models.UserResign.objects.filter(user=request.user)
    if request.method == 'POST':
        form = forms.UserResignForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user
            myform.save()

    else:
        form = forms.UserResignForm()
    return render(request,'employee/resignation.html',{'my_resigns':my_resigns,'form':form})


def delete_resign(request,id):
    resign = get_object_or_404(models.UserResign , id=id)
    resign.delete()
    messages.warning(request, 'Successfully Deleted ')
    return redirect('/resign')




def my_assets(request):
    my_assets = models.UserAssets.objects.filter(user=request.user)
    return render(request,'employee/assets.html',{'my_assets':my_assets})


def my_loan(request):

    return render(request,'employee/loan.html',{})
