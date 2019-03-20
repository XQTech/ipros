from django.contrib import admin
from .models import Status,Ticket,Breakdown,FunctionGroup,BreakdownCategory

# Register your models here.

class BreakdownCategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'code')

admin.site.register(Status)
# admin.site.register(Ticket)
# admin.site.register(Breakdown)
admin.site.register(FunctionGroup)
admin.site.register(BreakdownCategory, BreakdownCategoryAdmin)

