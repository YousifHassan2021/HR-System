from hr.models import Announcement




def get_announcements(request):
    announcements = Announcement.objects.all()
    print(announcements)
    return {'announcements' : announcements}