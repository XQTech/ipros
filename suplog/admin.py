from django.contrib import admin
from .models import SystemModule, Suplog, Customer, CustomerStaff, Status, Type

# Register your models here.
admin.site.register(SystemModule)
admin.site.register(Customer)
admin.site.register(CustomerStaff)
admin.site.register(Status)
admin.site.register(Type)

class SuplogAdmin(admin.ModelAdmin):
    readonly_fields = ('hours',)

admin.site.register(Suplog, SuplogAdmin)