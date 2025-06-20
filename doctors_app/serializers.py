from rest_framework import serializers

from doctors_app.models import Doctor, ScheduleDoctor, ReviewDoctor, Specialization



class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    specialization = SpecializationSerializer(read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=1, read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'


class ScheduleDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleDoctor
        fields = '__all__'


class ReviewDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewDoctor
        fields = '__all__'