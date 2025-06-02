from rest_framework import serializers

from users_app.models import UserManager ,User, SMSVerification, Appointment
from users_app.service.user_service import create_user_with_password  # вот он

from django.contrib.auth.password_validation import validate_password
from users_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'is_staff', 'role']  # Пароль убран


class SMSVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSVerification
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    doctor_name = serializers.SerializerMethodField()
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id', 'user', 'clinic', 'clinic_name', 'service', 'service_name',
            'doctor', 'doctor_name', 'date', 'time', 'end_time', 'status', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'end_time', 'created_at', 'updated_at']

    def get_doctor_name(self, obj):
        return getattr(obj.doctor, 'user', None) and obj.doctor.user.email


