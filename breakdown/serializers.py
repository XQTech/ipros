from rest_framework import serializers
from breakdown.models import Ticket, Breakdown, Customer, Status, FunctionGroup
from django.contrib.auth.models import User


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'code')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class FunctionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionGroup
        fields = ('id', 'description')

class BreakdownSerializer(serializers.ModelSerializer):
    ticket = serializers.ReadOnlyField(source='ticket.ticket_no')
    function_group = FunctionGroupSerializer()
    #status = StatusSerializer()
    class Meta:
        model = Breakdown
        fields = ('id', 'ticket', 'function_group', 'description', 'status',
                  'effort', 'create_date', 'create_user')

class TicketSerializer(serializers.ModelSerializer):
    breakdowns = BreakdownSerializer(many=True)
    status = StatusSerializer()
    customer = CustomerSerializer()
    assigned_user = UserSerializer()

    class Meta:
        model = Ticket
        #fields = '__all__'
        fields = ('id', 'status', 'customer', 'assigned_user', 'ticket_no',
                  'description', 'create_user', 'breakdowns')




