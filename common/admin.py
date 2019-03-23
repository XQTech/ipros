from django.contrib import admin
from .models import SystemModule, Customer, Config

# Register your models here.

class SystemModuleAdmin(admin.ModelAdmin):
    fields = ['customer', 'name']
    list_display = ('name', 'customers')

    def customers(self, obj):
        return ", ".join([p.name for p in obj.customer.all()])

admin.site.register(SystemModule, SystemModuleAdmin)

class ConfigAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

admin.site.register(Config, ConfigAdmin)
admin.site.register(Customer)

