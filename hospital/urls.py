from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"), 
    path('logout/', views.logoutUser, name="logout"), 
    path('register/', views.registerPage, name="register"), 
    #path('registerdocotor/', views.register_doctorPage, name="registerdoctor"),
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('departments/', views.departments, name="departments"),
    path('doctors/', views.doctors, name="doctors"),
    path('applyjob/', views.applyjob, name="applyjob"),
    path('send_email', views.send_email, name="send_email"),
    path('applysent/', views.applysent, name="applysent"),
    path('main/', views.main, name="main"),
    path('doctorprofile/', views.doctorprofile, name="doctorprofile"),
    path('add_patient', views.add_patient, name="add_patient"),
    
    path('patientprofile/', views.patientprofile, name="patientprofile"),
    path('patient/<str:patient_id>', views.patient, name="patient"),
    path('edit_patient', views.edit_patient, name="edit_patient"),
    path('delete_patient/<str:patient_id>', views.delete_patient, name="delete_patient"),
    path('add_appointment', views.add_appointment, name="add_appointment"),
    path('approve_bookappointment/', views.approve_bookappointment, name="approve_bookappointment"),
    path('doctor_approval/<int:pk>', views.doctor_approval, name="doctor_approval"),
    path('doctor_unapproval/<int:pk>', views.doctor_unapproval, name="doctor_unapproval"),
    path('appointmentdetails/', views.appointmentdetails, name="appointmentdetails"),
    
    path('contactsent/', views.contactsent,name="contactsent"),
   
    
    
 
  
   
]
