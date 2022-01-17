import pytest
from django.test import Client
from django.urls import reverse
from faker import Factory
from fileapp.models import BookingData, Upload
from fileParser.settings import BASE_DIR
from datetime import date
from fileapp.settings import (
    MSG_TYPE_SUCCESS,
    MSG_TYPE_WARNING,
    WRONG_FILE_TYPE,
    MSG_TYPE_ERROR,
)
import pandas as pd
from datetime import datetime, date
from openpyxl import load_workbook


@pytest.mark.django_db
class TestFileParserView(object):
    TEST_DIR = str(BASE_DIR) + '/fileapp/uploads/test_files/'
    sample_xlsx_file = TEST_DIR + 'dummy_test.xlsx'
    sample_xlsx_file_2 = TEST_DIR + 'dummy_test_2.xlsx'
    sample_csv_file = TEST_DIR + 'dummy_test.csv'
    sample_csv_file_2 = TEST_DIR + 'dummy_test_2.csv'
    sample_wrong_file = TEST_DIR + 'image.jpg'
    date_uploaded = date(2022, 1, 1)

    def setup(self):
        self.client = Client()
        self.url = reverse('fileupload')

    def test_get(self):
        response = self.client.get(self.url)
        assert 'fileapp/upload_form.html' in (t.name for t in response.templates)
        assert response.status_code == 200

    def test_post_xlsx_file(self):
        with open(self.sample_xlsx_file, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_SUCCESS
            xlsx_file.close()

    def test_post_csv_file(self):
        with open(self.sample_csv_file, "rb") as csv_file:
            data = {
                'uploaded_file': csv_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_SUCCESS
            csv_file.close()

    def test_post_wrong_file(self):
        with open(self.sample_wrong_file, "rb") as image_file:
            data = {
                'uploaded_file': image_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_ERROR
            assert message.message == WRONG_FILE_TYPE
            image_file.close()

    def test_xlsx_wrong_date(self):
        with open(self.sample_xlsx_file_2, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_WARNING
            xlsx_file.close()

    def test_csv_wrong_date(self):
        with open(self.sample_csv_file_2, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_WARNING
            xlsx_file.close()

    def test_xlsx_parse_pandas(self):
        with open(self.sample_xlsx_file, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse with pandas'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_SUCCESS
            xlsx_file.close()

    def test_csv_parse_pandas(self):
        with open(self.sample_csv_file, "rb") as csv_file:
            data = {
                'uploaded_file': csv_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse with pandas'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_SUCCESS
            csv_file.close()


@pytest.mark.django_db
class TestFileUpdateParserView(object):
    TEST_DIR = str(BASE_DIR) + '/fileapp/uploads/test_files/'
    sample_xlsx_file = TEST_DIR + 'dummy_test.xlsx'
    sample_xlsx_file_2 = TEST_DIR + 'dummy_test_2.xlsx'
    sample_csv_file = TEST_DIR + 'dummy_test.csv'
    sample_csv_file_2 = TEST_DIR + 'dummy_test_2.csv'
    sample_wrong_file = TEST_DIR + 'image.jpg'
    date_uploaded = date(2022, 1, 1)

    def setup(self):
        self.client = Client()
        self.url = reverse('fileupdate')

    def test_get(self):
        response = self.client.get(self.url)
        assert 'fileapp/update_form.html' in (t.name for t in response.templates)
        assert response.status_code == 200

    def test_post_xlsx_file(self):
        with open(self.sample_xlsx_file, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_SUCCESS
            xlsx_file.close()

    def test_post_csv_file(self):
        with open(self.sample_csv_file, "rb") as csv_file:
            data = {
                'uploaded_file': csv_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_SUCCESS
            csv_file.close()

    def test_post_wrong_file(self):
        with open(self.sample_wrong_file, "rb") as image_file:
            data = {
                'uploaded_file': image_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_ERROR
            assert message.message == WRONG_FILE_TYPE
            image_file.close()

    def test_xlsx_wrong_date(self):
        with open(self.sample_xlsx_file_2, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_WARNING
            xlsx_file.close()

    def test_csv_wrong_date(self):
        with open(self.sample_csv_file_2, "rb") as xlsx_file:
            data = {
                'uploaded_file': xlsx_file,
                'date_uploaded': self.date_uploaded,
                'parse_type': 'Parse Normally'
            }
            response = self.client.post(self.url, data=data, follow=True)
            assert response.status_code == 200
            message = list(response.context.get('messages'))[0]
            assert message.tags == MSG_TYPE_WARNING
            xlsx_file.close()
