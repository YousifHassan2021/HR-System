from django.db import models
# from django.contrib.auth.models import User 
from django.utils.translation import gettext_lazy as _
from django.utils import timezone 
from settings import models as st_model
from managers.models import Project
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from month.models import MonthField


class User(AbstractUser):
    is_hr = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)




SOCIAL_STATUS = (
    ('Single','Single' ),
    ('Married','Married' ),
    ('Divorced','Divorced')
)

GENDER_TYPE = (
    ('Male','Male' ) , 
    ( 'Femal','Femal')
)


RELIGION_TYPE = (
    ('MUSLIM','MUSLIM'),
    ('CHRISTIEN','CHRISTIEN'),
    ('OTHER','OTHER')
) 


USER_ROLE=(
    ('Employee' , 'Employee'),
    ('Manager' , 'Manager'),
    ('HR' , 'HR')
)

class UserProfile(models.Model):
    company  = models.ForeignKey(st_model.Company, related_name='company_user', on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_profile',verbose_name=_('user'), on_delete=models.CASCADE)
    ar_name = models.CharField(_('arabic name'),max_length=100)
    en_name = models.CharField(_('english name'),max_length=100)
    job_number = models.IntegerField(_("Job Number") , null=True , blank=True)
    social_status = models.CharField(_("Social Status"), max_length=10 , null=True , blank=True, choices=SOCIAL_STATUS)
    id_number = models.CharField(_('Id Number'),max_length=25 , blank=True, null=True)
    id_create_date = models.DateField(_("Id Create Date"),default=timezone.now)
    id_end_date = models.DateField(_("Id End Date"),default=timezone.now)
    id_issue_location = models.CharField(_("Id Issue Location"), max_length=100 , default='')    
    gender = models.CharField(max_length=10 , choices=GENDER_TYPE,verbose_name=_("Gender") , default='Male')
    visa_number = models.IntegerField(_("Visa Number"),blank=True, null=True)
    birth_date = models.DateField(_("Birth Date"),default=timezone.now )
    birth_location = models.CharField(_('Birth Location'),max_length=100, default='')
    passport_number = models.CharField(_("Passport Number"), max_length=15, default='')
    passport_issue_date =  models.DateField(_("Passport Issue Date"),default=timezone.now ) 
    passport_end_date = models.DateField(_("Passport End Date"),default=timezone.now ) 
    borders_number = models.IntegerField(_("Borders Number") ,  null=True , blank=True)
    job = models.CharField(_("Job as In Id"), max_length=100, default='')
    religion = models.CharField(_("Religion"), max_length=50 , choices=RELIGION_TYPE , default='MUSLIM')
    nationality = models.CharField(_('Nationality'),max_length=50 ,default='')
    id_card_date = models.DateField(_("Id Card Date"),default=timezone.now)  
    # user_role = models.CharField(_("User Role"), max_length=10 , choices=USER_ROLE , default='M')  
    image = models.ImageField(_("Image"), upload_to='attachements_img/' ,blank=True, null=True )
    file = models.FileField(_("File"), upload_to='attachements_files/', blank=True, null=True)
    first_login = models.BooleanField(_("First Login") , default=True)
    join_date =  models.DateField(_("Join Date"),default=timezone.now , blank=True, null=True)

    def __str__(self):
        return self.user.username


class UserNotes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_notes',verbose_name=_('user'), on_delete=models.CASCADE)
    note = models.TextField(_("Note"))
    def __str__(self):
        return self.user.username




class UserContact(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_contact',verbose_name=_('user'), on_delete=models.CASCADE)
    land_line = models.CharField(_("Land Line"),max_length=20 , default='')
    mobile_number = models.CharField(_("Mobile Number"),max_length=20, default='')
    postal_box = models.CharField(_("P.O.Box"),max_length=150, default='')
    email = models.EmailField(_("Email"), max_length=254, default='')
    home_phone_number = models.CharField(_("Home Number"),max_length=20, default='')
    mother_address = models.CharField(_("Mother Address"),max_length=100, default='')
    mother_phone_number =  models.CharField(_("Mother Home Number"),max_length=20, default='')
    guarantor = models.CharField(_("Guarantor"),max_length=100, default='')
    postal_code = models.IntegerField(_("Postal Code"),blank=True, null=True)
    Address = models.CharField(_('Address'),max_length=200, default='')
    passport_img = models.ImageField(_("Passport Image"), upload_to='user_img', default='')
    contract_img = models.ImageField(_("Contract Image"), upload_to='user_contract', default='')
    residence_img = models.ImageField(_("Residence Image"), upload_to='user_residence', default='')



class UserJob(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='user_job',verbose_name=_('user'), on_delete=models.CASCADE)
    branch = models.ForeignKey(st_model.Branch, related_name='user_branch',verbose_name=_("Branch"), on_delete=models.CASCADE,blank=True, null=True)
    job_type = models.ForeignKey(st_model.JobType, related_name='user_job_type',verbose_name=_("Job Type"), on_delete=models.CASCADE,blank=True, null=True)
    job_grade = models.ForeignKey(st_model.JobGrade, related_name='job_grade',verbose_name=_("Job Grade"), on_delete=models.CASCADE,blank=True, null=True)
    job_title = models.CharField(_("Job Title"),max_length=100, default='')
    employee_status = models.ForeignKey(st_model.EmployeeStatus, related_name='employee_status',verbose_name=_("Employee Status"), on_delete=models.CASCADE,blank=True, null=True)
    qualification = models.ForeignKey(st_model.Qualifications, related_name='qualifications',verbose_name=_("user qualifications"), on_delete=models.CASCADE,blank=True, null=True)
    spciality = models.CharField(_('Speciality'),max_length=100, default='')
    hiring_date = models.DateField(_("Hiring Date"),default=timezone.now )
    department_section = models.ForeignKey(st_model.Department_Section, related_name='user_department_section',verbose_name=_("Department or Section"), on_delete=models.CASCADE,blank=True, null=True)
    project_or_site = models.ForeignKey(Project, related_name='user_project',verbose_name=_("user project"), on_delete=models.CASCADE,blank=True, null=True)
    experience_years = models.IntegerField(_("Years Of Experience"),blank=True, null=True)
    direct_manager = models.ForeignKey(User ,verbose_name=_("Direct Manager"), related_name='user_manager' , on_delete=models.CASCADE,blank=True, null=True) 
    department_manager = models.ForeignKey(User ,verbose_name=_("Department Manager"), related_name='department_manager' , on_delete=models.CASCADE,blank=True, null=True) 




class UserSalary(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_salary',verbose_name=_('user'), on_delete=models.CASCADE)
    salary_type = models.ForeignKey(st_model.SalaryType, related_name='user_salary_type',verbose_name=_('salary type'), on_delete=models.CASCADE , blank=True, null=True)
    main_salary = models.FloatField(_("Main Salary"), default=0)
    fast_transfer = models.BooleanField(_("Fast Transfer") , default=False)
    stop_salary = models.BooleanField(_("Stap Salary") , default=False)
    stop_reason = models.TextField(_("Stop Reason"), max_length=50 , default='')
    stop_date = models.DateField(default=timezone.now , null=True , blank=True,verbose_name=_("Stop Date"))
    bank_name = models.ForeignKey(st_model.BankName, verbose_name=_("bank name"), on_delete=models.CASCADE , blank=True, null=True)
    bank_account_number = models.IntegerField(_("bank account number"), default=0)
    bank_account_iban = models.CharField(max_length=25, default='',verbose_name=_("Bank Account"))
    daily_working_hours = models.FloatField(_("Daily Working Hours"), default=0)
    yearly_vacation_days_count = models.IntegerField(_("Yearly Vacations Days"), default=0)
    attend_execlude = models.BooleanField(_("Attend Execlude") , default=False)
    has_loan = models.BooleanField(_("Loan") ,default=False)
    attendence_type = models.ForeignKey(st_model.AttendenceType, related_name='user_attendence_type',verbose_name=_("Attendence Type"), on_delete=models.CASCADE, blank=True, null=True)
    salary_pay_type = models.ForeignKey(st_model.SalaryPayType, related_name='user_salary_pay_type',verbose_name=_('Salary Pay Type'), on_delete=models.CASCADE , blank=True, null=True)
    salary_protection = models.BooleanField(_("Salary Protection"),default=False)
    net_salary = models.FloatField(_("Net Salary") , default=0)


REPLACEMENT_TYPE = (
    ('Addition' , 'Addition'),
    ('Deduction' , 'Deduction')
)


class UserReplacements(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_replacements',verbose_name=_('user'), on_delete=models.CASCADE)
    replacement_type = models.ForeignKey(st_model.ReplacementType, related_name='user_replacement_type',verbose_name=_('repacement type'), on_delete=models.CASCADE)
    percentage = models.IntegerField(_("Percentage") , blank=True, null=True)
    money = models.FloatField(_("Money") , blank=True, null=True)
    category = models.CharField(max_length=12 , choices=REPLACEMENT_TYPE,verbose_name=_("Category"))
    replacement_for = models.ForeignKey(st_model.ReplacementPeriod,verbose_name=_("Replacement For"), related_name='uer_replacement_period', on_delete=models.CASCADE)
    notes = models.TextField(_("Notes") , blank=True, null=True)
    month = MonthField(blank=True, null=True)

    ## override save to calculate the money

# class UserDiscounts(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_discounts',verbose_name=_('user'), on_delete=models.CASCADE)
#     discount_type = models.ForeignKey(st_model.DiscountType, related_name='user_discount_type',verbose_name=_('repacement type'), on_delete=models.CASCADE)
#     percentage = models.IntegerField(_("Percentage") , blank=True, null=True)
#     money = models.FloatField(_("Money") , blank=True, null=True)
#     category = models.CharField(max_length=12 , choices=REPLACEMENT_TYPE,verbose_name=_("Category"))
#     notes = models.TextField(_("Notes") , blank=True, null=True)

    ## override save to calculate the money



class UserAccountsConnection(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_connections',verbose_name=_('user'), on_delete=models.CASCADE)
    total_salary = models.FloatField(_("Total Salary"))
    company = models.ForeignKey(st_model.Company, related_name='user_company',verbose_name=_('Company'), on_delete=models.CASCADE)
    loan_account = models.FloatField(_("Loan Account") , blank=True, null=True)
    cost_center = models.FloatField(_("Cost Center"))


class UserContract(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_contract',verbose_name=_('user'), on_delete=models.CASCADE)
    contract_start_date = models.DateField(_("Contract Start Date"),default=timezone.now )
    contract_end_date = models.DateField(_("Contract End Date"),default=timezone.now )
    notes = models.TextField(_("Notes") , max_length=10000)


class UserSocialInsurance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_social_insurance',verbose_name=_('user'), on_delete=models.CASCADE)
    social_insurance_id = models.IntegerField(_("Social Insurance Id"), blank=True, null=True)
    join_date = models.DateField(_("Join Date"), default=timezone.now)
    basic_salary = models.FloatField(_("Basic Salary"), default=0)
    housing_replacement = models.FloatField(_("Housing Replacement"), default=0)
    comissions_replacement = models.FloatField(_("Comission Replacement"), default=0)
    other_replacements = models.FloatField(_("Other Replacements"), default=0)
    salary_under_social_insurance = models.FloatField(_("Salary Under Social Insurance"), default=0)
    employee_last_day = models.DateField(_("Employee Last Day"), default=timezone.now)
    labrorary_office_number = models.IntegerField(_("Labrorary Office Number"), default=0)


class UserMedicalInsurance(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_medical_attachments',verbose_name=_('user'), on_delete=models.CASCADE)
    insurance_class = models.ForeignKey(st_model.InsuranceClass, related_name='user_insurance_class',verbose_name=_('Insurance Class'), on_delete=models.CASCADE , blank=True, null=True) 
    insurance_company = models.ForeignKey(st_model.InsuranceCompany, related_name='user_insurance_company',verbose_name=_('Insurance Company'), on_delete=models.CASCADE , blank=True, null=True)
    insurance_valid_date = models.DateField(_("Insurance Valid Date"),default=timezone.now)
    insurance_number = models.IntegerField(_("Insurance Number"),default=0)


class UserTravel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_travel',verbose_name=_('user'), on_delete=models.CASCADE)
    deserve_ticket = models.BooleanField(_("Deserve Ticket"),default=False)
    ticket_type = models.ForeignKey(st_model.TicketType, related_name='user_ticket_type',verbose_name=_('Ticket Type'), on_delete=models.CASCADE)
    ticket_count = models.IntegerField(_("Ticket Count"))
    ticket_value = models.FloatField(_("Ticket Value"))
    city = models.ForeignKey(st_model.City, related_name='user_travel_city',verbose_name=_('City'), on_delete=models.CASCADE)


class UserFollowers(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_followers',verbose_name=_('user'), on_delete=models.CASCADE)
    name = models.CharField(_('name'),max_length=100)
    birth_date = models.DateField(_("Birth Date"),default=timezone.now )
    deserve_ticket = models.BooleanField(_("Deserve Ticket") , default=False)
    deserve_isurance = models.BooleanField(_("Deserve Insurance") , default=False)
    insurance_id_number = models.IntegerField(_("Insurance Id Number"))
    nationality = models.CharField(_('Nationality'),max_length=50)
    social_status = models.CharField(_("Social Status"), max_length=10 , null=True , blank=True, choices=SOCIAL_STATUS)
    gender = models.CharField(max_length=7 , choices=GENDER_TYPE,verbose_name=_("Gender"))
    id_number = models.CharField(_('Id Number'),max_length=25)
    follower_type = models.ForeignKey(st_model.FollowerType, related_name='Follower_Type', on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


class UserVacationRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_vacation_requests',verbose_name=_('user'), on_delete=models.CASCADE)
    request_id = models.IntegerField(_("Request Id") , blank=True, null=True)
    request_date = models.DateField(_("Request Date"), auto_now_add=True)
    vacation_balance = models.IntegerField(_("Vacation Balance"))
    vacation_type = models.ForeignKey(st_model.VacationType, verbose_name=_("vacation type"),related_name='user_vacation_type', on_delete=models.CASCADE)
    start_date = models.DateField(_("Start Date "), default=timezone.now) 
    end_date = models.DateField(_("End Date "), default=timezone.now) 
    last_vacation_date = models.DateField(_("End Date "), default=timezone.now , blank=True, null=True)
    vacation_days_count = models.IntegerField(_("Vacation Days Count"), blank=True, null=True)
    paid_days_count = models.IntegerField(_("Paid Days Count"),blank=True, null=True)
    no_paid_days_count =  models.IntegerField(_("Not Paid Days Count"),blank=True, null=True)
    vacation_salary_first = models.BooleanField(_("Vacation Salary First"),default=False)
    exit_visa = models.BooleanField(_("Exit Visa") , default=False)
    address = models.CharField(max_length=200 , blank=True, null=True,verbose_name=_("Address"))
    contact_number = models.CharField(max_length=18 , blank=True, null=True,verbose_name=_("Contact Number"))
    replacement_employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='replacement_employee', verbose_name=_("replacement employee"), on_delete=models.CASCADE)
    attachement = models.FileField(_("Attachement"), upload_to='request_files/')


    # request id auto add



class PermissionRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_permission_requests',verbose_name=_('user'), on_delete=models.CASCADE)
    request_id = models.IntegerField(_("Request Id") , blank=True, null=True)
    request_date = models.DateField(_("Request Date"), auto_now_add=True)  
    leave_reasons = models.ForeignKey(st_model.LeaveReasons,verbose_name=_("Leave Reasons"), related_name='user_leave_resons', on_delete=models.CASCADE)
    leaving_reasons = models.TextField(_("Leaving Reasons") , blank=True, null=True)
    leaving_time = models.TimeField(_("Leaving Time"), default=timezone.now)
    expected_return_time = models.TimeField(_("Leaving Time"), default=timezone.now)
    contact_number = models.CharField(max_length=18 , blank=True, null=True,verbose_name=_("Contact Number"))


    # request id auto add     



class LoanRequest(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_loan_requests',verbose_name=_('user'), on_delete=models.CASCADE)
    request_id = models.IntegerField(_("Request Id") , blank=True, null=True)
    request_date = models.DateField(_("Request Date"), auto_now_add=True)     
    needed_money = models.FloatField(_("Needed Money"))
    installment_start_date = models.DateField(_("Installment Start Date"), default=timezone.now)
    installment_count = models.IntegerField(_("Installment Count"))
    installment_value = models.FloatField(_("Installment Value"))
    loan_type = models.ForeignKey(st_model.LoanType, verbose_name=_("Loan Type"),related_name='user_loan_type', on_delete=models.CASCADE)  

    # request id auto add    


class UserDefinationLetter(models.Model):
    pass
    ## export with user name 


class UserResign(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_resign_requests',verbose_name=_('user'), on_delete=models.CASCADE)
    reason  = models.ForeignKey(st_model.ReasonToResign, related_name='user_resign_reason', on_delete=models.CASCADE)
    termination_date = models.DateField(_("End Date"), default=timezone.now)
    notice_date = models.DateField(_("Notice Date"), default=timezone.now)



class UserTermination(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_termination',verbose_name=_('user'), on_delete=models.CASCADE)
    termination_type  = models.ForeignKey(st_model.ReasonToTerminate,verbose_name=_("Termination Type"), related_name='user_terminate_reason', on_delete=models.CASCADE)
    termination_date = models.DateField(_("End Date"), default=timezone.now)
    reason = models.TextField(_("reason") , default='')
    notice_date = models.DateField(_("Notice Date"), default=timezone.now)



class UserPromotion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_promotion_requests',verbose_name=_('user'), on_delete=models.CASCADE)
    from_type  = models.ForeignKey(st_model.JobType, related_name='from_type', on_delete=models.CASCADE)
    from_grade = models.ForeignKey(st_model.JobGrade, related_name='from_grade', on_delete=models.CASCADE)  
    to_type = models.ForeignKey(st_model.JobType, related_name='to_type', on_delete=models.CASCADE)
    to_grade = models.ForeignKey(st_model.JobGrade, related_name='to_grade', on_delete=models.CASCADE)  
    date = models.DateField(_("Promotion Date"), default=timezone.now)

    def __str__(self):
        return str(self.user)



class UserAssets(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_rassets_equests',verbose_name=_('user'), on_delete=models.CASCADE)
    asset = models.ForeignKey(st_model.Assets, related_name='user_asset', on_delete=models.CASCADE)
    notes = models.TextField(_("Notes"))
    status = models.ForeignKey(st_model.AssetStatus,verbose_name=_("Status"), related_name='user_asset_status', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.asset)



TRAINING_STATUS = (
    ('ACTIVE' , 'ACTIVE'),
    ('IN ACTIVE' , 'IN ACTIVE')    
)

class UserTraining(models.Model):
    course = models.ForeignKey(st_model.TrainingCourse,verbose_name=_("Course"), related_name='training_course', on_delete=models.CASCADE)   
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("Trainer"), related_name='course_reainer', on_delete=models.CASCADE)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='training_employee',verbose_name=_("Employees"),blank=True, null=True)
    start_date = models.DateField(_("Start Date"), default=timezone.now)
    end_date = models.DateField(_("End Date"), default=timezone.now)
    cost = models.FloatField(_("Cost"))
    notes = models.TextField(_("Notes"))
    status =models.CharField(_("status"), max_length=15 , choices = TRAINING_STATUS)


    def __str__(self):
        return str(self.course)



overtime_status = (
    ('Pending' , 'Pending') , 
    ('Approved' , 'Approved'),
    ('Rejected' , 'Rejected')
)

class UserOverTime(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_overtime_requests',verbose_name=_('user'), on_delete=models.CASCADE)
    overhours = models.FloatField(_("Over Hourse "))
    total_over_time_hours = models.FloatField(_("Total Overtime Hours") , blank=True, null=True)
    date = models.DateField(_("Date"), default=timezone.now)
    description = models.TextField(_("Description"))
    status = models.CharField(max_length=15 , choices=overtime_status , default='Pending')
    hour_equal = models.FloatField(blank=True, null=True,verbose_name=_("Hour Equal"))
    month = MonthField(blank=True, null=True)
    
    class Meta:
        ordering = ['-date']

    ## multiply the overtime from setings and save it in total overtime 
    # save hour_equal



CUSTOMER_EXPERIENCE = (
    ('N' , 'NONE'),
    ('B' , 'BEIGINNER') , 
    ('I' , 'Intermediate'),
    ('A' , 'Advanced'),
    ('E' , 'Expert')
)



class UserEvaluation(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='employee_evaluation', on_delete=models.CASCADE)
    date = models.DateField(_("Date"), default=timezone.now)
    customer_experience = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Customer experience"))
    marketing = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Marketing"))
    management = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Management"))
    administration = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Adminstration"))
    presentation_skill = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Presentation SKill"))
    quality_of_work = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Quality Of WOrk"))
    efficiency = models.CharField(max_length=2 , choices=CUSTOMER_EXPERIENCE,verbose_name=_("Efficiency"))
    status = models.CharField(max_length=15 , choices=TRAINING_STATUS,verbose_name=_("Status"))



class UserPerformanceIndicator(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("Employee"), related_name='employee_performance_indicator', on_delete=models.CASCADE)
    key_result_area  = models.CharField(max_length=150,verbose_name=_("Key Result Area"))
    key_performance_indicator  = models.CharField(max_length=150,verbose_name=_("Key Performance Indicator"))
    weightage = models.FloatField(_("Weightage"))
    percentage_achieved = models.FloatField(_("Percentage achieved"))
    date = models.DateField(_("date"), default=timezone.now)


class UserAttendance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_("User"), related_name='user_attendance', on_delete=models.CASCADE)
    time_in = models.DateTimeField(_("Date & Time In"),auto_now_add=False)
    time_out = models.DateTimeField(_("Date & Time Out"),auto_now_add=False)

    def __str__(self):
        return str(self.user)







# # ## create new user singla 
@receiver(post_save , sender=User)
def create_user_profile(sender,instance,created , **kwargs):
    if created:
        # UserProfile.objects.create(user = instance)
        UserContact.objects.create(user=instance)
        UserJob.objects.create(user=instance)
        UserSalary.objects.create(user=instance)
        UserMedicalInsurance.objects.create(user=instance)
        UserSocialInsurance.objects.create(user=instance)
        