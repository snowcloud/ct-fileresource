# ct_fileresource/views.py

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from ct_fileresource.models import FileResource
from ct_groups.models import CTGroup
from ct_template.models import ClinTemplate

def fileresource_list(request, template_name='ct_fileresource/list.html'):

    objects = FileResource.objects.all()
    template_context = {'objects': objects}
    return render_to_response(template_name, RequestContext(request, template_context))


def fileresource_detail(request, object_id, template_name='ct_fileresource/detail.html'):
    object = FileResource.objects.get(pk=object_id)
    template_context = {'object': object}
    return render_to_response(template_name, RequestContext(request, template_context))


def group_fileresource_list(request, object_id, template_name='ct_fileresource/list.html'):
    obj = get_object_or_404(CTGroup, slug=object_id)
    objects = FileResource.group_resources.filter(object_id=obj.id)
    template_context = {'objects': objects}
    return render_to_response(template_name, RequestContext(request, template_context))

def template_fileresource_list(request, object_id, template_name='ct_fileresource/list.html'):
    obj = get_object_or_404(ClinTemplate, pk=object_id)
    objects = FileResource.template_resources.filter(object_id=obj.id)
    template_context = {'objects': objects}
    return render_to_response(template_name, RequestContext(request, template_context))


