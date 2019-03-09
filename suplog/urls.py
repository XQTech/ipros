from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from suplog import views

app_name = 'suplog'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'suplogs', views.SuplogViewSet)
router.register(r'systems', views.SystemModuleViewSet)
router.register(r'statuss', views.StatusViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'reporters', views.CustomerStaffViewSet)
router.register(r'types', views.TypeViewSet)
router.register(r'users', views.UsersViewSet)

schema_view = get_schema_view(title='Pastebin API')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
    path('suplogs-all/', views.SuplogSummaryViewSet.as_view(), name="suplogs-all")
]