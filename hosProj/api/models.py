from django.db import models
from users.models import User


class Appointment(models.Model):
    title = models.CharField(max_length=50)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PatientAppointment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(
        Appointment, on_delete=models.SET_NULL, blank=True, null=True)
    date = models.DateField(auto_now=True, auto_now_add=True,)

    def __str__(self):
        return self.student.username


class Speciality(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



