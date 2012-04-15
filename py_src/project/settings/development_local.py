from project.settings.development import *

IS_DEV_SERVER = True
CACHE_BACKEND = 'locmem://'

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.sqlite3',
       'HOST': '',
       'NAME': 'matinfo-site.db.sqlite3',
       'USER': '',
       'PASSWORD': '',
   },
}

SEKIZAI_IGNORE_VALIDATION = True
