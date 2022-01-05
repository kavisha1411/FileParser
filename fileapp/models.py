from django.db import models
from fileParser.settings import (
    PAYMENT_METHOD_CHOICES, STATUS_CHOICES, LANGUAGE_CHOICES,)
from django.utils.translation import gettext_lazy as _


class Upload(models.Model):
    upload_file = models.FileField()

    class Meta:
        db_table = 'upload_data'


class BookingData(models.Model):
    booking_id = models.BigIntegerField()
    code = models.CharField(max_length=12)
    origin = models.CharField(max_length=10)
    property = models.CharField(max_length=120)
    property_code = models.CharField(max_length=50)
    arrival = models.DateField(auto_now=True)
    departure = models.DateField(auto_now=True)
    accomodation = models.CharField(max_length=100)
    reservation_holder = models.CharField(max_length=60)
    reservation_total = models.DecimalField(max_digits=8, default=0.00, decimal_places=2)
    tax = models.DecimalField(max_digits=8, default=0.00, decimal_places=2)
    currency = models.CharField(max_length=7)
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    date_of_creation = models.DateField(auto_now=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=5)
    address = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=8, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    access_code = models.CharField(max_length=10, null=True, blank=True)
    b2b_discount = models.CharField(max_length=10, null=True, blank=True)
    rooming_info = models.TextField(max_length=300, null=True, blank=True)
    deposit = models.DecimalField(max_digits=8, default=0.00, decimal_places=2)
    rate_plan_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'booking_data'
        verbose_name = _('Booking Data')
        verbose_name_plural = _('Booking Data')