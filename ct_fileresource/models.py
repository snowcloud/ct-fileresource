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

class FileResource(models.Model):
    """docstring for FileResource"""
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=450)
    resource = models.FileField(upload_to='groups')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey('content_type', 'object_id')

    objects = models.Manager()
    group_resources = GroupResourceManager()
    template_resources = TemplateResourceManager()

    def __unicode__(self):
        return u'%s' % self.name

