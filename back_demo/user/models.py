from django.contrib.auth.models import AbstractUser
from django.db import models


class User:
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
