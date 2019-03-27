from django.contrib import admin
from .models import Status,Ticket,Breakdown,FunctionGroup,BreakdownCategory

# Register your models here.

class BreakdownCategoryAdmin(admin.ModelAdmin):
    list_display = ('parent', 'code')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')
admin.site.register(Status, StatusAdmin)
admin.site.register(FunctionGroup)
admin.site.register(BreakdownCategory, BreakdownCategoryAdmin)

