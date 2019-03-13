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
    bkcount = serializers.SerializerMethodField()

    def get_bkcount(self, obj):
        return obj.breakdowns.count()

    class Meta:
        model = Ticket
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BreakdownCategory
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(many=True)
    class Meta:
        model = BreakdownCategory
        fields = ('id','code','parent','sub_category')


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BreakdownCategory
#         fields = '__all__'





