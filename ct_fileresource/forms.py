# forms.py

from django import forms
from django.contrib.contenttypes.models import ContentType

from ct_fileresource.models import FileResource

class FileResourceForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        model = FileResource
        # fields = ('first_name', 'last_name', 'email')

    def clean_content_type(self):
        data = self.cleaned_data['content_type']
        return ContentType.objects.get(pk=data)
