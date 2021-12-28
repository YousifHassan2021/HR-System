from django.contrib import admin

# Register your models here.

from . import models 


admin.site.register(models.User)
admin.site.register(models.UserProfile)
admin.site.register(models.UserAccountsConnection)
admin.site.register(models.UserContact)
admin.site.register(models.UserContract)
# admin.site.register(models.UserDiscounts)
admin.site.register(models.UserFollowers)
admin.site.register(models.UserJob)
admin.site.register(models.UserMedicalInsurance)
admin.site.register(models.UserReplacements)
admin.site.register(models.UserSalary)
admin.site.register(models.UserSocialInsurance)
admin.site.register(models.UserTravel)
admin.site.register(models.UserPromotion)
admin.site.register(models.UserAssets)
admin.site.register(models.UserTermination)
admin.site.register(models.UserOverTime)
admin.site.register(models.UserResign)

class UserTrainingAdmin(admin.ModelAdmin):
    # list_filter = ['employees',]
    search_fields = ('employees',)
    # raw_id_fields = ('employees',)
    # autocomplete_fields = ('employees',)

admin.site.register(models.UserTraining,UserTrainingAdmin)

class UserAttendanceAdmin(admin.ModelAdmin):
    list_display = ['user','time_in','time_out']


admin.site.register(models.UserAttendance,UserAttendanceAdmin)