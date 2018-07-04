"""babysleep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from Model import views as Model_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
	path(r'children/', Model_views.children, name='children'),
	path(r'login/', Model_views.login,name='login'),
	path(r'forgetpassword/', Model_views.forgetpassword, name='forgetpassword'),
	path(r'registration/', Model_views.registration, name='registration'),
	path(r'about-me/', Model_views.about_me, name='about-me'),
	path(r'collection/', Model_views.collection, name='collection'),
	path(r'main/', Model_views.main, name='main'),
	path(r'record/', Model_views.record, name='record'),
	path(r'recordadd/', Model_views.recordadd, name='recordadd'),
	path(r'recordedit/', Model_views.recordedit, name='recordedit'),
	path(r'setting/', Model_views.setting, name='setting'),
	path(r'todayplay/', Model_views.todayplay, name='todayplay'),
	path(r'update_resources/', Model_views.update_resources, name='update_resources'),
	path(r'channel_user/', Model_views.channel_user, name='channel_user'),
	url(r'^$', Model_views.index,name='login'),
]
urlpatterns += staticfiles_urlpatterns()