import time
import os
import stat
import csv
import pandas as pd
from datetime import datetime
from django.shortcuts import render
from .models import BookingData, Upload
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from rest_framework.views import APIView
from openpyxl import load_workbook
from django.db import transaction
from datetime import date
import decimal


def get_last_modified_file():
    last_modified_time = datetime.strptime("Mon Nov  1 09:15:32 2000", '%a %b %d %H:%M:%S %Y')
    file_list = os.listdir('/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/')
    # Loop to get latest modified file to upload to database
    for file in file_list:
        if file[-4:] == 'xlsx' or file[-4:] == '.csv':
            file_stats = os.stat(f'/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/{file}')
            modified_time = datetime.strptime(time.ctime(file_stats[stat.ST_MTIME]), '%a %b %d %H:%M:%S %Y')
            if modified_time > last_modified_time:
                last_modified_time = modified_time
                filename = file
    return filename


class UploadView(CreateView):
    model = Upload
    fields = ['upload_file', ]
    success_url = reverse_lazy('fileupload')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documents'] = Upload.objects.all()
        return context


class ParseNormally(APIView):
    model = BookingData
    fields = '__all__'

    def get(self, request, format=None):
        filename = get_last_modified_file()
        path = f'/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/{filename}'
        BookingData.objects.all().delete()
        row_array = []

        if filename[-4:] == 'xlsx':
            workbook = load_workbook(path)
            xlsxfile = workbook.active
            for row in xlsxfile.iter_rows(min_row=2):
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
            with transaction.atomic():
                BookingData.objects.bulk_create(row_array)
            return render(request, template_name='parse_file_xlsx.html')

        elif filename[-4:] == '.csv':
            csvfile = open(path)
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                row_array.append(BookingData(booking_id=row[0], code=row[1],
                                             origin=row[2], property=row[3],
                                             property_code=row[4], arrival=row[5],
                                             departure=row[6], accomodation=row[7],
                                             reservation_holder=row[8], reservation_total=row[9],
                                             tax=row[10], currency=row[11], payment_method=row[12],
                                             status=row[13], date_of_creation=row[14],
                                             email=row[15], phone=row[16], country=row[17],
                                             language=row[18], address=row[19], zipcode=row[20],
                                             city=row[21], access_code=row[22], b2b_discount=row[23],
                                             rooming_info=row[24], deposit=row[25],
                                             rate_plan_name=row[26]))
            with transaction.atomic():
                BookingData.objects.bulk_create(row_array)
            return render(request, template_name='parse_file_csv.html')


class ParsePandas(APIView):
    model = BookingData
    fields = '__all__'

    def get(self, request, format=None):
        file_list = os.listdir('/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/')

        csvfiles = [file for file in file_list if file[-4:] == '.csv']
        path = f'/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/{csvfiles[0]}'
        df = pd.read_csv(path, index_col=0)

        excelfiles = [file for file in file_list if file[-4:] == 'xlsx']
        path = f'/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/{excelfiles[0]}'
        df = pd.read_excel(path, index_col=0)

        return render(request, template_name='parse_file_success.html')


class UpdateFile(APIView):
    model = BookingData

    def is_new_row(self, row, old_data, file_extension):
        if file_extension == 'xlsx':
            for old_row in old_data:
                if row[0].value == old_row.booking_id:
                    return False

        for old_row in old_data:
            if row[0] == old_row.booking_id:
                return False

    def data_is_modified(self, row, old_data, file_extension):
        fields = [field.name for field in BookingData._meta.fields]
        changed_fields = {}
        changed_booking_id = 0
        changed = 0

        if file_extension == 'xlsx':
            for old_row in old_data:
                booking_id = getattr(old_row, 'booking_id')
                if row[0].value == booking_id:
                    for index in range(0, 26):
                        attribute = fields[index+1]
                        value = getattr(old_row, attribute)
                        if row[index].value != value:
                            if (isinstance(row[index].value, int)) and (int(value) == row[index].value):
                                continue
                            elif (isinstance(row[index].value, str)) and (row[index].value == str(value)):
                                continue
                            elif (isinstance(row[index].value, datetime)) and (row[index].value.date() == value):
                                continue
                            else:
                                changed_booking_id = getattr(old_row, 'booking_id')
                                changed_fields[attribute] = row[index].value
                                changed = 1

        else:
            for old_row in old_data:
                booking_id = getattr(old_row, 'booking_id')
                if int(row[0]) == booking_id:
                    for index in range(0, 26):
                        attribute = fields[index + 1]
                        value = getattr(old_row, attribute)
                        if row[index] != value:
                            if (isinstance(row[index], int)) and (int(value) == row[index]):
                                continue
                            elif isinstance(value, date):
                                valid_date = datetime.strptime(row[index], "%m/%d/%Y")
                                if valid_date.date() == value:
                                    continue
                            elif isinstance(row[index], str):
                                if isinstance(value, int) and row[index] == str(value):
                                    continue
                                elif isinstance(value, decimal.Decimal) and row[index] == str(value):
                                    continue
                            else:
                                changed_booking_id = getattr(old_row, 'booking_id')
                                changed_fields[attribute] = row[index]
                                changed = 1

        return changed, changed_booking_id, changed_fields

    def get(self, request, format=None):
        filename = get_last_modified_file()
        path = f'/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/{filename}'
        row_array = []
        old_data = BookingData.objects.all()
        file_extension = filename[-4:]

        if file_extension == 'xlsx':
            workbook = load_workbook(path)
            xlsxfile = workbook.active
            for row in xlsxfile.iter_rows(min_row=2):
                if UpdateFile.is_new_row(self, row, old_data, file_extension):
                    row_array.append(row)
                else:
                    is_data_modified, booking_id, modified_fields = UpdateFile.data_is_modified(
                                                                        self, row, old_data, file_extension)
                    if is_data_modified:
                        BookingData.objects.filter(booking_id=booking_id).update(**modified_fields)
                    else:
                        continue
            if row_array:
                with transaction.atomic():
                    BookingData.objects.bulk_create(row_array)

        elif file_extension == '.csv':
            csvfile = open(path)
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                if UpdateFile.is_new_row(self, row, old_data, file_extension):
                    row_array.append(row)
                else:
                    is_data_modified, booking_id, modified_fields = UpdateFile.data_is_modified(
                        self, row, old_data, file_extension)
                    print(is_data_modified, booking_id, modified_fields)
                    if is_data_modified:
                        BookingData.objects.filter(booking_id=booking_id).update(**modified_fields)
                    else:
                        continue
            if row_array:
                with transaction.atomic():
                    BookingData.objects.bulk_create(row_array)

        return render(request, template_name='parse_file_success.html')
