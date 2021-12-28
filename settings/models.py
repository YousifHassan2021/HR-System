from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django_countries.fields import CountryField
from django.conf import settings
# Create your models here.

# class models.Model(models.Model):
#     name = models.CharField(max_length=100,verbose_name=_('name'))

#     def __str__(self):
#         return self.name

class Branch(models.Model):
    company  = models.ForeignKey('Company', related_name='company_branch', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('name'))
    city = models.ForeignKey('City', verbose_name=_('city'),related_name='branch_city', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    def __str__(self):
            return self.name   


class JobType(models.Model):
    company  = models.ForeignKey('Company', related_name='company_job_type', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('name'))
    department = models.ForeignKey('Department_Section',verbose_name=_('department'), related_name='job_department', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name  


class JobGrade(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_job_grade', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class EmployeeStatus(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_employee_status', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Qualifications(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_qualifications', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Department_Section(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_department_section', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class SalaryType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_salary_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class BankName(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_bank_name', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class AttendenceType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_attendance_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class SalaryPayType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_salary_pay_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


REPLACEMENT_TYPE = (
    ('Monthly' , 'Monthly') , 
    ('Month Count' , 'Month Count')
)

class ReplacementType(models.Model):
    company  = models.ForeignKey('Company', related_name='company_replacement_type', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('name'))
    # type = models.CharField(max_length=15 , choices=REPLACEMENT_TYPE)
    # month_count = models.IntegerField(_("Month Count"), blank=True, null=True)
    # percentage = models.FloatField(_("Percentage") , blank=True, null=True)
    # amount = models.FloatField(_("Amount") , blank=True, null=True)
    def __str__(self):
        return self.name


class ReplacementPeriod(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_replacement_period', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class DiscountType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_discount_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class InsuranceClass(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_insurance_class', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class InsuranceCompany(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_insurance_company', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class TicketType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_ticket_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class RequestType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_request_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class AnnualVacationDays(models.Model):
    company  = models.ForeignKey('Company', related_name='company_annual_vations', on_delete=models.CASCADE)
    count = models.IntegerField(_("Count"))

    def __str__(self):
        return self.count



class VacationType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_vacation_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LeaveReasons(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_leave_reasons', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class LoanType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_loan_type', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ProjectPeriority(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_project_periority', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class TaskStatus(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_task_status', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ReasonToResign(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_reasons_to_resign', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ReasonToTerminate(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_reasons_to_terminate', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class OrganizationPolicies(models.Model):
    company  = models.ForeignKey('Company', related_name='company_organization_policies', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('name'))
    description = models.TextField(_("Description"))
    department_section = models.ForeignKey(Department_Section, verbose_name=_('Department or section'), related_name='organization_department_section', on_delete=models.CASCADE)
    upload_policy = models.FileField(_("Upload Policy"), upload_to='policy/')
    create_date = models.DateField(_("Create Date"),  auto_now_add=True)

    def __str__(self):
        return self.name


class AssetCondition(models.Model):
    company  = models.ForeignKey('Company', related_name='company_asset_condition', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('name'))
    def __str__(self):
        return self.name

class Assets(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_asset', on_delete=models.CASCADE)
    asset_id = models.CharField(max_length=10, verbose_name=_('Asset'),blank=True, null=True)
    purchase_date = models.DateField(_("Purchase Date"), default=timezone.now)
    warranty = models.CharField(max_length=12, verbose_name=_('Warrnty'))
    warranty_end =  models.DateField(_("Warranty End Date"),default= timezone.now)
    amount = models.FloatField(_("Amount"))
    condition = models.ForeignKey(AssetCondition, verbose_name=_('Condition'), related_name='asset_contion', on_delete=models.CASCADE)
    model  = models.CharField(max_length=100, verbose_name=_('Model'))
    serial_number = models.CharField(max_length=50, verbose_name=_('Serial Number')) 
    supplier = models.CharField(max_length=50, verbose_name=_('Supplier'))
    manufacture = models.CharField(max_length=50, verbose_name=_('manufacture'))

    def __str__(self):
        return self.asset_id


class AssetStatus(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_asset_status', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


TRAINING_STATUS = (
    ('ACTIVE' , 'ACTIVE'),
    ('IN ACTIVE' , 'IN ACTIVE')    
)


class TrainingCourse(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_training_course', on_delete=models.CASCADE)
    description = models.TextField(max_length=2000 , verbose_name=_('Description'), default='')
    status =models.CharField(_("status"), max_length=15 , choices = TRAINING_STATUS)
    def __str__(self):
        return self.name

class WorkingHours(models.Model):
    company  = models.ForeignKey('Company', related_name='company_working_hourse', on_delete=models.CASCADE)
    hour_in_over_time = models.FloatField(_("Hour In Over Time"))


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    contact_person = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Contact Person'), related_name='company_contact_user', on_delete=models.CASCADE,blank=True, null=True)
    address = models.CharField(_('Address'),max_length=300 ,default='')
    country = CountryField(blank_label='(select country)',default='')
    city = models.ForeignKey(City, verbose_name=_("city"), on_delete=models.CASCADE , blank=True, null=True)
    postal_code = models.IntegerField(_("Postal Code"),default=0)
    email = models.EmailField(_("Email"), max_length=254,default='')
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone Number'),default='')
    mobile_number = models.CharField(max_length=20, verbose_name=_('Mobile Number'),default='')
    fax_number = models.CharField(max_length=20, verbose_name=_('Fax Number'),default='')
    website_url = models.URLField(_("Website Url"), max_length=200, blank=True, null=True)

    website_name = models.CharField(_("Website Name"), max_length=100 ,default='')
    logo = models.ImageField(_("Logo"), upload_to='logo/' ,default='')
    fav_icon = models.ImageField(_("Fav Icon"), upload_to='icon/' , default='')
    def __str__(self):
        return self.company_name



class CompanyThemeSettings(models.Model):
    company  = models.ForeignKey(Company, related_name='company_settings', on_delete=models.CASCADE)
    website_name = models.CharField(max_length =50, verbose_name=_('Website Name'))
    logo = models.ImageField(_("Logo"), upload_to='company_logo/')
    favicon = models.ImageField(_("FavIcon"), upload_to='company_icon')
    def __str__(self):
        return self.website_name


class DefaultPassword(models.Model):
    company  = models.ForeignKey(Company, related_name='company_default_password', on_delete=models.CASCADE)
    password = models.CharField(_('Default Password'),max_length=20)




# class PayrollItems(models.Model):
#     name = models.CharField(max_length=100)



class FollowerType(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_follower_type', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



class Holiday(models.Model):
    name = models.CharField(max_length=100,verbose_name=_('name'))
    company  = models.ForeignKey('Company', related_name='company_holiday', on_delete=models.CASCADE)
    date_from = models.DateField(_("Date From") , default=timezone.now)
    date_to = models.DateField(_("Date From") , default=timezone.now)


    def __str__(self):
        return self.name



class ProjectStatus(models.Model):
    company  = models.ForeignKey('Company', related_name='company_project_status', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,verbose_name=_('name'))

    def __str__(self):
        return self.name