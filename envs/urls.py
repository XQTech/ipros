from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from envs import views

app_name = 'envs'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'types', views.EnvtypeViewSet)
router.register(r'items', views.EnvitemViewSet)

schema_view = get_schema_view(title='Pastebin API')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls))
]