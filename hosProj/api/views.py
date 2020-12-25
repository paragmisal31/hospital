from rest_framework import viewsets
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST
)

from .models import Appointment, PatientAppointment
from .serializers import AppointmentSerializer, PatientAppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

    def create(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            appointment = serializer.create(request)
            if appointment:
                return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class GradedAssignmentListView(ListAPIView):
    serializer_class = GradedAssignmentSerializer

    def get_queryset(self):
        queryset = PatientAppointment.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(student__username=username)
        return queryset


class PatientAppointmentCreateView(CreateAPIView):
    serializer_class = PatientAppointmentSerializer
    queryset = PatientAppointment.objects.all()

    def post(self, request):
        print(request.data)
        serializer = PatientAppointmentSerializer(data=request.data)
        serializer.is_valid()
        PatientAppointment = serializer.create(request)
        if PatientAppointment:
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
