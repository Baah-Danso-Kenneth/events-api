<<<<<<< HEAD
from email.policy import default
from pathlib import Path
import os
from dotenv import load_dotenv

from django.conf.global_settings import MEDIA_URL, MEDIA_ROOT, AUTH_USER_MODEL
=======

import os.path
from pathlib import Path
from dotenv import  load_dotenv

from django.conf.global_settings import MEDIA_ROOT, AUTH_USER_MODEL

load_dotenv()

ENV = os.environ.get("ENV")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
>>>>>>> e027666 (Prep project with new apps)

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv()

<<<<<<< HEAD
ENV = os.environ.get("ENV")

SECRET_KEY = os.environ.get("SECRET_KEY", default="django-insecure-aminqra+yiq%c-3wutdn4h02b59q3@=vl-ck!!xbo)ntx($wkw")

=======
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
>>>>>>> e027666 (Prep project with new apps)
DEBUG = False if ENV == "PROD" else True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")

<<<<<<< HEAD
=======

# Application definition

>>>>>>> e027666 (Prep project with new apps)
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

<<<<<<< HEAD
THIRD_PARTY_APPS = [
  'rest_framework'
]

LOCAL_APPS = [
  'core.events',
  'core.profiles',
  'core.users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

=======
LOCAL_APPS = [
    "apps.events",
    "apps.users"
]

THIRD_PARTY_APPS = [
   "rest_framework"
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS
>>>>>>> e027666 (Prep project with new apps)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coreRoot.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'coreRoot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/ "media"

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

<<<<<<< HEAD
AUTH_USER_MODEL = "users.User"
=======
AUTH_USER_MODEL = "users.User"
>>>>>>> e027666 (Prep project with new apps)
