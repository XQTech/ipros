from .models import Envitem
import django_filters

class EnvitemFilter(django_filters.FilterSet):
    class Meta:
        model = Envitem
        fields = {            
            'customer': ['exact',],
            'envtype': ['exact',],
            'name': ['icontains',],
            'url': ['icontains',],
            'remark': ['icontains',]
        }