from django.db import models
from django.forms import CharField

# Create your models here.
class user(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email_address = models.EmailField(max_length=100)
  user_type = models.CharField(max_length=100)
  password = models.CharField(max_length=100)