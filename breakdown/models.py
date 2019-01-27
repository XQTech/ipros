from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Status(models.Model):
    code = models.CharField(max_length=15)
    def __str__(self):
        return self.code

class Customer(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ticket_no = models.CharField(max_length=10, default="")
    description = models.TextField(max_length=500, null=True)
    start_date =  models.DateField(null=True)
    end_date = models.DateField(null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('customer', 'ticket_no')

    def __str__(self):
        return '{} - {} - {}'.format(self.customer, self.ticket_no, self.status)

class FunctionGroup(models.Model):
    description = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.description

class Breakdown(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.PROTECT)
    function_group = models.ForeignKey(FunctionGroup, on_delete=models.PROTECT)
    description = models.TextField(max_length=500, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    effort = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(500),
            MinValueValidator(0)
        ]
    )
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.description







