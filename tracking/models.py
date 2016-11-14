from django.db import models

# Create your models here.
class Package(models.Model):
    change_date = models.DateTimeField()
    place = models.CharField(max_length=100)
    message = models.CharField(max_length=255)
