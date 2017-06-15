from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# table for users extends the main User table
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    city = models.CharField(max_length=250)
