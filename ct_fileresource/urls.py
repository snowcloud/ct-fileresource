from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('ct_fileresource.views',
    url(r'^$', 'fileresource_list', name="fileresource_list"),
    url(r'^(?P<object_id>[0-9A-Za-z]+)/$', 'fileresource_detail', name="fileresource_detail"),
)
