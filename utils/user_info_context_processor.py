from accounts.models import UserProfile
#from django.contrib.auth.models import User 
from django.shortcuts import get_object_or_404
import datetime


def user_info(request):
    user_profile = get_object_or_404(UserProfile , user=request.user)
    today = datetime.datetime.now()
    return {'user':user_profile , 'today' : today}