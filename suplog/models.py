from django.db import models
from django.conf import settings
import datetime

# Create your models here.

class SystemModule(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class CustomerStaff(models.Model):
    name = models.CharField(max_length=15)
    company = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ('company', 'name')

class Status(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Suplog(models.Model):
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    assignee = models.ForeignKey(
         settings.AUTH_USER_MODEL, related_name='suplog', on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(CustomerStaff, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, null=True, blank=True)
    solution = models.TextField(max_length=500, null=True, blank=True)
    issueType = models.ForeignKey(Type, null=True, on_delete=models.SET_NULL)
    sup_st_time = models.DateTimeField(null=True, blank=True)
    sup_ed_time = models.DateTimeField(null=True, blank=True)
    system = models.ForeignKey(SystemModule, null=True, on_delete=models.SET_NULL)

    @property
    def hours(self):
        if (self.sup_st_time == None or self.sup_ed_time == None):
            return 0
        else:
            delta = self.sup_ed_time - self.sup_st_time
            return round(delta.total_seconds() / 3600, 2)

    class Meta:
        ordering = ('-sup_ed_time', '-sup_st_time')

    def __str__(self):
        return '{} / {} / {}'.format(self.customer, self.reporter,
                                     self.issueType)