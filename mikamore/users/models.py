from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=255, verbose_name="email")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
