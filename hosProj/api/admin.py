from django.contrib import admin

from .models import Appointment,PatientAppointment,Speciality



admin.site.register(Speciality)
admin.site.register(Appointment)
admin.site.register(PatientAppointment)
