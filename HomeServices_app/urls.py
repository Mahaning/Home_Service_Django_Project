from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from HomeServices_app import views
from HomeServices_project import settings
from django.contrib.auth.views import (
    # LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [


    path('', views.Login.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('user_registration/', views.User_Register.as_view(), name='user_registration'),
    path('Worker_Register/', views.Worker_Register.as_view(), name='Worker_Register'),
    path('index/', views.home.as_view(), name='index'),
    path('about/',views.about.as_view(),name='about'),
    path('services/',views.services.as_view(),name='services'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('bookservice/<int:id>',views.bookservice.as_view(),name='bookservice'),

    path('admmin_home/', views.admmin_home.as_view(), name='admmin_home'),
    path('workers_home/', views.workers_home.as_view(), name='workers_home'),



    path('manageworker/', views.manageworker.as_view(), name='manageworker'),
    path('manageusers/', views.manageusers.as_view(), name='manageusers'),
    path('verify_worker/<str:action>/<int:id>',views.verify_worker.as_view(),name='verify_worker'),

    path('AddCountry/', views.AddCountry.as_view(), name='AddCountry'),
    path('ManageCountry/', views.ManageCountry.as_view(), name='ManageCountry'),
    path('DeleteCountry/<int:id>',views.DeleteCountry.as_view(),name='DeleteCountry'),

    path('AddCity/', views.AddCity.as_view(), name='AddCity'),
    path('managecity/', views.managecity.as_view(), name='managecity'),
    path('DeleteCity/<int:id>',views.DeleteCity.as_view(),name='DeleteCity'),

    path('AddState/', views.AddState.as_view(), name='AddState'),
    path('ManageState/', views.ManageState.as_view(), name='ManageState'),
    path('DeleteState/<int:id>',views.DeleteState.as_view(),name='DeleteState'),


    path('AddServices/', views.AddServices.as_view(), name='AddServices'),
    path('ManageServices/', views.ManageServices.as_view(), name='ManageServices'),
    path('DeleteServices/<int:id>',views.DeleteServices.as_view(),name='DeleteServices'),
    path('EditServices/<int:id>',views.EditServices.as_view(),name='EditServices'),

    path('AssignWorker/<int:id>',views.AssignWorker.as_view(),name='AssignWorker'),
   

    path('feedback_form/', views.feedback_form.as_view(), name='feedback_form'),
    path('viewfeedbacks/', views.viewfeedbacks.as_view(), name='viewfeedbacks'),
    path('ViewRequests/', views.ViewRequests.as_view(), name='ViewRequests'),
    path('viewresponse/',views.viewresponse.as_view(),name='viewresponse'),

    
    path('Viewappointment_history/',views.Viewappointment_history.as_view(),name='Viewappointment_history'),
    path('CancelRequest/<int:id>',views.CancelRequest.as_view(),name='CancelRequest'),
    path('userprofile/',views.userprofile.as_view(),name='userprofile'),
    path('workerprofile/',views.workerprofile.as_view(),name='workerprofile'),
   



    path('ViewColleagues/', views.ViewColleagues.as_view(), name='ViewColleagues'),
    path('WorkerViewRequests/', views.WorkerViewRequests.as_view(), name='WorkerViewRequests'),
    path('viewworkerfeedbacks/', views.viewworkerfeedbacks.as_view(), name='viewworkerfeedbacks'),
    path('WorkerpendingTask/',views.workerviewresponse.as_view(),name='WorkerpendingTask'),

    path('acceptrequest/<str:action>/<int:id>',views.acceptrequest.as_view(),name='acceptrequest'),
    path('markcompleted/<str:action>/<int:id>',views.markcompleted.as_view(),name='markcompleted'),
    path('reject/<str:action>/<int:id>',views.reject.as_view(),name='reject'),
    

    # path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/',PasswordResetView.as_view(template_name='password_reset.html',html_email_template_name='password_reset_email.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)