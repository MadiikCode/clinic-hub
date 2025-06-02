from users_app.models import Appointment
from datetime import datetime, timedelta
from django.utils import timezone

def create_appointment(user, clinic, service, doctor, date, time, notes=''):
    # Подсчёт времени окончания (если есть услуга)
    end_time = None
    if service and service.duration:
        end_time = (
            datetime.combine(date, time) + timedelta(minutes=service.duration)
        ).time()

    appointment = Appointment.objects.create(
        user=user,
        clinic=clinic,
        service=service,
        doctor=doctor,
        date=date,
        time=time,
        end_time=end_time,
        notes=notes,
        status='pending'
    )
    return appointment
