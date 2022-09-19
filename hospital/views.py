from ast import If
from atexit import register
from cgitb import html
from dataclasses import fields
import email
import imp
from multiprocessing import context
from pyexpat import model
from unicodedata import name
from urllib import request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from hospital.forms import SignUpForm
from hospital.forms import DoctorSignUpForm
from django.contrib.auth.decorators import user_passes_test
from hospital.models import Doctor, Patient, Appointment
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def loginPage(request):
    page= 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR password incorect')

    context={'page': page}
    return render(request, 'login_register.html', context)



def registerPage(request): 
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = SignUpForm(request.POST) 
            if form.is_valid(): 
                username = form.cleaned_data.get('username') 
                password = form.cleaned_data.get('password1')
                form.save() 
                new_user = authenticate(username=username, password=password) 
            else:
                messages.error(request, 'User already exist')
                return redirect('/register')
            if new_user is not None:
                login(request, new_user) 
                return redirect('index') 
              
    else:
        return redirect('logout')

    form = SignUpForm()

    context = { 'form': form  }

            
    return render(request, 'login_register.html', context) 


'''Creare cont ddoctor da tot aia poti sterge
def register_doctorPage(request): 
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = DoctorSignUpForm(request.POST) 
            if form.is_valid(): 
                username = form.cleaned_data.get('username') 
                password = form.cleaned_data.get('password1')
                form.save() 
                new_user = authenticate(username=username, password=password) 
                if new_user is not None:
                    login(request, new_user) 
                    return redirect('index') 
    else:
        return redirect('logout')

    form = DoctorSignUpForm()

    context = { 'form': form  }

            
    return render(request, 'login_registerdoctor.html', context) 
'''


@cache_control(no_cache=True, must_revalidade=True, no_store=True)
def logoutUser(request):
    logout(request)
    return redirect('index')

#Send apply job form
def send_email(request):
    full_name=request.POST.get('full_name')
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')

    template = loader.get_template('apply_job.txt')
    context = {
        'full_name': full_name,
        'email': email,
        'subject': subject,
        'message': message,

        

    }
    message = template.render(context)
    email = EmailMultiAlternatives(
        "New Job Application", message,
        "New CV" + "-Good news!",
        ['contact.giurgiu@gamil.com']
    )
    email.content_subtype = 'html'
    if request.FILES:
        file = request.FILES['file']
        email.attach(file.name, file.read(), file.content_type)
    email.send()
    messages.success(request, '')
    return HttpResponseRedirect('applysent')


#send contact form
def index(request):
    if request.method == 'POST':
        contact_name=request.POST.get('contact_name')
        contact_email=request.POST.get('contact_email')
        contact_message=request.POST.get('contact_message')

        data = {
        'contact_name': contact_name,
        'contact_email': contact_email,
        'contact_message': contact_message,

        }
        contact_message= '''
            Name: {}

            New message: {}
            
            From: {}
        '''.format(data['contact_name'],data['contact_message'], data['contact_email'])
        send_mail(data['contact_name'], contact_message, contact_email, ['contact.giurgiu@gmail.com'])
        return HttpResponseRedirect('/contactsent')
    return render(request, 'index.html', {})


@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def doctorprofile(request):
  if request.user.is_staff:  
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q)  | Q(phone__icontains=q)  | Q(email__icontains=q)  | Q(age__icontains=q)  | Q(gender__icontains=q) | Q(department__icontains=q) | Q(note__icontains=q)   
        ).order_by('-created_at')

    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')
    paginator = Paginator(all_patient_list, 3)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)


    return render(request, 'doctorprofile.html', {'patients':all_patient})
        
    
@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def add_patient(request):
   if request.user.is_staff: 
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('department') and request.POST.get('note'):
            pateint = Patient()
            pateint.name = request.POST.get('name')
            pateint.phone = request.POST.get('phone')
            pateint.email = request.POST.get('email')
            pateint.age = request.POST.get('age')
            pateint.gender = request.POST.get('gender')
            pateint.department = request.POST.get('department')
            pateint.note = request.POST.get('note')
            pateint.save()
            messages.success(request, 'Patient added succesfully!')
            return HttpResponseRedirect('/doctorprofile')
    else:
            return render(request ,'addpatient.html')

  
#function acces the patient invidulay

@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def patient(request, patient_id):
   if request.user.is_staff: 
    patient = Patient.objects.get(id = patient_id)
    if patient != None:
        return render(request, 'editprofile.html', {'patient': patient})

