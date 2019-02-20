from breakdown.models import Ticket, Breakdown, Status, FunctionGroup, Customer
from breakdown import serializers as bds
from breakdown.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.decorators import action, api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.contrib.auth.models import User
from .filters import TicketFilter
from jira import JIRA
from django.views import View


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tickets': reverse('ticket-list', request=request, format=format),
        'breakdowns': reverse('breakdown-list', request=request, format=format),
    })

class TicketViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Ticket.objects.all()
    serializer_class = bds.TicketSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = TicketFilter
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # def perform_create(self, serializer):
    #    serializer.save()


class BreakdownViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    
    queryset = Breakdown.objects.all()
    serializer_class = bds.BreakdownSerializer
    #permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        print("perform_create of breakdown in serializer...")
        #serializer.save(create_user=self.request.user.username)
        serializer.save()

    
    @action(detail=True)
    def breakdowns(self, request, pk=None):
        serializer = self.get_serializer(self.queryset.filter(ticket=pk), many=True)
        return Response(serializer.data)


class StatusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Status.objects.all()
    serializer_class = bds.StatusSerializer

class FuncGroupsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FunctionGroup.objects.all()
    serializer_class = bds.FunctionGroupSerializer

class CustomersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = bds.CustomerSerializer

class UsersViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = bds.UserSerializer

# For auth with JWT
class RestrictedView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'id': request.user.id,
            'username': request.user.username,
            'token': str(request.auth)
        }
        return Response(data)

class JiraView(APIView):

    queryset = None
    serializer_class = None
    def get(self, request, format=None):
        """
        Return a list of all issues.
        """
        jira_server = 'http://192.168.3.39:8080'
        jira_username = 'liqiang'
        jira_password = 'lq2017@gips'

        myjira = JIRA(jira_server,basic_auth=(jira_username,jira_password))
        # jql_str = "project%20%3D%20IPROS%20AND%20createdDate%20>%3D%202018-01-01%20AND%20type%20%3D%20Task%20"
        jql_str = "project = IPROS AND createdDate >= 2018-01-01 AND type = Task"
        fields = [
            'status',
            'fixVersions',
            'assignee',
            'key',
            'summary',
            'duedate',
            'customfield_10112',
            'id'
        ]
        data = myjira.search_issues(jql_str, 0, -1, True, fields, None, True)
        return Response(data)


