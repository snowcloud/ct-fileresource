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

    def setUp(self):
        super(ViewsTestCase, self).setUp()

        from django.test.client import Client

        self.client = Client()

        self.fr1 = FileResource(name='resource one', description='blahblah one')
        self.fr1.attached_to = self.dummy
        self.fr1.save()
        self.fr2 = FileResource(name='resource two', description='blahblah two')
        self.fr2.attached_to = self.dummy
        self.fr2.save()


    def test_no_files(self):

        from django.core.urlresolvers import reverse

        # response = self.client.get(reverse('fileresource_list'))
        # self.assertEqual(response.status_code, 302)

        # self.client.login(username='bob', password='password')

        response = self.client.get(reverse('fileresource_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "list.html")

    def test_files(self):

        from django.core.urlresolvers import reverse

        # response = self.client.get(reverse('fileresource_list'))
        # self.assertEqual(response.status_code, 302)

        # self.client.login(username='bob', password='password')

        response = self.client.get(reverse('fileresource_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "resource one")
        self.assertContains(response, "resource two")






