import random
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from users_app.models import User


def register_user(email: str, role: str = 'user') -> User:
    if not email:
        raise ValidationError("Email обязателен.")

    if User.objects.filter(email=email).exists():
        raise ValidationError("Пользователь с таким email уже существует.")

    # Генерируем случайный 8-значный пароль
    password = ''.join(random.choices('abcdefghijkmnpqrstuvwxyz23456789', k=8))

    user = User(email=email, role=role)
    user.set_password(password)
    user.is_active = False  # активировать позже, например после подтверждения кода
    user.save()

    # Отправка пароля на email
    send_mail(
        subject='Ваш пароль для входа',
        message=f'Ваш временный пароль: {password}',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )

    return user
