from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ServiceViewSet, ScheduleViewSet, ClinicViewSet


router = DefaultRouter()
# router.register(r'categories', CategoryView, basename='category')
# router.register(r'clinics', ClinicView, basename='clinic')
# router.register(r'schedules', ScheduleView, basename='schedule')

router.register('categories', CategoryViewSet)
router.register('services', ServiceViewSet)
router.register('schedules', ScheduleViewSet)
router.register('clinics', ClinicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]