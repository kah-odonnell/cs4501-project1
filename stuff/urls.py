from django.conf.urls import patterns, include, url
from django.contrib import admin
from helloworld import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'stuff.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
)
