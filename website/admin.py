from django.contrib import admin

# Register your models here.
from . import models 



admin.site.register(models.Company)
admin.site.register(models.Feature)
admin.site.register(models.SubFeatureHeading)
admin.site.register(models.SubFeatures)
admin.site.register(models.CoreFeatures)
admin.site.register(models.CustomerReviewTitle)
admin.site.register(models.Review)
admin.site.register(models.Analysis)
admin.site.register(models.AddedValueSection)
admin.site.register(models.SoftwareBenefit)
admin.site.register(models.HomeBanner)