from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
  email = models.EmailField(_('email address'), unique=True)

  objects = CustomUserManager

  def __str__(self):
    return self.email
