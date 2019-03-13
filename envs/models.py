from django.db import models
from common.models import Customer

# Create your models here.
class Envtype(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Envitem(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    envtype = models.ForeignKey(Envtype, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    remark = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ('customer', 'envtype', 'name')

    def __str__(self):
        return '{} / {} / {}'.format(self.customer, self.envtype,
                                     self.name)