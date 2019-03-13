from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from envs.models import Envitem, Envtype
from rest_framework import viewsets
from envs import serializers as envSerializer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EnvitemFilter

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'types': reverse('envtype-list', request=request, format=format),
        'items': reverse('envitem-list', request=request, format=format)
    })

class EnvtypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Envtype.objects.all()
    serializer_class = envSerializer.EnvtypeSerializer
    pagination_class = None

class EnvitemViewSet(viewsets.ModelViewSet):
    
    queryset = Envitem.objects.all()
    serializer_class = envSerializer.EnvitemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = EnvitemFilter
    pagination_class = None
