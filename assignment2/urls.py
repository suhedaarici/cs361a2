__author__ = 'suhedaarici'
from django.conf.urls import include, url
from django.conf.urls import url
from . import views

urlpatterns = patterns('',
    url(r'^$', include('assigment2.urls'))

)