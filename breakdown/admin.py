from django.contrib import admin
from .models import Status,Ticket,Breakdown,FunctionGroup,BreakdownCategory

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'code')

admin.site.register(Status, StatusAdmin)

class FunctionGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(FunctionGroup, FunctionGroupAdmin)

class BreakdownCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'parent', 'tips')

admin.site.register(BreakdownCategory, BreakdownCategoryAdmin)

