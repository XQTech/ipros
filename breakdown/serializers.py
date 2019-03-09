from rest_framework import serializers
from breakdown.models import Ticket, Breakdown, Status, FunctionGroup, BreakdownCategory
from django.contrib.auth.models import User


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'code')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')

class FunctionGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = FunctionGroup
        fields = ('id', 'description')

class BreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breakdown
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakdownCategory
        fields = '__all__'




