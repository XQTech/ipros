from django.urls import path, include
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from breakdown import views

app_name = 'breakdown'

#urlpatterns = [
    #path('', views.index, name='index'),
    #path('tickets', views.TicketList.as_view(), name='TicketList'),
    #path('ticket/<int:pk>', views.TicketDetail.as_view()),
    #path('tickets/', views.TicketList.as_view()),
    #path('', views.api_root),
#]

#urlpatterns = format_suffix_patterns([
#    path('', api_root),
#    path('tickets/', ticket_list, name='ticket-list'),
#    path('tickets/<int:pk>/', ticket_detail, name='ticket-detail')
#])

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'tickets', views.TicketViewSet)
router.register(r'breakdowns', views.BreakdownViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'funcgroups', views.FuncGroupsViewSet)
router.register(r'users', views.UsersViewSet)
router.register(r'categories', views.CategoryViewSet)

schema_view = get_schema_view(title='Pastebin API')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('schema/', schema_view),
    path('', include(router.urls)),
    path('jira/', views.JiraView.as_view(), name="jira-list"),
    url(r'^jira/upload/(?P<pk>[0-9]+)/$', views.UploadToJiraView.as_view(), name="upload-jira"),
    url(r'^breakdowns/image/(?P<pk>[0-9]+)/$', views.UploadImageView.as_view(), name="upload-image"),
    url(r'^breakdowns/doc/(?P<pk>[0-9]+)/$', views.GenerateDocView.as_view(), name="generate-doc"),
    path('docs/', views.DocumentListView.as_view(), name="doc-list"),
    # path('docs/<slug:slug>/', views.DocumentListView.as_view(), name="get-doc"),
]