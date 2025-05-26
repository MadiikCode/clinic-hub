from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('sms', views.SMSVerificationViewSet)
router.register('appointments', views.AppointmentViewSet)


urlpatterns = router.urls