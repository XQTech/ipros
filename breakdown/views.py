from breakdown.models import Ticket, Breakdown, Status, FunctionGroup, Customer, BreakdownCategory
from breakdown import serializers as bds
from breakdown.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets, status
from django.http import Http404
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
from django.conf import settings
import os


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
    
    # def pre_save(self, obj):
    #     print(obj)
    #     if (obj.image1 == None):
    #         obj.image1 = self.request.FILES.get('file')
    #     elif (obj.image2 == None):
    #         obj.image2 = self.request.FILES.get('file')
    #     elif (obj.image3 == None):
    #         obj.image3 = self.request.FILES.get('file')

    @action(detail=True)
    def breakdowns(self, request, pk=None):
        serializer = self.get_serializer(self.queryset.filter(ticket=pk), many=True)
        return Response(serializer.data)

class UploadImageView(APIView):
    def get_object(self, pk):
        try:
            return Breakdown.objects.get(pk=pk)
        except Breakdown.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):    
        bk = self.get_object(pk)
        print(self.request.FILES.get('file'))     
        if (bk.image1 == ''):          
            bk.image1 = self.request.FILES.get('file')
        elif (bk.image2 == ''):
            bk.image2 = self.request.FILES.get('file')
        elif (bk.image3 == ''):
            bk.image3 = self.request.FILES.get('file')
        bk.save()
        bks = bds.BreakdownSerializer(bk)
        return Response(bks.data)
    
    def delete(self, request, pk, format=None):
        filename = self.request.query_params.get('name')
        bk = self.get_object(pk)
        if (bk.image1.url.endswith(filename)):
            os.remove(settings.MEDIA_ROOT + bk.image1.url)
            bk.image1 = ''
        elif (bk.image2.url.endswith(filename)):
            os.remove(settings.MEDIA_ROOT + bk.image2.url)
            bk.image2 = ''
        elif (bk.image3.url.endswith(filename)):
            os.remove(settings.MEDIA_ROOT + bk.image3.url)
            bk.image3 = ''

        bk.save()
        return Response('{success:true}')

    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


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

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BreakdownCategory.objects.all()
    serializer_class = bds.CategorySerializer

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


