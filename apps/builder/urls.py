from __future__ import unicode_literals

from django.conf.urls import patterns, url

from . import views


urlpatterns = [
    url(r'home$', views.create_api, name='create-api-home'),
]
