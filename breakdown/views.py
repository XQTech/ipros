from breakdown.models import Ticket, Breakdown, Status, FunctionGroup, Customer
from breakdown import serializers as bds
from breakdown.permissions import IsOwnerOrReadOnly
from rest_framework import permissions, viewsets
from rest_framework.decorators import action, api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

# Create your views here.
#def index(request):
#    return HttpResponse("Hello World, You're at the breakdown index.")

#class TicketList(ListView):
#    model = Ticket
#    paginate_by = 5

#class TicketDetail(DetailView):
#    model = Ticket
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
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    #@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    #def highlight(self, request, *args, **kwargs):
    #    snippet = self.get_object()
    #    return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(create_user=self.request.user.username)

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
        serializer.save(create_user='QQ')
    
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


