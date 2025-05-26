from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from django.utils import timezone

from .models import User, SMSVerification, Appointment
from .serializers import (
    UserSerializer,
    SMSVerificationSerializer,
    AppointmentSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # Измени на IsAuthenticated, если нужно
    serializer_class = UserSerializer



class SMSVerificationViewSet(viewsets.ModelViewSet):
    queryset = SMSVerification.objects.all()
    serializer_class = SMSVerificationSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def verify_code(self, request):
        email = request.data.get('email')
        code = request.data.get('code')

        try:
            verification = SMSVerification.objects.get(email=email, code=code)
            if verification.is_code_valid():
                verification.is_used = True
                verification.save()
                return Response({'detail': 'Код подтвержден.'}, status=status.HTTP_200_OK)
            return Response({'detail': 'Код истёк или уже использован.'}, status=status.HTTP_400_BAD_REQUEST)
        except SMSVerification.DoesNotExist:
            return Response({'detail': 'Неверный код или email.'}, status=status.HTTP_404_NOT_FOUND)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
