from rest_framework import viewsets
from .models import Category, Clinic, Schedule, Service
from .serializers import CategorySerializer, ClinicSerializer, ScheduleSerializer, ServiceSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiExample, OpenApiParameter

<<<<<<< HEAD
=======

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
>>>>>>> dc96274e6eb63e1251dbaaa01b4aed5ded0f87ad
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ClinicViewSet(viewsets.ModelViewSet):
    queryset = Clinic.objects.all()
    serializer_class = ClinicSerializer
