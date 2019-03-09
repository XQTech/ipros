from django.contrib import admin
from .models import Status,Ticket,Breakdown,FunctionGroup,BreakdownCategory

# Register your models here.
admin.site.register(Status)
# admin.site.register(Customer)
# admin.site.register(Ticket)
admin.site.register(Breakdown)
admin.site.register(FunctionGroup)
admin.site.register(BreakdownCategory)

