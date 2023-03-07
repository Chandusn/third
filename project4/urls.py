"""project4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app3.views import *
from app4.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('app3_first/',app3_first,name='app3_first'),
    path('app3_second/',app3_second,name='app3_second'),
    path('app4_first/',app4_first,name='app4_first'),
    path('app4_second/',app4_second,name='app4_second'),
]
