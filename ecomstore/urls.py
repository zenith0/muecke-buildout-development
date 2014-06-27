from django.conf.urls import patterns, include
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecomstore.views.home', name='home'),
    # url(r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^', include('catalog.urls')),
    #(r'^catalog/$', 'templates.preview.views.home'),
    #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    #    'document_root': '/home/stefan/budterence/WebShop/code/WebShop/ecomstore/static'}),
    (r'^cart/', include('cart.urls')),

)

