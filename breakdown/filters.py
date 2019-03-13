from .models import Ticket
import django_filters

class TicketFilter(django_filters.FilterSet):
    class Meta:
        model = Ticket
        fields = {            
            'status': ['icontains',],
            'customer': ['icontains',],
            'assignee': ['icontains',],
            'ticket_no': ['icontains',],
            'summary': ['icontains',],
            'gn_no': ['icontains'],
            'jira_id': ['iexact']
        }