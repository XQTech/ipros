from rest_framework import serializers
from envs.models import Envitem, Envtype

class EnvtypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Envtype
        fields = '__all__'

class EnvitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envitem
        fields = '__all__'

