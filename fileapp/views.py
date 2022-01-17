import logging
import csv
import decimal
import pandas as pd
from openpyxl import load_workbook

from django.shortcuts import render
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import UploadForm
from .models import BookingData, Upload
from .write_records import insert_xlsx_data, insert_csv_data, insert_csv_data_pandas, insert_xlsx_data_pandas
from .update_records import update_csv_data, update_xlsx_data
from .settings import (
    WRONG_FILE_TYPE,
    MSG_TYPE_SUCCESS,
    MSG_TYPE_WARNING,
    MSG_TYPE_WARNING_LIST,
    ERROR_MSG_GENERIC,
    ERROR_MSG_DB,
    UPLOAD_DIR,
)

logger = logging.getLogger('fileapp')


class FileParserView(View):
    template_name = 'fileapp/upload_form.html'

    def get(self, request):
        form = UploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        Upload.objects.all().delete()
        form = UploadForm(request.POST, request.FILES)

        uploaded_file = request.FILES.get('uploaded_file')
        if (not uploaded_file.name.endswith('.xlsx')) and (
            not uploaded_file.name.endswith('.csv')
        ):
            messages.error(request, WRONG_FILE_TYPE)
            logger.error(WRONG_FILE_TYPE)
            return HttpResponseRedirect(request.path_info)

        parse_type = request.POST.get('parse_type')
        if form.is_valid():
            form.save()

        msg, msg_type = self.file_parser(request, uploaded_file, parse_type)
        if msg_type == MSG_TYPE_SUCCESS:
            messages.success(request, msg)
            logger.info(msg)
        elif msg_type == MSG_TYPE_WARNING_LIST:
            for m in msg:
                messages.warning(request, m)
            logger.warning(msg)
        else:
            messages.warning(request, msg)
            logger.warning(msg)
        return HttpResponseRedirect(request.path_info)

    def file_parser(self, request, uploaded_file, parse_type):
        msg = ERROR_MSG_GENERIC
        msg_type = MSG_TYPE_WARNING
        if uploaded_file.name.endswith('xlsx') and parse_type == 'Parse Normally':
            msg, msg_type = insert_xlsx_data(uploaded_file)
        elif uploaded_file.name.endswith('csv') and parse_type == 'Parse Normally':
            msg, msg_type = insert_csv_data(uploaded_file)
        elif uploaded_file.name.endswith('xlsx') and parse_type == 'Parse with pandas':
            msg, msg_type = insert_xlsx_data_pandas(uploaded_file)
        else:
            msg, msg_type = insert_csv_data_pandas(uploaded_file)

        return msg, msg_type


class FileUpdateParserView(View):
    template_name = 'fileapp/update_form.html'

    def get(self, request):
        form = UploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # Upload.objects.all().delete()
        form = UploadForm(request.POST, request.FILES)

        uploaded_file = request.FILES.get('uploaded_file')
        if (not uploaded_file.name.endswith('.xlsx')) and (
                not uploaded_file.name.endswith('.csv')
        ):
            messages.error(request, WRONG_FILE_TYPE)
            logger.error(WRONG_FILE_TYPE)
            return HttpResponseRedirect(request.path_info)

        parse_type = request.POST.get('parse_type')
        if form.is_valid():
            form.save()

        msg, msg_type = self.file_updater(request, uploaded_file, parse_type)
        if msg_type == MSG_TYPE_SUCCESS:
            messages.success(request, msg)
            logger.info(msg)
        elif msg_type == MSG_TYPE_WARNING_LIST:
            for m in msg:
                messages.warning(request, m)
            logger.warning(msg)
        else:
            messages.warning(request, msg)
            logger.warning(msg)
        return HttpResponseRedirect(request.path_info)

    def file_updater(self, request, uploaded_file, parse_type):
        msg = ERROR_MSG_GENERIC
        msg_type = MSG_TYPE_WARNING
        if uploaded_file.name.endswith('xlsx'):
            msg, msg_type = update_xlsx_data(uploaded_file)
        else:
            msg, msg_type = update_csv_data(uploaded_file)

        return msg, msg_type


