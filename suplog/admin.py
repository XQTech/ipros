from django.contrib import admin
from .models import Suplog, CustomerStaff, Status, Type

# Register your models here.

# class SuplogAdmin(admin.ModelAdmin):
#     readonly_fields = ('hours',)

class CustomerStaffAdmin(admin.ModelAdmin):
    list_display = ('company', 'name')

admin.site.register(CustomerStaff, CustomerStaffAdmin)
admin.site.register(Status)
admin.site.register(Type)
# admin.site.register(Suplog, SuplogAdmin)

