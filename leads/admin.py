from django.contrib import admin

# Register your models here.
from .models import Lead, Provider, User

admin.site.register(User)
admin.site.register(Lead)
admin.site.register(Provider)