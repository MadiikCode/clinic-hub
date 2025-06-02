# from rest_framework import routers
#
# from . import views
#
#
# router = routers.DefaultRouter()
# router.register('users', views.RegisterUserView, basename='register-user')
# router.register('sms', views.SMSVerificationViewSet)
# router.register('appointments', views.AppointmentViewSet)
#
#
# urlpatterns = router.urls


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users_app.views import RegisterUserView, UserViewSet

router = DefaultRouter()
router.register("users", UserViewSet, basename="users")  # Это ViewSet

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="register"),  # Это APIView
    path("", include(router.urls)),
]
