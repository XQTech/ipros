from .models import Suplog
import django_filters

class SuplogFilter(django_filters.FilterSet):
    class Meta:
        model = Suplog
        fields = {
            'id':['in'],
            'status': ['exact',],
            'customer': ['exact',],
            'assignee': ['exact',],
            'description': ['icontains',],
            'solution': ['icontains',],
            'system': ['exact']
        }