"""Mxonline3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import path, include, re_path
# from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # Django 2.0.1中不需要加r也不需要加^
    path('xadmin/', xadmin.site.urls),
    # TemplateView.as_view会将template转换为view
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('login/', LoginView.as_view(), name="user_login")
]
