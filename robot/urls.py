from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^timeline$', views.show_timeline, name='timeline'),
    url(r'^$', views.show_index, name='index')
]