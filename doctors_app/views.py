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

from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample, OpenApiParameter


@extend_schema_view(
    list=extend_schema(
        summary='Получение списка врачей',
        description='Возвращает список всех врачей с их специализациями.',
        responses={200: DoctorSerializer}
    ),
    retrieve=extend_schema(
        summary='Получение информации о враче',
        description='Возвращает подробную информацию о выбранном враче.',
        responses={200: DoctorSerializer, 404: OpenApiExample('Врач не найден', {'error': 'Врач с данным ID не найден'})}
    ),
    create=extend_schema(
        summary='Создание врача',
        description='Позволяет создать нового врача.',
        responses={201: DoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    update=extend_schema(
        summary='Обновление информации о враче',
        description='Полное обновление данных врача.',
        responses={200: DoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    partial_update=extend_schema(
        summary='Частичное обновление информации о враче',
        description='Позволяет обновить отдельные поля врача.',
        responses={200: DoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    destroy=extend_schema(
        summary='Удаление врача',
        description='Удаляет врача из системы.',
        responses={204: None, 404: OpenApiExample('Врач не найден', {'error': 'Врач с данным ID не найден'})}
    ),
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

# ScheduleDoctorViewSet
@extend_schema_view(
    list=extend_schema(
        summary='Получение расписания всех врачей',
        description='Возвращает список всех расписаний врачей.',
        responses={200: ScheduleDoctorSerializer}
    ),
    retrieve=extend_schema(
        summary='Получение расписания врача',
        description='Возвращает подробное расписание выбранного врача.',
        responses={200: ScheduleDoctorSerializer, 404: OpenApiExample('Расписание не найдено', {'error': 'Расписание с данным ID не найдено'})}
    ),
    create=extend_schema(
        summary='Создание расписания врача',
        description='Позволяет создать расписание для врача.',
        responses={201: ScheduleDoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    update=extend_schema(
        summary='Обновление расписания врача',
        description='Полное обновление расписания врача.',
        responses={200: ScheduleDoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    partial_update=extend_schema(
        summary='Частичное обновление расписания врача',
        description='Позволяет обновить отдельные поля расписания.',
        responses={200: ScheduleDoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    destroy=extend_schema(
        summary='Удаление расписания врача',
        description='Удаляет расписание врача из системы.',
        responses={204: None, 404: OpenApiExample('Расписание не найдено', {'error': 'Расписание с данным ID не найдено'})}
    ),
)

class ScheduleDoctorViewSet(viewsets.ModelViewSet):
    #API для работы с расписанием врачей
    queryset = ScheduleDoctor.objects.all()
    serializer_class = ScheduleDoctorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ReviewDoctorViewSet
@extend_schema_view(
    list=extend_schema(
        summary='Получение списка отзывов о врачах',
        description='Возвращает список всех отзывов о врачах.',
        responses={200: ReviewDoctorSerializer}
    ),
    retrieve=extend_schema(
        summary='Получение отзыва о враче',
        description='Возвращает подробный отзыв о выбранном враче.',
        responses={200: ReviewDoctorSerializer, 404: OpenApiExample('Отзыв не найден', {'error': 'Отзыв с данным ID не найден'})}
    ),
    create=extend_schema(
        summary='Создание отзыва о враче',
        description='Позволяет пользователю оставить отзыв о враче (один отзыв на врача, только после приема).',
        responses={201: ReviewDoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    update=extend_schema(
        summary='Обновление отзыва о враче',
        description='Полное обновление отзыва о враче.',
        responses={200: ReviewDoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    partial_update=extend_schema(
        summary='Частичное обновление отзыва о враче',
        description='Позволяет обновить отдельные поля отзыва о враче.',
        responses={200: ReviewDoctorSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    destroy=extend_schema(
        summary='Удаление отзыва о враче',
        description='Удаляет отзыв о враче.',
        responses={204: None, 404: OpenApiExample('Отзыв не найден', {'error': 'Отзыв с данным ID не найден'})}
    ),
)

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



# SpecializationViewSet
@extend_schema_view(
    list=extend_schema(
        summary='Получение списка специализаций',
        description='Возвращает список всех специализаций врачей.',
        responses={200: SpecializationSerializer}
    ),
    retrieve=extend_schema(
        summary='Получение специализации',
        description='Возвращает подробную информацию о выбранной специализации.',
        responses={200: SpecializationSerializer, 404: OpenApiExample('Специализация не найдена', {'error': 'Специализация с данным ID не найдена'})}
    ),
    create=extend_schema(
        summary='Создание специализации',
        description='Позволяет создать новую специализацию врача.',
        responses={201: SpecializationSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    update=extend_schema(
        summary='Обновление специализации',
        description='Полное обновление специализации.',
        responses={200: SpecializationSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    partial_update=extend_schema(
        summary='Частичное обновление специализации',
        description='Позволяет обновить отдельные поля специализации.',
        responses={200: SpecializationSerializer, 400: OpenApiExample('Некорректные данные', {'error': 'Некорректные данные'})}
    ),
    destroy=extend_schema(
        summary='Удаление специализации',
        description='Удаляет специализацию из системы.',
        responses={204: None, 404: OpenApiExample('Специализация не найдена', {'error': 'Специализация с данным ID не найдена'})}
    ),
)
class SpecializationViewSet(viewsets.ModelViewSet):
    #API для работы со специализациями врачей
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]