# from rest_framework import serializers
# from .models import Category, Clinic, Schedule
#
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'
#
#
# class ClinicSerializer(serializers.ModelSerializer):
#     services = serializers.StringRelatedField(many=True, read_only=True)
#     category = serializers.StringRelatedField()
#     schedule = serializers.StringRelatedField()
#
#     class Meta:
#         model = Clinic
#         fields = '__all__'
#
#
#
# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = '__all__'





from rest_framework import serializers
from .models import Category, Clinic, Schedule, Service


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


class ClinicSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    services = ServiceSerializer(many=True, read_only=True)
    schedule = ScheduleSerializer(read_only=True)

    class Meta:
        model = Clinic
        fields = '__all__'
