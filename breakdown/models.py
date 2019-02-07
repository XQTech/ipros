from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum


# Create your models here.
class TaskStatus(Enum):
    NOT_STARTED = 1
    IN_PROGRESS = 2
    DONE = 3

    def __str__(self):
        return self.name


class Status(models.Model):
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.code


class Customer(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class TicketManager(models.Manager):
    def all_with_prefetch_breakdown(self):
        qs = self.get_queryset()
        return qs.prefetch_related('breakdown')


class Ticket(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    assigned_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='tickets', on_delete=models.SET_NULL, null=True)
    ticket_no = models.CharField(max_length=10, default="")
    description = models.TextField(max_length=500, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)

    objects = TicketManager()

    class Meta:
        ordering = ('customer', 'ticket_no')

    def __str__(self):
        return '{} - {} - {}'.format(self.customer, self.ticket_no,
                                     self.status)


class FunctionGroup(models.Model):
    description = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.description


class Breakdown(models.Model):
    ticket = models.ForeignKey(
        Ticket, on_delete=models.PROTECT, related_name='breakdowns')
    function_group = models.ForeignKey(FunctionGroup, on_delete=models.PROTECT)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=10, default=TaskStatus.NOT_STARTED)
    effort = models.IntegerField(
        default=0, validators=[MaxValueValidator(500),
                               MinValueValidator(0)])
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ('ticket', 'function_group', 'create_date')

    def __str__(self):
        return '{} - {} - {}'.format(self.ticket, self.function_group,
                                     self.description)
