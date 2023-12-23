from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from account.models import CustomUser

def validate_email_unique(email):
    if CustomUser.objects.filter(email=email).exists():
        raise ValidationError("Este correo electrónico ya está registrado.")

def validate_username_unique(username):
    if CustomUser.objects.filter(username=username).exists():
        raise ValidationError("Este nombre de usuario ya está en uso.")

def validate_passwords_match(password1, password2):
    if password1 and password2 and password1 != password2:
        raise ValidationError("Las contraseñas no coinciden. Inténtalo de nuevo.")