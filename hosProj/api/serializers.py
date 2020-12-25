from rest_framework import serializers

from users.models import User
from .models import Appointment, Speciality, PatientAppointment


class AppointmentSerializer(serializers.ModelSerializer):
    appointment = serializers.SerializerMethodField()
    doctor = StringSerializer(many=False)

    class Meta:
        model = Assignment
        fields = ('__all__')

    def get_appointment(self, obj):
        appointment = AppointmentSerializer(obj.appointment.all(), many=True).data
        return appointment

    def create(self, request):
        data = request.data

        appointment = Appointment()
        doctor = User.objects.get(username=data['teacher'])
        appointment.doctor = doctor
        appointment.title = data['title']
        appointment.save()

        order = 1
        for q in data['questions']:
            newQ = Question()
            newQ.question = q['title']
            newQ.order = order
            newQ.save()

            for c in q['choices']:
                newC = Choice()
                newC.title = c
                newC.save()
                newQ.choices.add(newC)

            newQ.answer = Choice.objects.get(title=q['answer'])
            newQ.assignment = assignment
            newQ.save()
            order += 1
        return assignment


class GradedAssignmentSerializer(serializers.ModelSerializer):
    student = StringSerializer(many=False)

    class Meta:
        model = GradedAssignment
        fields = ('__all__')

    def create(self, request):
        data = request.data
        print(data)

        appointment = Appointment.objects.get(id=data['appId'])
        patient = User.objects.get(username=data['username'])

        patient_app = PatientAssignment()
        patient_app.appointment = appointment
        patient_app.patient = patient

       
        patient_app.save()
        return patient_app