#function to edit patient   

@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def edit_patient(request):
   if request.user.is_staff:
    if request.method == 'POST':
        patient = Patient.objects.get(id = request.POST.get('id'))
        if patient !=None:
            
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.department = request.POST.get('department')
            patient.note = request.POST.get('note')
            patient.save()
            
            return HttpResponseRedirect('/doctorprofile')
    else:
            return render(request ,'editprofile.html')




#function to delete patient   

@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def delete_patient(request, patient_id):
   if request.user.is_staff: 
    patient = Patient.objects.get(id = patient_id)
    patient.delete()
    messages.success(request, 'Patient removed succesfully!')
    return HttpResponseRedirect('/doctorprofile')



    


# book appoitment from patient
@cache_control(no_cache=True, must_revalidade=True, no_store=True)
@login_required(login_url='login')
def add_appointment(request): 
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('doctorName') and request.POST.get('department') and request.POST.get('note'):
            pateint = Appointment()
            pateint.name = request.POST.get('name')
            pateint.phone = request.POST.get('phone')
            pateint.email = request.POST.get('email')
            pateint.doctorName = request.POST.get('doctorName')
            pateint.department = request.POST.get('department')
            pateint.note = request.POST.get('note')
            pateint.save()
            messages.success(request, 'Appointment send succesfully!')
            return HttpResponseRedirect('/add_appointment')
    else:
            return render(request ,'bookappointemnt.html')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def patientprofile(request):
    if 'y' in request.GET:
        y = request.GET['y']
        all_doctor_list = Doctor.objects.filter(
            Q(name__icontains=y)  | Q(phone__icontains=y)  | Q(email__icontains=y) | Q(department__icontains=y) | Q(note__icontains=y)   
        ).order_by('-created_at')

    else:
        all_doctor_list = Doctor.objects.all().order_by('-created_at')
    paginator = Paginator(all_doctor_list, 3)
    page = request.GET.get('page')
    all_doctor = paginator.get_page(page)


    return render(request, 'patientprofile.html', {'doctors':all_doctor})



@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def approve_bookappointment(request):
   if request.user.is_staff:  
    if 'x' in request.GET:
        x = request.GET['x']
        all_appointment_list = Appointment.objects.filter(
            Q(name__icontains=x)  | Q(phone__icontains=x)  | Q(email__icontains=x) |  Q(age__icontains=x) | Q(department__icontains=x) |  Q(created_at__icontains=x) | Q(appointdata__icontains=x)  | Q(approve__icontains=x)  
        ).order_by('-created_at')

    else:
        all_appointment_list = Appointment.objects.all().order_by('-created_at')
    paginator = Paginator(all_appointment_list, 3)
    page = request.GET.get('page')
    all_appointment = paginator.get_page(page)


    return render(request, 'approve_bookappointment.html', {'appointments':all_appointment})



@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def doctor_approval(request, pk) :
   if request.user.is_staff:  
    appointment = Appointment.objects.get(id = pk)
    appointment.approve= True
    appointment.save()
    return HttpResponseRedirect('/approve_bookappointment')

@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def doctor_unapproval(request, pk) :
   if request.user.is_staff:  
    appointment = Appointment.objects.get(id = pk)
    appointment.approve= False
    appointment.save()
    return HttpResponseRedirect('/approve_bookappointment')

    


@cache_control(no_cache=True, must_revalidade=True, no_store=True)    
@login_required(login_url='login')
def appointmentdetails(request):
    if 'x' in request.GET:
        x = request.GET['x']
        all_appointment_list = Appointment.objects.filter(
                Q(department__icontains=x) |  Q(created_at__icontains=x) | Q(appointdata__icontains=x)  | Q(approve__icontains=x)  
        ).order_by('-created_at')

    else:
        all_appointment_list = Appointment.objects.all().order_by('-created_at')
    paginator = Paginator(all_appointment_list, 3)
    page = request.GET.get('page')
    all_appointment = paginator.get_page(page)


    return render(request, 'appointmentdetails.html', {'appointments':all_appointment})


#simple functiom
def about(request):
    return render(request, 'about.html')


def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')

def applyjob(request):
    return render(request, 'applyjob.html' )


def login_register(request):
    return render(request, 'login_register.html')
        
    
def applysent(request):
    return render(request, 'applysent.html')

def main(request):
    return render(request, 'main.html')

    
def  contactsent(request):
    return render(request, 'contactsent.html')
 

