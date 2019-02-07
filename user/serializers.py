from rest_framework import serializers
from breakdown.models import Ticket
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Ticket.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tickets')