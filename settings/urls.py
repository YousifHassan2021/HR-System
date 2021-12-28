from django.urls import path
from . import views

app_name = 'settings'


urlpatterns = [
    path('asset-condition' , views.AssetConditionListCreateView.as_view(),name='asset-condition-list-create'),
    path('asset-condition/<int:id>/delete' , views.asset_Condition_delete,name='asset-condition-delete'),

    path('asset-status' , views.AssetStatusListCreateView.as_view(),name='asset-status-List-Create'),
    path('asset-status/<int:id>/delete' , views.asset_status_delete,name='asset-status-delete'),

    path('attendance-types' , views.AttendanceTypesListCreateView.as_view(),name='attendance-types-List-Create'),
    path('attendance-types/<int:id>/delete' , views.attendance_types_delete,name='attendance-types-delete'),

    path('bank-names' , views.BankNamesListCreateView.as_view(),name='bank-names-List-Create'),
    path('bank-names/<int:id>/delete' , views.bank_names_delete,name='bank-names-delete'),

    path('branch' , views.BranchesListCreateView.as_view(),name='branch-List-Create'),
    path('branch/<int:id>/delete' , views.branch_delete,name='branch-delete'),

    path('city' , views.CityListCreateView.as_view(),name='city-List-Create'),
    path('city/<int:id>/delete' , views.city_delete,name='city-delete'),

    path('discount-types' , views.DiscountTypesListCreateView.as_view(),name='discount-types-List-Create'),
    path('discount-types/<int:id>/delete' , views.discount_types_delete,name='discount-types-delete'),

    path('employee-status' , views.EmployeeStatusListCreateView.as_view(),name='employee-status-List-Create'),
    path('employee-status/<int:id>/delete' , views.employee_status_delete,name='employee-status-delete'),

    path('follower-types' , views.FollowerTypesListCreateView.as_view(),name='follower-types-List-Create'),
    path('follower-types/<int:id>/delete' , views.follower_type_delete,name='follower-types-delete'),

    path('insurance-class' , views.InsuranceClassListCreateView.as_view(),name='insurance-class-List-Create'),
    path('insurance-class/<int:id>/delete' , views.insurance_class_delete,name='insurance-class-delete'),

    path('insurance-company' , views.InsuranceCompanyListCreateView.as_view(),name='insurance-company-List-Create'),
    path('insurance-company/<int:id>/delete' , views.insurance_company_delete,name='insurance-company-delete'),

    path('job-grade' , views.JobGradeListCreateView.as_view(),name='job-grade-List-Create'),
    path('job-grade/<int:id>/delete' , views.job_grade_delete,name='job-grade-delete'),

    path('project-periority' , views.ProjectPeriorityListCreateView.as_view(),name='project-periority-List-Create'),
    path('project-periority/<int:id>/delete' , views.project_periority_delete,name='project-periority-delete'),

    path('project-status' , views.ProjectStatusListCreateView.as_view(),name='project-status-List-Create'),
    path('project-status/<int:id>/delete' , views.project_status_delete,name='project-status-delete'),

    path('qualifications' , views.QualificationListCreateView.as_view(),name='qualifications-List-Create'),
    path('qualifications/<int:id>/delete' , views.qualifications_delete,name='qualifications-delete'),

    path('reason-to-terminate' , views.ReasonToTerminateListCreateView.as_view(),name='reason-to-terminate-List-Create'),
    path('reason-to-terminate/<int:id>/delete' , views.reason_to_terminate_delete,name='reason-to-terminate-delete'),


    path('replacement-period' , views.ReplacementPeriodListCreateView.as_view(),name='replacement-period-List-Create'),
    path('replacement-period/<int:id>/delete' , views.replacement_period_delete,name='replacement-period-delete'),

    path('replacement-type' , views.ReplacementTypeListCreateView.as_view(),name='replacement-type-List-Create'),
    path('replacement-type/<int:id>/delete' , views.replacement_type_delete,name='replacement-type-delete'),

    path('salary-pay-types' , views.SalaryPayTypesListCreateView.as_view(),name='salary-pay-types-List-Create'),
    path('salary-pay-types/<int:id>/delete' , views.salary_pay_types_delete,name='salary-pay-types-delete'),

    path('salary-type' , views.SalaryTypeListCreateView.as_view(),name='salary-type-List-Create'),
    path('salary-type/<int:id>/delete' , views.salary_type_delete,name='salary-type-delete'),

    path('ticket-type' , views.TcketTypeListCreateView.as_view(),name='ticket-type-List-Create'),
    path('ticket-type/<int:id>/delete' , views.ticket_type_delete,name='ticket-type-delete'),

]