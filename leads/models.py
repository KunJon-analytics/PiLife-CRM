from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_provider = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    date_of_birth = models.DateField()
    number_of_people = models.IntegerField(default=1)
    health_plan = models.CharField(max_length=20, blank=True)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        "Provider", null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(
        "Category", related_name="leads", null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Category(models.Model):
    # New, Contacted, Converted, Unconverted
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
