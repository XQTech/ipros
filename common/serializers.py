from rest_framework import serializers
from .models import SystemModule, Customer, Config


class SystemModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemModule
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

