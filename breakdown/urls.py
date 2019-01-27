from django.urls import path
from . import views

app_name = 'breakdown'
urlpatterns = [
    path('', views.index, name='index'),
    path('tickets', views.TicketList.as_view(), name='TicketList'),
    path('ticket/<int:pk>', views.TicketDetail.as_view(), name='TicketDetail'),
]