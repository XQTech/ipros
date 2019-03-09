from rest_framework import serializers
from suplog.models import Suplog, SystemModule, Customer, CustomerStaff, Status, Type
from django.contrib.auth.models import User


class SuplogSerializer(serializers.ModelSerializer):

    sup_st_time = serializers.DateTimeField(required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S")
    sup_ed_time = serializers.DateTimeField(required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Suplog
        fields = ('id', 'status', 'customer', 'assignee', 'reporter',
                  'description', 'solution', 'issueType', 'sup_st_time',
                  'sup_ed_time', 'system', 'hours')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class SystemModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemModule
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerStaff
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
