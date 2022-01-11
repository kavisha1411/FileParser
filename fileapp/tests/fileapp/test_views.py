from ..models import BookingData, Upload
import pytest
from faker import Factory
from .factories import BookingDataFactory, UploadFactory
from ..views import get_last_modified_file
from fileParser.settings import BASE_DIR


def get_dummy_file(self):
    latest_file = get_last_modified_file()
    num_of_lines = 20
    dummy_file = f'{BASE_DIR}/fileapp/uploads/files/tests/dummy.xlsx'
    with open(latest_file, 'r') as rfp:
        with open(dummy_file, 'w') as wfp:
            for i in range(num_of_lines):
                a_line = rfp.readline()
                wfp.write(a_line)


@pytest.mark.django_db
class TestParseNormally(object):
    def setup(self):
        self.booking_data = BookingDataFactory.create()
        self.url = reverse('parsenormal')

    def teardown(self):
        BookingData.objects.all().delete()

    def test_get(self, client):
        response = admin.get(self.url)
        assert response.status_code == 200


@pytest.mark.django_db
class TestParsePandas(object):
    def setup(self):
        self.booking_data = BookingDataFactory.create()
        self.url = reverse('parsepandas')

    def teardown(self):
        BookingData.objects.all().delete()

    # def test


@pytest.mark.django_db
class TestUpload(object):
    def setup(self):
        self.uploaded_file = UploadFactory.create()
        self.url = reverse('fileupload')

    def teardown(self):
        Upload.objects.all().delete()


@pytest.mark.django_db
class TestUpdate(object):
    def setup(self):
        self.booking_data = BookingDataFactory.create(0)
        self.url = reverse('fileupdate')

    def teardown(self):
        BookingData.objects.all().delete()




