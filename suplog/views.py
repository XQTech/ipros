from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from suplog.models import Suplog, SystemModule, Customer, CustomerStaff, Status, Type
from rest_framework import permissions, viewsets, status
from suplog import serializers as supSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from .filters import SuplogFilter

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'suplogs': reverse('suplog-list', request=request, format=format),
        'systems': reverse('system-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format),
        'reporters': reverse('reporter-list', request=request, format=format),
        'statuss': reverse('status-list', request=request, format=format),
        'types': reverse('type-list', request=request, format=format),
    })

class SystemModuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SystemModule.objects.all()
    serializer_class = supSerializer.SystemModuleSerializer
    pagination_class = None

class SuplogViewSet(viewsets.ModelViewSet):
    
    queryset = Suplog.objects.all()
    serializer_class = supSerializer.SuplogSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = SuplogFilter

class SuplogSummaryViewSet(APIView):
    
    def get_object(self):
        try:
            return Suplog.objects.all()
        except Suplog.DoesNotExist:
            pass

    def get(self, request):
        startTime = self.request.query_params.get('start-time')
        endTime = self.request.query_params.get('end-time')
        if startTime == None or startTime == '':
            startTime = '2014-01-01'
        if endTime == None or endTime == '':
            endTime = '2100-01-01'
        objects = self.get_object().filter(sup_st_time__range=[datetime.strptime(startTime , '%Y-%m-%d'), datetime.strptime(endTime , '%Y-%m-%d')])
        serializer = supSerializer.SuplogSerializer(objects, many=True)
        return Response(serializer.data)


class CustomerViewSet(viewsets.ModelViewSet):
    
    queryset = Customer.objects.all()
    serializer_class = supSerializer.CustomerSerializer
    pagination_class = None

class CustomerStaffViewSet(viewsets.ModelViewSet):
    
    queryset = CustomerStaff.objects.all()
    serializer_class = supSerializer.CustomerStaffSerializer
    pagination_class = None

class StatusViewSet(viewsets.ModelViewSet):
    
    queryset = Status.objects.all()
    serializer_class = supSerializer.StatusSerializer
    pagination_class = None

class TypeViewSet(viewsets.ModelViewSet):
    
    queryset = Type.objects.all()
    serializer_class = supSerializer.TypeSerializer
    pagination_class = None


