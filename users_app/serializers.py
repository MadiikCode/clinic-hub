from rest_framework import serializers

from users_app.models import UserManager ,User, SMSVerification, Appointment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id' , 'email', 'is_active', 'is_staff', 'role']



class SMSVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSVerification
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    clinic_name = serializers.CharField(source='clinic.name', read_only=True)
    doctor_name = serializers.CharField(source='doctor.name', read_only=True)
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = Appointment
        fields = [
            'id',
            'user',
            'clinic',
            'clinic_name',
            'service',
            'service_name',
            'doctor',
            'doctor_name',
            'date',
            'time',
            'end_time',
            'status',
            'notes',
            'created_at',
            'updated_at',
        ]