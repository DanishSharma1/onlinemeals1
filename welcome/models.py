from django.db import models


# Create your models here
class Hotel(models.Model):
    ItemName = models.CharField(max_length=255)
    Price = models.CharField(max_length=255)





