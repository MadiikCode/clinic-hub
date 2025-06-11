from rest_framework import viewsets
from .models import Category, Clinic, Schedule, Service
from .serializers import CategorySerializer, ClinicSerializer, ScheduleSerializer, ServiceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample, OpenApiParameter

#CategoryViewSet
@extend_schema_view(
    list=extend_schema(
        summary='Получение списка категорий',
        description='Описание Получение списка категорий',
        responses={
            200: CategorySerializer,
            404: OpenApiExample(
                'Категория не найдена',
                {'error': 'Категория с данным ID не найдена'}
            )
        }
    ),
    retrieve=extend_schema(
        summary='Получение категории',
        description='Описание Получение категории',
        responses={
            200: CategorySerializer,
            404: OpenApiExample(
                'Категория не найдена',
                {'error': 'Категория с данным ID не найдена'}
            )
        }
    ),
    create=extend_schema(
        summary='Создание категории',
        description='Описание Создание категории',
        responses={
            201: CategorySerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    update=extend_schema(
        summary='Обновление категории',
        description='Описание Обновление категории',
        responses={
            200: CategorySerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    partial_update=extend_schema(
        summary='Частичное обновление категории',
        description='Описание Частичное обновление категории',
        responses={
            200: CategorySerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    destroy=extend_schema(
        summary='Удаление категории',
        description='Описание Удаление категории',
        responses={
            204: None,
            404: OpenApiExample(
                'Категория не найдена',
                {'error': 'Категория с данным ID не найдена'}
            )
        }
    )
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



#ServiceViewSet
@extend_schema_view(
    list=extend_schema(
        summary=' Получение списка услуг',
        description='Описание Получение списка услуг',
        responses={
            200: ServiceSerializer,
            404: OpenApiExample(
                'Услуга не найдена',
                {'error': 'Услуга с данным ID не найдена'}
            )
        }
    ),
    retrieve=extend_schema(
        summary=' Получение услуги',
        description='Описание Получение услуги',
        responses={
            200: ServiceSerializer,
            404: OpenApiExample(
                'Услуга не найдена',
                {'error': 'Услуга с данным ID не найдена'}
            )
        }
    ),
    create=extend_schema(
        summary=' Создание услуги',
        description='Описание Создание услуги',
        responses={
            201: ServiceSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    update=extend_schema(
        summary=' Обновление услуги',
        description='Описание Обновление услуги',
        responses={
            200: ServiceSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    partial_update=extend_schema(
        summary=' Частичное обновление услуги',
        description='Описание Частичное обновление услуги',
        responses={
            200: ServiceSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    destroy=extend_schema(
        summary=' Удаление услуги',
        description='Описание Удаление услуги',
        responses={
            204: None,
            404: OpenApiExample(
                'Услуга не найдена',
                {'error': 'Услуга с данным ID не найдена'}
            )
        }
    )
)

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


#ScheduleViewSet
@extend_schema_view(
    list=extend_schema(
        summary=' Получение списка расписаний',
        description='Описание Получение списка расписаний',
        responses={
            200: ScheduleSerializer,
            404: OpenApiExample(
                'Расписание не найдено',
                {'error': 'Расписание с данным ID не найдено'}
            )
        }
    ),
    retrieve=extend_schema(
        summary=' Получение расписания',
        description='Описание Получение расписания',
        responses={
            200: ScheduleSerializer,
            404: OpenApiExample(
                'Расписание не найдено',
                {'error': 'Расписание с данным ID не найдено'}
            )
        }
    ),
    create=extend_schema(
        summary=' Создание расписания',
        description='Описание Создание расписания',
        responses={
            201: ScheduleSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    update=extend_schema(
        summary=' Обновление расписания',
        description='Описание Обновление расписания',
        responses={
            200: ScheduleSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    partial_update=extend_schema(
        summary=' Частичное обновление расписания',
        description='Описание Частичное обновление расписания',
        responses={
            200: ScheduleSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    destroy=extend_schema(
        summary=' Удаление расписания',
        description='Описание Удаление расписания',
        responses={
            204: None,
            404: OpenApiExample(
                'Расписание не найдено',
                {'error': 'Расписание с данным ID не найдено'}
            )
        }
    )
)

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer



#ClinicViewSet
@extend_schema_view(
    list=extend_schema(
        summary=' Получение списка клиник',
        description='Описание Получение списка клиник',
        responses={
            200: ClinicSerializer,
            404: OpenApiExample(
                'Клиника не найдена',
                {'error': 'Клиника с данным ID не найдена'}
            )
        }
    ),
    retrieve=extend_schema(
        summary=' Получение клиники',
        description='Описание Получение клиники',
        responses={
            200: ClinicSerializer,
            404: OpenApiExample(
                'Клиника не найдена',
                {'error': 'Клиника с данным ID не найдена'}
            )
        }
    ),
    create=extend_schema(
        summary=' Создание клиники',
        description='Описание Создание клиники',
        responses={
            201: ClinicSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    update=extend_schema(
        summary=' Обновление клиники',
        description='Описание Обновление клиники',
        responses={
            200: ClinicSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    partial_update=extend_schema(
        summary=' Частичное обновление клиники',
        description='Описание Частичное обновление клиники',
        responses={
            200: ClinicSerializer,
            400: OpenApiExample(
                'Некорректные данные',
                {'error': 'Некорректные данные'}
            )
        }
    ),
    destroy=extend_schema(
        summary=' Удаление клиники',
        description='Описание Удаление клиники',
        responses={
            204: None,
            404: OpenApiExample(
                'Клиника не найдена',
                {'error': 'Клиника с данным ID не найдена'}
            )
        }
    )
)

class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
