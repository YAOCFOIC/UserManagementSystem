from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos.")
    
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username