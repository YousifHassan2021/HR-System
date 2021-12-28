from django.shortcuts import render , redirect
from . import models
from settings.models import Company
from accounts.models import User , UserProfile , UserContact
from .forms import RegisterForm
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    banner = models.HomeBanner.objects.last()
    added_value = models.AddedValueSection.objects.last()
    core_features = models.CoreFeatures.objects.last()
    sub_features = models.SubFeatureHeading.objects.last()
    software_benefit = models.SoftwareBenefit.objects.last()
    analysis = models.Analysis.objects.last()
    customer_review = models.CustomerReviewTitle.objects.last()
    midd_banner = models.Feature.objects.get(banner=True)

    return render(request,'website/home.html',{
        'banner' : banner , 
        'added_value' : added_value , 
        'core_features' : core_features , 
        'sub_feature' : sub_features , 
        'software_benefit' : software_benefit , 
        'analysis' : analysis , 
        'customer_review' : customer_review,
        'midd_banner':midd_banner
    })




def about(request):
    
    return render(request,'website/about.html',{})




def contact(request):
    
    return render(request,'website/contact.html',{})




def new_company(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            companyname = form.cleaned_data['company_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password_confirm = form.cleaned_data['password_confirm']
            
            new_company = Company.objects.create(company_name=companyname)
            if password == password_confirm : 
                new_user = User.objects.create(username=username , password=password)
                new_user.is_hr = True
                new_user.save()

                user_contact = get_object_or_404(UserContact , user=new_user)
                user_contact.email = email 
                user_contact.save()

                new_profile = UserProfile.objects.create(company=new_company , user=new_user)


                ### login & update session

                title = f'Congratualtions {companyname}'
                message = f' Welcome {username} , thanks for joining Us'

                send_mail(
                    title,
                    message,
                    settings.EMAIL_HOST_USER,
                    [email],
                    fail_silently=False,
                )

                return redirect('/dashboard')

    else: 
        form = RegisterForm()
    return render(request,'website/new_company.html',{'form':form})