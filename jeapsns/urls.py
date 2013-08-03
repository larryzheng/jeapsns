from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from jeapsns.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jeapsns.views.home', name='home'),
    # url(r'^jeapsns/', include('jeapsns.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url(r'^hello/$', hello),		
     url(r'^index_temp/([a-z]{1,10})$',index_temp), 	 	
     url(r'^index_temp_file/(\d{1,6})$',index_temp_file), 	
)
