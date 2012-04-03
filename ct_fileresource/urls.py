from django.conf.urls.defaults import url, patterns

urlpatterns = patterns('ct_fileresource.views',
    url(r'^$', 'fileresource_list', name="fileresource_list"),
    url(r'^(?P<object_id>[0-9A-Za-z]+)/$', 'fileresource_detail', name="fileresource_detail"),

    url(r'^groups/(?P<object_id>[0-9A-Za-z]+)/$', 'group_fileresource_list', name="group_fileresource_list"),
    url(r'^template/(?P<object_id>[0-9A-Za-z]+)/$', 'template_fileresource_list', name="template_fileresource_list"),

)
