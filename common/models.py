from django.db import models

# Create your models here.
class SystemModule(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name