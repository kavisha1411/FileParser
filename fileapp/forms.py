from django.db import forms
from .models import Upload


class UploadForm(forms.modelForm):
    class Meta:
        model = Upload
        fields = ('upload_file',)
