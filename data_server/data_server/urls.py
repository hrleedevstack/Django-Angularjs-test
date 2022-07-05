"""data_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from django.conf.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

import data.views as views
import data.api

app_name = 'data'

router = routers.DefaultRouter()
router.register('data', data.api.DataVeiwSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexPage, name='index'),
    path('popup.html', views.popupPage, name='popup'),
    path('api/doc/', get_swagger_view(title='Rest API Document')),
    path('api/v1/', include((router.urls, 'data'), namespace='api')),
]
