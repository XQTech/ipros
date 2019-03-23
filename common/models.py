from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class SystemModule(models.Model):
    name = models.CharField(max_length=50)
    customer = models.ManyToManyField(Customer, related_name="systems")

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ('name',)

class Config(models.Model):
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.key
    
    class Meta:
        ordering = ('key',)

# class Helplink(models.Model):
#     name = models.CharField(max_length=15)
#     customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

#     def __str__(self):
#         return self.name