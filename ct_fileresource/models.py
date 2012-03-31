# ct_fileresource/models.py

from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FileResource(models.Model):
    """docstring for FileResource"""
    name = models.CharField(_('name'), max_length=100)
    description = models.CharField(_('description'), max_length=250)
    resource = models.FileField(upload_to='groups')
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    attached_to = generic.GenericForeignKey('content_type', 'object_id')


        