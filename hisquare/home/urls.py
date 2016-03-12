from django.conf.urls import patterns, url
import home.views

urlpatterns = patterns(
    '',
    url(r'^$', home.views.index, name='index'),
    url(r'^about/$', home.views.about, name='about'),
    url(r'^details/(?P<pk>\d+)/$', home.views.details, name='details'),
    url(r'^merchants/(?P<catcode>[-_\w]+)/$', home.views.category, name='category'),
    url(r'^events/$', home.views.events, name='events'),
   url(r'^street-fair-signup/$', home.views.sfform, name='sfform'),
)
