__author__ = 'UTURNMI'

from django.conf.urls import patterns, url
import home.views

urlpatterns = patterns(
    '',
    url(r'^$', home.views.index, name='index'),
    url(r'^about/$', home.views.about, name='about'),
    url(r'^details/(?P<pk>\d+)/$', home.views.details, name='details'),
    url(r'^merchants/(?P<catname>\w+)/$', home.views.category, name='category'),
    url(r'^events/$', home.views.events, name='events'),
)