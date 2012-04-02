# ct_fileresource/views.py

from django.shortcuts import render_to_response
from django.template import RequestContext

from ct_fileresource.models import FileResource

def fileresource_list(request, template_name='ct_fileresource/list.html'):

    objects = FileResource.objects.all()
    template_context = {'objects': objects}
    return render_to_response(template_name, RequestContext(request, template_context))


def fileresource_detail(request, object_id, template_name='ct_fileresource/detail.html'):
    object = FileResource.objects.get(pk=object_id)
    template_context = {'object': object}
    return render_to_response(template_name, RequestContext(request, template_context))
