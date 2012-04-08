# ct_fileresource/models.py

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class GroupResourceManager(models.Manager):
    def get_query_set(self):
        obj_ct = ContentType.objects.get(app_label="ct_groups", model="ctgroup")
        return super(GroupResourceManager, self).get_query_set().filter(content_type__pk=obj_ct.id)

class TemplateResourceManager(models.Manager):
    def get_query_set(self):
        obj_ct = ContentType.objects.get(app_label="ct_template", model="clintemplate")
        return super(TemplateResourceManager, self).get_query_set().filter(content_type__pk=obj_ct.id)

def _upload_path(instance, filename):
    return 'fileresources/%s/%s/%s' % (instance.content_type.model, instance.id, filename)

class FileResource(models.Model):
    """docstring for FileResource"""
    name = models.CharField(_('name'), max_length=100)
    description = models.TextField(_('description'))
    resource = models.FileField(upload_to=_upload_path)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey('content_type', 'object_id')

    objects = models.Manager()
    group_resources = GroupResourceManager()
    template_resources = TemplateResourceManager()

    def __unicode__(self):
        return u'%s' % self.name

    def path(self):
        return 'files/%s' % self.content_type.model
