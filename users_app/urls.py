from rest_framework import routers

from . import views
from users_app.views import UserViewSet


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('sms', views.SMSVerificationViewSet)
router.register('appointments', views.AppointmentViewSet)


urlpatterns = router.urls