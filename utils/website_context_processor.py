from website.models import Company



def company(request):
    comapny = Company.objects.last()
    return {'company':comapny}