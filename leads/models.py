from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    company_name        = models.CharField(max_length=100, default='PiLife')
    pass



class Lead(models.Model):
    first_name          = models.CharField(max_length=20)
    last_name           = models.CharField(max_length=20)
    phone_number        = models.IntegerField(default=0)
    email_address       = models.EmailField()
    date_of_birth       = models.DateField()
    number_of_people    = models.IntegerField(default=1)
    health_plan         = models.CharField(max_length=20, blank=True)
    provider            = models.ForeignKey("Provider", on_delete=models.SET_DEFAULT, default= "PiLife")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Provider(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name        = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.user.company_name
