from settings.models import Company


def company_info(request):
    info = Company.objects.last()
    return {'info':info}