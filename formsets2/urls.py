
from django.conf.urls import include, url
from . import views

urlpatterns = [
    #url(r'^$', views.dynamic_js, name='index'),
    url(r'^$', views.some_view, name='index'),
]
