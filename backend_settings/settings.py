import django_heroku
import os

"""
Django settings for Fasd project.

Generated by 'django-admin startproject' using Django 2.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import pkg_resources as resources


def get_resource_address(resource_name, resource_package):
    """
    Get absolute address for `resource_name`
    :param str resource_name:
    :param str resource_package:
    :return: absolute path for accessing the resource file inside resources package
    """
    filepath = resources.resource_filename(resource_package, resource_name)
    return filepath


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@hke#wuhwlu5)&-1-5wcpk9tamn6b(u5_le(9+8bcg&7_)ga5s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'apps.registration',
    'apps.index',
    'apps.news',
    'apps.product',
    'apps.royan_admin',
    'apps.service',
    'apps.research',
    'apps.tutorial',
    'apps.order',
    'django_unused_media',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'backend_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'apps', 'temporary', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'registration', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'product', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'royan_admin', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'news', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'service', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'research', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'tutorial', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'order', 'templates'),
            os.path.join(BASE_DIR, 'apps', 'index', 'templates'),
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'backend_settings.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Royan_Tokagene',
        'USER': 'Royan_Tokagene',
        'PASSWORD': 'royan_tokagene_royan',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/staticfiles/'
STATIC_ROOT = "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'front'),
]
LOGIN_REDIRECT_URL = '/login_success/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587

EMAIL_HOST_USER = 'tucagenesite'
EMAIL_HOST_PASSWORD = 'TuCAGenesite'
LOGIN_URL = '/login/'

if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

GOOGLE_RECAPTCHA_SECRET_KEY = '6LdRSRYUAAAAAOnk5yomm1dI9BmQkJWTg_wIlMJ_'
