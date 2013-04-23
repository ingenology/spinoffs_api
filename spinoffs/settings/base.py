# Django settings for spinoffs.
import os
from os.path import join, normpath, dirname
import dj_database_url

from datetime import date, timedelta

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_NAME = "Spinoffs API"
PROJECT_AUTHOR = "Ingenology"
PROJECT_SLUG = 'spinoffs'

# https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = (
    'spinoffs.ingenology.com',
)

here = lambda *x: join(normpath(dirname(__file__)), *x)
PROJECT_ROOT = normpath(here('..'))  # path to spinoffs
DJANGO_ROOT = normpath(here('..', '..'))  # path to dir that contains /spinoffs
rel = lambda * args: os.path.join(DJANGO_ROOT, *args)  # rel to DJANGO_ROOT

ADMINS = (
    ('Ingenology', 'dev@ingenology.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.config(),
}

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

TIME_INPUT_FORMATS = (
    '%I:%M%p', '%I:%M %p', '%H:%M:%S', '%H:%M'
)

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = rel('media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = rel('static_collected')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    rel('static'),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django_assets.finders.AssetsFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# django-assets will automatically look for assets.py files in each application,
# where you can register your bundles. If you want additional modules to be loaded,
# you can define this setting.
ASSETS_MODULES = [
    '{0}.assets'.format(PROJECT_SLUG),
]


# django storages
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_HEADERS = {
    'Expires': (date.today() + timedelta(days=30)).strftime("%a, %d %b %Y 20:00:00 GMT"),
}

if AWS_ACCESS_KEY_ID:
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
else:
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'


# thumbs
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE
THUMBNAIL_SUBDIR = "thumbs"
#THUMBNAIL_ALIASES = {
#    'appname': {
#        'size_name': {
#            'size': (250, 155),
#            'crop': True,
#        }
#    }
#}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    #'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'spinoffs.context_processors.constants',
)

CRISPY_TEMPLATE_PACK = 'bootstrap'

MIDDLEWARE_CLASSES = (
    'djunk_drawer.middleware.AuthSetsNoCacheHeadersMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'djunk_drawer.middleware.RequireLoginMiddleware',
)

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"


# For djunk_drawer.middleware.RequireLoginMiddleware:
LOGIN_REQUIRED_URLS = (
    r'/(.*)$',
)

LOGIN_REQUIRED_URLS_EXCEPTIONS = (
    r'/login(.*)$',
)

LOGIN_URL = "/login/"
LOGOUT_URL = "/logout/"
LOGIN_REDIRECT_URL = "/"

ROOT_URLCONF = '{0}.urls'.format(PROJECT_SLUG)

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{0}.wsgi.application'.format(PROJECT_SLUG)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    rel('templates'),
)

DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    'djunk_drawer',
    'crispy_forms',
    'django_assets',
    'django_tables2',
    'easy_thumbnails',
    'floppyforms',
    'gunicorn',
    'south',
    'storages',
    #'filer',
    'rest_framework',
)

PROJECT_APPS = (
    'archive',
    'facts',
    'users',
)

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Custom User model
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'PAGINATE_BY': 10,
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


## Celery
# import djcelery
# djcelery.setup_loader()
# BROKER_URL = os.environ.get('BROKER_URL', 'redis://')
# CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', BROKER_URL)


#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#        'LOCATION': '127.0.0.1:11211',
#     },
#}

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.environ.get("EMAIL_PORT", 25))
EMAIL_SUBJECT_PREFIX = "[{0}] ".format(PROJECT_NAME)
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "root@localhost")
