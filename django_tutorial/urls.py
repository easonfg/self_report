
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.get_name, name='index'),
    url(r'^manage/$', views.manage_articles, name='manage'),
    #url(r'^edit/$', views.post_new, name='edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^dynamic/$', views.dynamic_js, name='dynamic_js'),
]
