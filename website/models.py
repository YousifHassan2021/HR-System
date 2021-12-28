from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(_("Logo"), upload_to='company/')
    email = models.EmailField(_("Email"), max_length=254)
    address = models.CharField(max_length=120)
    mobile_number = models.CharField(max_length=22)
    youtube_link = models.URLField(_("Youtube Link"), max_length=200)
    facebook_link = models.URLField(_("facebook Link"), max_length=200)
    twitter_link = models.URLField(_("twitter Link"), max_length=200)
    about_company = models.TextField(_("About Company"))

    def __str__(self):
        return self.name



class HomeBanner(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    subtitle = models.TextField(_("Subtitle"))
    button_toggle = models.BooleanField(_("Button Toggle") , default=True)
    button_text = models.CharField(max_length=50)
    button_link = models.URLField(_("Link"), max_length=200)
    image = models.ImageField(_("Image"), upload_to='home/')

    def __str__(self):
        return self.title



class AddedValueSection(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    derscription = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to='home/')  
    button_toggle = models.BooleanField(_("Button Toggle") , default=True)
    button_text = models.CharField(max_length=50)  
    button_link = models.URLField(_("Link"), max_length=200)   
    value1 = models.CharField(max_length=100 , blank=True, null=True)
    value2 = models.CharField(max_length=100 , blank=True, null=True)
    value3 = models.CharField(max_length=100 , blank=True, null=True)
    value4 = models.CharField(max_length=100 , blank=True, null=True)

    def __str__(self):
        return self.title


class CoreFeatures(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    features = models.ManyToManyField("Feature", verbose_name=_("Features"))

    def __str__(self):
        return self.title


class Feature(models.Model):
    main_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    derscription = models.TextField(_("Description"))
    button_toggle = models.BooleanField(_("Button Toggle") , default=True)
    button_text = models.CharField(max_length=50)
    button_link = models.URLField(_("Link"), max_length=200)   
    image = models.ImageField(_("Image"), upload_to='feature/')  
    order = models.IntegerField(_("Order"))
    active = models.BooleanField(_("Active"),default=True)
    banner = models.BooleanField(_("Banner"),default=False)

    def __str__(self):
        return self.title



class SubFeatureHeading(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)  
    sub_features = models.ManyToManyField("SubFeatures", verbose_name=_("Sub Features"))  

    def __str__(self):
        return self.title


class SubFeatures(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)    
    image = models.ImageField(_("Image"), upload_to='feature/')  
    order = models.IntegerField(_("Order"))
    active = models.BooleanField(_("Active"),default=True)

    def __str__(self):
        return self.title


class SoftwareBenefit(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    derscription = models.TextField(_("Description"))
    image = models.ImageField(_("Image"), upload_to='home/')  
    statics1_title =  models.CharField(max_length=100)  
    statics1_icon =  models.ImageField(_("Image"), upload_to='benefit/') 
    statics1_number = models.IntegerField(_("Statics 1 Number"))
    statics2_title =  models.CharField(max_length=100)  
    statics2_icon =  models.ImageField(_("Image"), upload_to='benefit/') 
    statics2_number = models.IntegerField(_("Statics 1 Number"))

    def __str__(self):
        return self.title


class Analysis(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    derscription = models.TextField(_("Description"))
    button_toggle = models.BooleanField(_("Button Toggle") , default=True)
    button_text = models.CharField(max_length=50)   
    button_link = models.URLField(_("Link"), max_length=200)
    value1 = models.CharField(max_length=100 , blank=True, null=True)
    value2 = models.CharField(max_length=100 , blank=True, null=True)
    value3 = models.CharField(max_length=100 , blank=True, null=True)
    value4 = models.CharField(max_length=100 , blank=True, null=True)

    feature1_title =  models.CharField(max_length=100)  
    feature1_icon =  models.ImageField(_("Image"), upload_to='benefit/') 
    feature1_description = models.TextField(_("Description"))

    feature2_title =  models.CharField(max_length=100)  
    feature2_icon =  models.ImageField(_("Image"), upload_to='benefit/') 
    feature2_description = models.TextField(_("Description"))

    feature3_title =  models.CharField(max_length=100)  
    feature3_icon =  models.ImageField(_("Image"), upload_to='benefit/') 
    feature3_description = models.TextField(_("Description"))

    feature4_title =  models.CharField(max_length=100)  
    feature4_icon =  models.ImageField(_("Image"), upload_to='benefit/') 
    feature4_description = models.TextField(_("Description"))

    def __str__(self):
        return self.title



class CustomerReviewTitle(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    reviews = models.ManyToManyField("Review", verbose_name=_("Review"))

    def __str__(self):
        return self.title


class Review(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(_("Subtitle"),max_length=100)
    review = models.TextField(_("Review"))
    image = models.ImageField(_("Image"), upload_to='home/')  

    def __str__(self):
        return self.name


 