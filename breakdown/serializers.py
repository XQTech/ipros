from rest_framework import serializers
from breakdown.models import Ticket, Breakdown, Status, FunctionGroup, BreakdownCategory
from django.contrib.auth.models import User
import datetime
from common.config import SysConfig, ConfigKey


sysConfig = SysConfig()
incompleteIds = sysConfig.getStringConfig(ConfigKey.INCOMPLETE_BK_ST_ID).split(',')

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
    restdays = serializers.SerializerMethodField()

    def get_bkcount(self, obj):
        return obj.breakdowns.count()
    
    def get_restdays(self, obj):
        bks = obj.breakdowns.all()
        mindiff = 100
        for bk in bks:
            try:
                index = incompleteIds.index(str(bk.status.id))
                if bk.due_date != None and index >= 0:
                    diff = (bk.due_date - datetime.date.today()).days
                    if mindiff > diff:
                        mindiff = diff
            except ValueError:
                continue

        return mindiff

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
        fields = ('id', 'code', 'parent', 'tips', 'sub_category')





