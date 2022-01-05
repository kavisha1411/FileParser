from django.shortcuts import render
from .models import BookingData, Upload
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from openpyxl import load_workbook
# from rest_framework.parsers import MultiPartParser
from django.db import transaction
import time
import os
import stat


class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context


class ParseExcel(APIView):
    model = BookingData
    fields = '__all__'

    def get(self, request, format=None):
        filename = ''
        latest_time = ''
        file_list = os.listdir('/home/kavisha/PycharmProjects/pythonProject/fileParser/')

        # Loop to get latest modified file to upload to database
        for file in file_list:
            if file[-4:] == 'xlsx' or file[-4:] == '.csv':
                f = os.stat(f'/home/kavisha/PycharmProjects/pythonProject/fileParser/{file}')
                modified_time = time.ctime(f[stat.ST_MTIME])
                if modified_time > latest_time:
                    latest_time = modified_time
                    filename = file

        path = f'/home/kavisha/PycharmProjects/pythonProject/fileParser/{filename}'
        workbook = load_workbook(path)
        file_pointer = workbook.active
        row_array = []
        for row in file_pointer.iter_rows(min_row=2):
            row_array.append(BookingData(booking_id=row[0].value, code=row[1].value,
                                         origin=row[2].value, property=row[3].value,
                                         property_code=row[4].value, arrival=row[5].value,
                                         departure=row[6].value, accomodation=row[7].value,
                                         reservation_holder=row[8].value, reservation_total=row[9].value,
                                         tax=row[10].value, currency=row[11].value, payment_method=row[12].value,
                                         status=row[13].value, date_of_creation=row[14].value,
                                         email=row[15].value, phone=row[16].value, country=row[17].value,
                                         language=row[18].value, address=row[19].value, zipcode=row[20].value,
                                         city=row[21].value, access_code=row[22].value, b2b_discount=row[23].value,
                                         rooming_info=row[24].value, deposit=row[25].value,
                                         rate_plan_name=row[26].value))
        BookingData.objects.all().delete()
        with transaction.atomic():
            BookingData.objects.bulk_create(row_array)
            return render(request, template_name='parse_file.html')
