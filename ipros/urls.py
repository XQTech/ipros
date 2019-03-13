"""ipros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from django.views.generic.base import RedirectView

favicon_view = RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('user/', include('user.urls', namespace='user')),
    path('api/', include('breakdown.urls', namespace='breakdown')),
    path('api/sup/', include('suplog.urls', namespace='suplog')),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    path('breakdown/', RedirectView.as_view(url='/')),
    path('suplog/', RedirectView.as_view(url='/')),
    path('login/', RedirectView.as_view(url='/')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_jwt_token),
    path('favicon\.ico', favicon_view),
]
