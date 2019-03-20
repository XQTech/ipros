from django.contrib import admin
from .models import SystemModule, Customer

# Register your models here.

class SystemModuleAdmin(admin.ModelAdmin):
    fields = ['customer', 'name']
    list_display = ('name', 'customers')

    def customers(self, obj):
        return ", ".join([p.name for p in obj.customer.all()])

admin.site.register(SystemModule, SystemModuleAdmin)
admin.site.register(Customer)

