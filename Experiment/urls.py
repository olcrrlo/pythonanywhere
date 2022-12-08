"""Experiment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from cogEx import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cogEx/', include('cogEx.urls')),
    path('ex01/', include('ex01.urls')),
    path('k102/', include('k102.urls')),

]
"""

urlpatterns = [
    url(r'^cogEx/$', views.index, name='index'),
    url(r'^cogEx/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^cogEx/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^cogEx/(?P<question_id>\d+)/results/$', views.results, name='results'),
    url(r'^admin', admin.site.urls),

]

"""