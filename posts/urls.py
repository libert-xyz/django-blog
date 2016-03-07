from django.conf.urls import url
from django.contrib import admin


from views import *

urlpatterns = [

    url(r'^$', post_list),
    url(r'^create/$', post_create),
    url(r'^(?P<pk>\d+)/$', post_detail,name='detail'),
    url(r'^list/$', post_list),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]
