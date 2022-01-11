import factory
from factory.faker import faker
from fileParser.fileapp.models import BookingData, Upload
import pytest

fake = faker.Faker()

class BookingDataFactory(factory.django.DjangoModelFactory):
    booking_id = fake.ean(length=8)
    code = f'PH{booking_id}'
    origin = fake.company_suffix()
    property = fake.street_name()
    property_code = fake.password(length=32)
    arrival = fake.date()
    departure = fake.date()
    accomodation = fake.street_name()
    reservation_holder = fake.name()
    reservation_total = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    tax = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
    currency = fake.currency_code()
    payment_method = fake.word()
    status = fake.words(2)
    date_of_creation = fake.date()
    email = fake.email()
    phone = fake.msisdn()
    country = fake.country()
    language = fake.language_code()
    address = fake.street_address()
    zipcode = fake.postcode()
    city = fake.city()
    access_code = fake.word()
    b2b_discount = fake.pydecimal(left_digits=2, right_digits=2, positive=True)
    rooming_info = fake.address()
    deposit = fake.pydecimal(left_digits=3, right_digits=2, positive=True)
    rate_plan_name = fake.words(3)

    class Meta:
        model = BookingData


class UploadFactory(factory.django.DjangoModelFactory):
    upload_file = fake.file_name(extension = '.csv')

    class Meta:
        model = Upload
