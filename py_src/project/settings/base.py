# -*- coding: utf-8 -*-
#from base_i18n import *
#from base_cms import *
from base_zinnia import *
import os

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False

TEMPLATE_DEBUG = DEBUG
IS_DEV_SERVER = False
IS_HTTP_SERVER = False
PREPEND_WWW = False
FORCE_SCRIPT_NAME = ''

USE_ETAGS = False

INTERNAL_IPS = ['127.0.0.1',]

ADMINS = [
    # ('Your Name', 'your_email@domain.com'),
]

PUBLIC_URLS = [
#    r'^admin/(.*)',
    r'^admin/image_filer/operations/upload/',
    r'^admin/filer/clipboard/operations/upload/',
]

MANAGERS = ADMINS

DATABASES = {
   'default': {
       'ENGINE': '',
       'HOST': '',
       'NAME': '',
       'USER': '',
       'PASSWORD': '',
       'PORT': '',
   },
}

TIME_ZONE = 'Europe/Zurich'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

USE_TZ = True # Django >= 1.4.0

PROJECT_DIR = os.path.abspath( os.path.join(os.path.dirname(__file__),'../') )

MEDIA_ROOT = os.path.join(PROJECT_DIR, '..', '..', 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_DIR, '..', '..', 'tmp', 'static')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = ''.join([STATIC_URL, 'admin/'])

SECRET_KEY = 'jkUUidfsfz5hgji789hkjHFD$drte@jhgJESD!bjh(rt+hfD'

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_DIR, "templates"),
]

INSTALLED_APPS = [
    # django core apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.comments',
    'django.contrib.admin',

    # 3rd party apps
    'appmedia',
    'easy_thumbnails',
    'filer',
    'login_as',
    'sekizai',
    'south',
    'crispy_forms',
#    'django_extensions',

    # custom apps
    'mptt',
    'tagging',
    'django_bitly',
    'django_xmlrpc',
    'ifactiveurl',
    'ajaxcomments',
    #'djcelery',
    #'ghettoq',
    #'monitor',
    'zinnia',
    'project',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.static",
    "sekizai.context_processors.sekizai",
    "zinnia.context_processors.version", # optional
]

THUMBNAIL_BASEDIR = 'tmp'
THUMBNAIL_QUALITY = 70
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
#    'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

SERVER_EMAIL = 'django@%s' % os.uname()[1]
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
TIME_FORMAT = 'H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j. F'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'login_as.auth_backend.LoginAsBackend',
]

SEKIZAI_IGNORE_VALIDATION = True

# djcelery
#OPERATION_TIMEOUT = 10
#RUN_INTERVAL = "*/5"

# monitor :: heck these sites to make sure the monitor itself is up
#CHECK_URLS = (
#    ('www.google.ch', '/'),
#    ('www.w3.org', '/'),
#    ('apache.org', '/')
#)
# if this many hosts of the above are down, we're down too
#CHECK_URL_THRESHOLD = 2

#CARROT_BACKEND = "ghettoq.taproot.Database"

#PUSH_NOTIFICATION_CREDENTIALS = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
