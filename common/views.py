from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from common.models import SystemModule, Customer
from rest_framework import viewsets
from common import serializers as commonSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'systems': reverse('system-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format)
    })

class SystemModuleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SystemModule.objects.all()
    serializer_class = commonSerializer.SystemModuleSerializer
    pagination_class = None

class CustomerViewSet(viewsets.ModelViewSet):
    
    queryset = Customer.objects.all()
    serializer_class = commonSerializer.CustomerSerializer
    pagination_class = None
