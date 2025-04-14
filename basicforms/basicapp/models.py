from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Device(models.Model):
    devname = models.CharField(max_length=60)
    devalias = models.CharField(max_length=60)
    def __str__(self):
        return self.devname
