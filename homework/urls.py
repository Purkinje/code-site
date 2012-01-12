from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('homework.views',
    url(r'^$', 'weeks', name='weeks'),
    url(r'^(?P<week>[\w\d\-]+)/$', 'week', name='week'),
    url(r'^(?P<week>[\w\d\-]+)/(?P<hw>[\w\d\-]+)/$', 'hw', name='hw'),
)
