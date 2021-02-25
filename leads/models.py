from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user                = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



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
    organisation        = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(post_user_created_signal, sender=User)
