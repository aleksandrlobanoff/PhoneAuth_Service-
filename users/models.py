from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = None

    phone_number = models.CharField(max_length=12, unique=True)
    otp_code = models.CharField(max_length=4)

    def __str__(self):
        return self.phone_number

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def check_otp_code(self, otp_code):
        return self.otp_code == otp_code

    def __str__(self):
        return self.phone_number
