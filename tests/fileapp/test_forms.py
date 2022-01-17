from django.test import TestCase

from fileapp.forms import UploadForm


class TestUploadForm(TestCase):
    def test_init(self):
        form = UploadForm()

        assert form.fields['uploaded_file'].required is True
        assert form.fields['parse_type'].required is True
