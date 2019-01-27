from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from breakdown.models import Ticket

# Create your views here.
def index(request):
    return HttpResponse("Hello World, You're at the breakdown index.")

class TicketList(ListView):
    model = Ticket
    paginate_by = 5

class TicketDetail(DetailView):
    model = Ticket
