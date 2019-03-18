from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import Enum


# Create your models here.
class Status(models.Model):
    code = models.CharField(max_length=15)

    def __str__(self):
        return self.code


# class Ticket(models.Model):
#     status = models.ForeignKey(Status, on_delete=models.PROTECT)
#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
#     assigned_user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, related_name='tickets', on_delete=models.SET_NULL, null=True)
#     ticket_no = models.CharField(max_length=10, default="")
#     description = models.TextField(max_length=500, null=True, blank=True)
#     start_date = models.DateField(null=True, blank=True)
#     end_date = models.DateField(null=True, blank=True)
#     create_date = models.DateTimeField(auto_now_add=True)
#     create_user = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         ordering = ('customer', 'ticket_no')

#     def __str__(self):
#         return '{} - {} - {}'.format(self.customer, self.ticket_no,
#                                      self.status)

class FunctionGroup(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class BreakdownCategory(models.Model):
    code = models.CharField(max_length=50)
    parent = models.ForeignKey('self', related_name='sub_category', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.code


class Ticket(models.Model):
    # status.name
    status = models.CharField(max_length=20, null=True, blank=True)
    # fixVersions.name
    customer = models.CharField(max_length=20, null=True, blank=True)
    # assignee.name
    assignee = models.CharField(max_length=30, null=True, blank=True)
    # key
    ticket_no = models.CharField(max_length=20, null=True, blank=True)
    # summary
    summary = models.TextField(max_length=500, null=True, blank=True)
    # duedate
    due_date = models.DateField(null=True, blank=True)
    # customfield_10112
    gn_no = models.CharField(max_length=50, null=True, blank=True)
    # id
    jira_id = models.IntegerField(default=0)

    class Meta:
        ordering = ('-jira_id',)

    def __str__(self):
        return '{} / {} / {}'.format(self.customer, self.ticket_no,
                                     self.status)


def upload_path_handler(instance, filename):
    return 'breakdown/' + instance.ticket.ticket_no + '/' + filename
    
class Breakdown(models.Model):
    sequence = models.IntegerField(default=0)
    category = models.ForeignKey(BreakdownCategory, null=True, blank=True, on_delete=models.SET_NULL)
    ticket = models.ForeignKey(
        Ticket, on_delete=models.PROTECT, related_name='breakdowns')
    function_group = models.ForeignKey(FunctionGroup, null=True, on_delete=models.SET_NULL)
    description = models.TextField(max_length=500, null=True, blank=True)
    status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    effort = models.FloatField(null=True, blank=True, default=0.0)        
    assigned_user = models.ForeignKey(
         settings.AUTH_USER_MODEL, related_name='breakdowns', on_delete=models.SET_NULL, null=True)
    image1 = models.ImageField(upload_to=upload_path_handler, null=True, blank=True)
    image2 = models.ImageField(upload_to=upload_path_handler, null=True, blank=True)
    image3 = models.ImageField(upload_to=upload_path_handler, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    create_user = models.CharField(max_length=50, blank=True, null=True)
    in_fd = models.BooleanField(default=True)
    in_bk = models.BooleanField(default=True)

    class Meta:
        ordering = ('sequence', 'ticket', 'function_group', 'create_date')

    def __str__(self):
        return '{} - {} - {}'.format(self.ticket, self.function_group,
                                     self.description)
