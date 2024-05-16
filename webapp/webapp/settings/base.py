"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/

*These settings are the base for all other settings. Variables declared here
may be overidden by the importing file.*
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from utils.paths import ensure_dir

load_dotenv('../.env', override=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
AUTH_USER_MODEL = 'home.User'

# Site paths and URLs
HOSTNAME = '127.0.0.1:5000'
GALAXY_SITE_NAME = 'Media'  # Rendered as "Galaxy <GALAXY_SITE_NAME>"
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'webapp/static'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'webapp/media'
LOG_ROOT = ensure_dir(BASE_DIR / 'webapp/logs')
RECIPIENT_MASTER_CSV = BASE_DIR / '../scripts/mail/recipient_records.csv'

# Hostnames
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

# Application definition

INSTALLED_APPS = [
    'django_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_recaptcha',
    'home',
    'news',
    'events',
    'people',
    'django_cleanup.apps.CleanupConfig',
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

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.settings'
            ],
        },
    },
]

WSGI_APPLICATION = 'webapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['MAIL_HOSTNAME']
EMAIL_PORT = os.environ['MAIL_SMTP_PORT']
EMAIL_HOST_USER = os.environ.get('MAIL_SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.environ.get('MAIL_SMTP_PASSWORD')
EMAIL_USE_TLS = os.environ.get('MAIL_USE_TLS').lower() in ('1', 'true')
EMAIL_FROM_ADDRESS = os.environ['MAIL_FROM_ADDRESS']
EMAIL_TO_ADDRESS = os.environ['MAIL_TO_ADDRESS']
SERVER_EMAIL = os.environ['MAIL_FROM_ADDRESS']
EMAIL_SUBJECT_PREFIX = os.getenv('EMAIL_SUBJECT_PREFIX', 'GMS: ')

# Validating whether submitted email is valid Galaxy AU account
MOCK_GALAXY_INTERACTIONS = (
    os.environ.get('MOCK_GALAXY_INTERACTIONS')
    in ('1', 'true')
)
if MOCK_GALAXY_INTERACTIONS:
    print("MOCK_GALAXY_INTERACTIONS is set: mocking galaxy interactions")

# Galaxy API auth
GALAXY_URL = os.environ.get('GALAXY_URL')
GALAXY_API_KEY = os.environ.get('GALAXY_API_KEY')

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Australia/Brisbane'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Random bits
LOGOUT_REDIRECT_URL = '/'
