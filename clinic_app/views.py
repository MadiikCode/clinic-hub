from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Clinic, Schedule
from .serializers import CategorySerializer, ClinicSerializer, ScheduleSerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ClinicView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ClinicSerializer


class ScheduleView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = ScheduleSerializer
