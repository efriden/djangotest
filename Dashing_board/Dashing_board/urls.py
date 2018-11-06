"""
Definition of urls for Dashing_board.
"""

from django.conf.urls import include, url
from TestApp.widgets import Weather
from dashing.utils import router

import TestApp.views

#router.register(Weather, 'weather_widget')
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

	url(r'^$', include(router.urls)),

	url(r'^weather/$', Weather.as_view(), name='weather_widget'),

	#url(r'^index$', TestApp.views.index, name='index'),
	
]
