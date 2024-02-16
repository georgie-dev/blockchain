from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username= None
    email = models.EmailField(max_length=100, unique=True)
    wallet= models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    referral = models.CharField(max_length=100, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)

class CryptoData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    btc= models.FloatField(default=0.00)
    eth= models.FloatField(default=0.00)
    sol= models.FloatField(default=0.00)

