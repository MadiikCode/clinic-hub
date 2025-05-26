from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryView, ClinicView, ScheduleView


router = DefaultRouter()
router.register(r'categories', CategoryView, basename='category')
router.register(r'clinics', ClinicView, basename='clinic')
router.register(r'schedules', ScheduleView, basename='schedule')



urlpatterns = [
    path('', include(router.urls)),
]