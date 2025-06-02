from users_app.models import SMSVerification

def verify_sms_code(email, code):
    try:
        verification = SMSVerification.objects.get(email=email, code=code)
        if verification.is_code_valid():
            verification.is_used = True
            verification.save()
            return True, "Код подтвержден."
        return False, "Код истёк или уже использован."
    except SMSVerification.DoesNotExist:
        return False, "Неверный код или email."
