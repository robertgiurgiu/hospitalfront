import email
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Docdepartments=[('Cardiologist','Cardiologist'),
    ('Emergency Doctor','Emergency Doctor'),
    ('Surgeon','Surgeon'),
    ('ICU Doctor','ICU Doctor'),
    ('Radiologist','Radiologist'),

]
Patdepartments=[('Cardiology','Cardiology'),
    ('Emergency ','Emergency '),
    ('Surgery','Surgery'),
    ('ICU','ICU '),
    ('Radiology','Radiology'),

]
class Patient(models.Model):
    GENDER = (
        ('M', 'M'),
        ('F', 'F'),
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    department= models.CharField(max_length=50,choices=Patdepartments,default='Cardiology')
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


class Doctor(models.Model):

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    department= models.CharField(max_length=50,choices=Docdepartments,default='Cardiologist')
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Appointment(models.Model):

    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    age = models.CharField(max_length=3)
    department= models.CharField(max_length=50,choices=Patdepartments,default='Cardiology')
    doctorName=models.CharField(max_length=40)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    appointdata =  models.CharField(max_length=8)
    approve=models.BooleanField(default=False)

    def __str__(self):
        return self.name