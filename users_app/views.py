from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action

from .models import User, SMSVerification, Appointment
from .serializers import (
    UserSerializer,
    SMSVerificationSerializer,
    AppointmentSerializer
)

from users_app.service.verification import verify_sms_code
from users_app.service.appointment_service import create_appointment


from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ValidationError
from users_app.service.registration import register_user

# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.decorators import action
# from django.utils import timezone
#
# from .models import User, SMSVerification, Appointment
# from .serializers import (
#     UserSerializer,
#     SMSVerificationSerializer,
#     AppointmentSerializer
# )
#
#
# from users_app.service.verification import verify_sms_code
#
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     permission_classes = [AllowAny]  # Измени на IsAuthenticated, если нужно
#     serializer_class = UserSerializer
#
#     @action(detail=False, methods=['post'])
#     def verify_code(self, request):
#         email = request.data.get('email')
#         code = request.data.get('code')
#         success, message = verify_sms_code(email, code)
#         return Response({'detail': message}, status=200 if success else 400)
#
#
#
# class SMSVerificationViewSet(viewsets.ModelViewSet):
#     queryset = SMSVerification.objects.all()
#     serializer_class = SMSVerificationSerializer
#     permission_classes = [AllowAny]
#
#     @action(detail=False, methods=['post'])
#     def verify_code(self, request):
#         email = request.data.get('email')
#         code = request.data.get('code')
#
#         try:
#             verification = SMSVerification.objects.get(email=email, code=code)
#             if verification.is_code_valid():
#                 verification.is_used = True
#                 verification.save()
#                 return Response({'detail': 'Код подтвержден.'}, status=status.HTTP_200_OK)
#             return Response({'detail': 'Код истёк или уже использован.'}, status=status.HTTP_400_BAD_REQUEST)
#         except SMSVerification.DoesNotExist:
#             return Response({'detail': 'Неверный код или email.'}, status=status.HTTP_404_NOT_FOUND)
#
#
# class AppointmentViewSet(viewsets.ModelViewSet):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
#



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get("email")
        role = request.data.get("role", "user")

        try:
            user = register_user(email=email, role=role)
            return Response(
                {"detail": "Пароль отправлен на email. Используйте его для входа."},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SMSVerificationViewSet(viewsets.ModelViewSet):
    queryset = SMSVerification.objects.all()
    serializer_class = SMSVerificationSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def verify_code(self, request):
        email = request.data.get('email')
        code = request.data.get('code')
        success, message = verify_sms_code(email, code)
        return Response({'detail': message}, status=status.HTTP_200_OK if success else status.HTTP_400_BAD_REQUEST)


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Если нужна простая логика, пока оставим как есть
        serializer.save(user=self.request.user)

        # Или можно сделать вот так, если используешь create_appointment():
        appointment_data = serializer.validated_data
        create_appointment(
            user=self.request.user,
            clinic=appointment_data['clinic'],
            service=appointment_data.get('service'),
            doctor=appointment_data.get('doctor'),
            date=appointment_data['date'],
            time=appointment_data['time'],
            notes=appointment_data.get('notes', '')
        )



