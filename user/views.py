#from django.contrib.auth.forms import UserCreationForm
#from django.urls import reverse_lazy
#from django.views.generic import CreateView
from breakdown.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets

# Create your views here.
#class RegisterView(CreateView):
#    template_name = 'user/register.html'
#    form_class = UserCreationForm
#    success_url = reverse_lazy('breakdown:TicketList')

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

