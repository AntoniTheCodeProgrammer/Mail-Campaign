from django.db import models

# Create your models here.
class Mail(models.Model):
    author = models.CharField(max_length=255)
    text = models.CharField(max_length=2550)