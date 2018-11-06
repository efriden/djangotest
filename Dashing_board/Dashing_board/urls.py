"""
Definition of urls for Dashing_board.
"""

from django.conf.urls import include, url
import dash.urls

import TestApp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', Dashing_board.views.home, name='home'),
    # url(r'^Dashing_board/', include('Dashing_board.Dashing_board.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

	#url(r'^$', TestApp.views.index, name='index'),
	url(r'^home$', TestApp.views.index, name='home'),
	url(r'^dashboard/', include(dash.urls)),

	# django-dash stuff stolen from the docs
	# django-dash RSS contrib plugin URLs:
	url(r'^dash/contrib/plugins/rss-feed/',
    include('dash.contrib.plugins.rss_feed.urls')),

	# django-dash public dashboards contrib app:
	url(r'^', include('dash.contrib.apps.public_dashboard.urls')),
	
]
