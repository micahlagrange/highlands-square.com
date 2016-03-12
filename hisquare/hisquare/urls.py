from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

import home.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hisquare.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hisquare/', include(home.urls, namespace='home')),
    
    # Angular GET urls
    url(r'^get/categories/$', home.views.get_all_categories),
    url(r'^get/events/$', home.views.get_all_events),
    url(r'^get/about/$', home.views.get_about_page),
    url(r'^get/merchants/(?P<catcode>[-_\w]+)/$', home.views.get_merchants_by_category),
    url(r'^get/merchant/(?P<m_id>\d+)/$', home.views.get_merchant_by_id),
    
    # Angular templates
    url(r'^pages/events/$', TemplateView.as_view(template_name="angularTemplates/events.html")),
    url(r'^pages/about/$', TemplateView.as_view(template_name="angularTemplates/about.html")),
    url(r'^pages/merchants/$', TemplateView.as_view(template_name="angularTemplates/merchants.html")),
    url(r'^pages/details/$', TemplateView.as_view(template_name="angularTemplates/details.html")),
    
    # Redirect
    url(r'^$', home.views.index, name='index'),
    
    # Admin Urls
    url(r'^hsma-admin/', include(admin.site.urls)),
)


# Below only works in dev server
from django.conf.urls.static import static
from hisquare import settings
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
