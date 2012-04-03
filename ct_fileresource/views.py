# ct_fileresource/views.py

from django.conf import settings
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _

from ct_fileresource.models import FileResource
from ct_fileresource.forms import FileResourceForm
from ct_framework.forms import ConfirmForm
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

def template_fileresource_add(request, object_id, next=None, template_name='ct_fileresource/add.html'):
    # next = request.REQUEST.get('next', reverse('fileresource_list'))
    next = next or '%s?tView=files' % reverse('template-detail',kwargs={'object_id':object_id})
    obj = get_object_or_404(ClinTemplate, pk=object_id)
    if request.method == 'POST':
        result = request.POST.get('result')
        if result == _('Cancel'):
            return HttpResponseRedirect(next)
        form = FileResourceForm(request.POST, request.FILES)
        if form.is_valid():
            fr = form.save()
            messages.success(request, _('Your changes were saved.'))
            return HttpResponseRedirect(next)
    else:
        form = FileResourceForm(initial={'content_type': ContentType.objects.get_for_model(obj).id, 'object_id': obj.id})

    template_context = {'form': form}
    return render_to_response(template_name, RequestContext(request, template_context))

def template_fileresource_edit(request, object_id, next=None, template_name='ct_fileresource/add.html'):
    # next = request.REQUEST.get('next', reverse('fileresource_list'))
    obj = get_object_or_404(FileResource, pk=object_id)
    next = next or '%s?tView=files' % reverse('template-detail',kwargs={'object_id':obj.attached_to.id})
    if request.method == 'POST':
        result = request.POST.get('result')
        if result == _('Cancel'):
            return HttpResponseRedirect(next)
        form = FileResourceForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            fr = form.save()
            messages.success(request, _('Your changes were saved.'))
            return HttpResponseRedirect(next)
    else:
        form = FileResourceForm(instance=obj)

    template_context = {'form': form}
    return render_to_response(template_name, RequestContext(request, template_context))

def template_fileresource_delete(request, object_id, next=None):
    obj = get_object_or_404(FileResource, pk=object_id)
    next = next or '%s?tView=files' % reverse('template-detail',kwargs={'object_id':obj.attached_to.id})

    if request.POST:
        if request.POST['result'] == _('Cancel'):
            return HttpResponseRedirect(next)
        else:
            form = ConfirmForm(request.POST)
            if form.is_valid():
                obj.delete()
                return HttpResponseRedirect(next)
    else:
        form = ConfirmForm(initial={ 'resource_name': obj.name })
    return render_to_response('ct_framework/confirm.html', 
        RequestContext( request, 
            {   'form': form,
                'title': _('Delete this file?')
            })
        )


