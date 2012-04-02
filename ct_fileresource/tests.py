"""
Tests for ct-fileresource
"""

from django.db import models
from django.test import TestCase
from ct_fileresource.models import FileResource

class Dummy(models.Model):
    """docstring for Dummy"""
    name = models.CharField(max_length=100)     

class ResourceFileTestBase(TestCase):
    def setUp(self):
        self.dummy = Dummy(name='emma dummy')
        self.dummy.save()

class ResourceFileUnitTest(ResourceFileTestBase):

    def test_models(self):
        """
        
        """

        f = FileResource(name='blah', description='blahblah')
        f.attached_to = self.dummy
        f.save()
        self.assertEqual(1, FileResource.objects.count())
        f = FileResource.objects.get(name='blah')
        self.assertEqual('blahblah', f.description)
        self.assertEqual('emma dummy', f.attached_to.name)

        from django.core.files.base import ContentFile
        myfile = ContentFile("hello world")
        f.resource.save('testfile.txt', myfile)

        f.resource.delete()
    
class ViewsTestCase(ResourceFileTestBase):

    def test_views(self):
        pass




