from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from common import views

app_name = 'common'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'systems', views.SystemModuleViewSet)
router.register(r'customers', views.CustomerViewSet)

schema_view = get_schema_view(title='Pastebin API')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls))
]