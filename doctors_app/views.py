from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from doctors_app.models import Doctor, ScheduleDoctor, ReviewDoctor, Specialization
from doctors_app.serializers import (
    DoctorSerializer,
    ScheduleDoctorSerializer,
    ReviewDoctorSerializer,
    SpecializationSerializer,
)

from rest_framework.exceptions import PermissionDenied




class DoctorViewSet(viewsets.ModelViewSet):
#API для работы с врачами: список, создание, детали, обновление, удаление
    queryset = Doctor.objects.all().select_related('specialization')
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'])
    def schedules(self, request, pk=None):
        #Получить расписание врача
        doctor = self.get_object()
        schedules = doctor.schedules.all()
        serializer = ScheduleDoctorSerializer(schedules, many=True)
        return Response(serializer.data)

class ScheduleDoctorViewSet(viewsets.ModelViewSet):
    #API для работы с расписанием врачей
    queryset = ScheduleDoctor.objects.all()
    serializer_class = ScheduleDoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ReviewDoctorViewSet(viewsets.ModelViewSet):
    queryset = ReviewDoctor.objects.all()
    serializer_class = ReviewDoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user = self.request.user
        doctor = serializer.validated_data['doctor']

        # Ограничим — можно оставить отзыв только 1 раз
        if ReviewDoctor.objects.filter(user=user, doctor=doctor).exists():
            raise PermissionDenied("Вы уже оставили отзыв этому врачу.")

        # Можно добавить: только если была запись к врачу
        if not user.appointments.filter(doctor=doctor, status='completed').exists():
            raise PermissionDenied("Вы можете оставить отзыв только после приёма у этого врача.")

        serializer.save(user=user)

class SpecializationViewSet(viewsets.ModelViewSet):
    #API для работы со специализациями врачей
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]