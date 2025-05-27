from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('doctors', views.DoctorViewSet, basename='doctors')
router.register('schedules', views.ScheduleDoctorViewSet, basename='schedules')
router.register('reviews', views.ReviewDoctorViewSet, basename='reviews')
router.register('specializations', views.SpecializationViewSet, basename='specializations')


urlpatterns = [
    path('', include(router.urls)),
]