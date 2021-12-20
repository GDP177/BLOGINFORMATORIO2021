from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	dni = models.CharField(max_length=8, null=True, blank=True)
	birth_date = models.DateField(null=True, blank=True)
