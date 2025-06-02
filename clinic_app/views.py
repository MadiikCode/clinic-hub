# from django.shortcuts import render
# from rest_framework import viewsets
# from .models import Category, Clinic, Schedule
# from .serializers import CategorySerializer, ClinicSerializer, ScheduleSerializer
#
#
# class CategoryView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class ClinicView(viewsets.ModelViewSet):
#     queryset = Clinic.objects.all()
#     serializer_class = ClinicSerializer
#
#
#
# class ScheduleView(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = ScheduleSerializer


from rest_framework import viewsets
from .models import Category, Clinic, Schedule, Service
from .serializers import CategorySerializer, ClinicSerializer, ScheduleSerializer, ServiceSerializer


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
