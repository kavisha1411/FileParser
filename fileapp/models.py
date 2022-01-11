from django.db import models
from fileParser.settings import (
    PAYMENT_METHOD_CHOICES, STATUS_CHOICES, LANGUAGE_CHOICES,)
from django.utils.translation import gettext_lazy as _


class Upload(models.Model):
    upload_file = models.FileField()

    class Meta:
        db_table = 'upload_data'


class BookingData(models.Model):
    booking_id = models.BigIntegerField(_("booking_id"))
    code = models.CharField(_("code"), max_length=12)
    origin = models.CharField(_("origin"), max_length=10)
    property = models.CharField(_("property"), max_length=120)
    property_code = models.CharField(_("property_code"), max_length=50)
    arrival = models.DateField(_("arrival"))
    departure = models.DateField(_("departure"))
    accomodation = models.CharField(_("accomodation"), max_length=100)
    reservation_holder = models.CharField(_("reservation_holder"), max_length=60)
    reservation_total = models.DecimalField(_("reservation_total"), max_digits=8, default=0.00, decimal_places=2)
    tax = models.DecimalField(_("tax"), max_digits=8, default=0.00, decimal_places=2)
    currency = models.CharField(_("currency"), max_length=7)
    payment_method = models.CharField(_("payment_method"), choices=PAYMENT_METHOD_CHOICES, max_length=10)
    status = models.CharField(_("status"), choices=STATUS_CHOICES, max_length=10)
    date_of_creation = models.DateField(_("date_of_creation"))
    email = models.CharField(_("email"), max_length=50)
    phone = models.CharField(_("phone"), max_length=15, null=True, blank=True)
    country = models.CharField(_("country"), max_length=15, null=True, blank=True)
    language = models.CharField(_("language"), choices=LANGUAGE_CHOICES, max_length=5)
    address = models.CharField(_("address"), max_length=100, null=True, blank=True)
    zipcode = models.CharField(_("zipcode"), max_length=8, null=True, blank=True)
    city = models.CharField(_("city"), max_length=30, null=True, blank=True)
    access_code = models.CharField(_("access_code"), max_length=10, null=True, blank=True)
    b2b_discount = models.CharField(_("b2b_discount"), max_length=10, null=True, blank=True)
    rooming_info = models.TextField(_("rooming_info"), max_length=300, null=True, blank=True)
    deposit = models.DecimalField(_("deposit"), max_digits=8, default=0.00, decimal_places=2)
    rate_plan_name = models.CharField(_("rate_plan_name"), max_length=100)

    class Meta:
        db_table = 'booking_data'
        verbose_name = _('Booking Data')
        verbose_name_plural = _('Booking Data')
