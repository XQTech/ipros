from rest_framework import serializers
from suplog.models import Suplog, CustomerStaff, Status, Type

class SuplogSerializer(serializers.ModelSerializer):

    sup_st_time = serializers.DateTimeField(required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S")
    sup_ed_time = serializers.DateTimeField(required=False, allow_null=True, format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Suplog
        fields = ('id', 'status', 'customer', 'assignee', 'reporter',
                  'description', 'solution', 'issueType', 'sup_st_time',
                  'sup_ed_time', 'system', 'hours')

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
