from django.contrib import admin

from hospital.views import departments
from .models import Doctor, Patient, Appointment
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'age' ,'gender','department', 'created_at']
    search_fields = ['name', 'phone', 'email', 'age', 'department']
    list_filter = ['gender', 'department',]
    list_per_page = 10


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email','department', 'created_at', 'status']
    search_fields = ['name', 'phone', 'email', 'department']
    list_filter = ['department']
    list_per_page = 10


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'age','department', 'doctorName' ,'created_at', 'appointdata' ,'approve']
    search_fields = ['name', 'phone', 'email', 'department', 'approve']
    list_filter = ['department', 'doctorName', 'approve']
    list_per_page = 10

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment , AppointmentAdmin)