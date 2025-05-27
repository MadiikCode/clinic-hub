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
    #API для работы с отзывами о врач
    queryset = ReviewDoctor.objects.all()
    serializer_class = ReviewDoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        #Автоматически привязывает отзыв к текущему пользователю
        serializer.save(user=self.request.user)

class SpecializationViewSet(viewsets.ModelViewSet):
    #API для работы со специализациями врачей
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]