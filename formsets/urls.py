
from django.conf.urls import include, url
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    #url(r'^$', views.dynamic_js, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'thanks$', TemplateView.as_view(template_name='formsets/thanks.html')),
]
