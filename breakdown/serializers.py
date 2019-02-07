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

class BreakdownSerializer(serializers.ModelSerializer):
    ticket = serializers.ReadOnlyField(source='ticket.ticket_no')
    function_group = serializers.ReadOnlyField(source='function_group.description')
    class Meta:
        model = Breakdown
        fields = ('id', 'ticket', 'function_group', 'description', 'status',
                  'effort', 'create_date', 'create_user')

class TicketSerializer(serializers.ModelSerializer):
    #create_user = serializers.ReadOnlyField(source='create_user.username')
    #assigned_user = serializers.PrimaryKeyRelatedField()
    #status = serializers.Prima
    #breakdowns = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    breakdowns = BreakdownSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ('id', 'status', 'customer', 'assigned_user', 'ticket_no',
                  'description', 'create_user', 'breakdowns')


class FunctionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionGroup
        fields = ('id', 'description')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')
