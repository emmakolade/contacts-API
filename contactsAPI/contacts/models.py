from django.db import models
from django.contrib.auth.models import User

# Create your models here.:


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(max_length=255)
    contact_picture = models.URLField(null=True)
    address = models.CharField(max_length=255)
    is_favourite = models.BooleanField(default=True)
