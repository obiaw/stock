from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.dashboard,name='dashboard'),
    url(r'^asset/$',views.asset, name ='asset'),
    url(r'^logs/$', views.logs,name='logs'),
    url(r'^new_asset',views.new_asset,name='new_asset'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
]