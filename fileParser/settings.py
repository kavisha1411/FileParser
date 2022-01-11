"""
Django settings for fileParser project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from django.utils.translation import gettext_lazy as _
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&zy$k%ioa2uk!r&@^3j0&@bmss1682fizh_v*i*)ze^xxt@lh^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fileapp.apps.FileappConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fileParser.urls'

SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
        'DIRS': ['/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/templates/fileapp',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'fileParser.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fileops',
        'USER': 'kavishag',
        'PASSWORD': 'kavishag',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
MEDIA_ROOT = '/home/kavisha/PycharmProjects/pythonProject/fileParser/fileapp/uploads/files/'
MEDIA_URL = 'media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

PAYMENT_METHOD_BANK = 'bank'
PAYMENT_METHOD_CC = 'cc'
PAYMENT_METHOD_FAX = 'fax'

PAYMENT_METHOD_CHOICES = (
    (PAYMENT_METHOD_BANK, _('bank')),
    (PAYMENT_METHOD_CC, _('cc')),
    (PAYMENT_METHOD_FAX, _('fax')),
)

STATUS_CANCELLED = 'Cancelled'
STATUS_OK = 'OK'
STATUS_ON_HOLD = 'On hold'

STATUS_CHOICES = (
    (STATUS_CANCELLED, _('Cancelled')),
    (STATUS_OK, _('OK')),
    (STATUS_ON_HOLD, _('On hold')),
)

LANGUAGE_CODE_DE = 'DE'
LANGUAGE_CODE_EN = 'EN'
LANGUAGE_CODE_ES = 'ES'
LANGUAGE_CODE_FI = 'FI'
LANGUAGE_CODE_FR = 'FR'
LANGUAGE_CODE_HU = 'HU'
LANGUAGE_CODE_IT = 'IT'
LANGUAGE_CODE_NL = 'NL'
LANGUAGE_CODE_PL = 'PL'
LANGUAGE_CODE_RU = 'RU'

LANGUAGE_CHOICES = (
    (LANGUAGE_CODE_DE, _('DE')),
    (LANGUAGE_CODE_EN, _('EN')),
    (LANGUAGE_CODE_ES, _('ES')),
    (LANGUAGE_CODE_FI, _('FI')),
    (LANGUAGE_CODE_FR, _('FR')),
    (LANGUAGE_CODE_HU, _('HU')),
    (LANGUAGE_CODE_IT, _('IT')),
    (LANGUAGE_CODE_NL, _('NL')),
    (LANGUAGE_CODE_PL, _('PL')),
    (LANGUAGE_CODE_RU, _('RU')),
)
