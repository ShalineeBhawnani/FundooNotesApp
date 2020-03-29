
import datetime
import logging
import os
import time
from datetime import datetime, timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/token"

SITE_ID = 2
INSTALLED_APPS = [
    'storages',
    #'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'snippets', 
    'rest_framework_swagger',
    'oauth2_provider',
    'rest_framework',
    'rest_framework_jwt',
    'django_short_url',
    'social_django',
    'note',
    'rest_framework.authtoken',
    'django_elasticsearch_dsl',
    'django_celery_beat',
    'django_elasticsearch_dsl_drf',
    'django_celery_results',
    'corsheaders', #Cross Origin Resource Sharing.
    'djcelery',
    
    
]


MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.middleware.common.CommonMiddleware',
     'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', 
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    

  
]
CORS_ORIGIN_ALLOW_ALL = True 
CORS_ORIGIN_WHITELIST = [
   "http://127.0.0.1:4200",
 ]
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'X-CSRFToken',
    'x-csrftoken',
    'X-XSRF-TOKEN',
    'XSRF-TOKEN',
    'csrfmiddlewaretoken',
    'csrftoken',
    'X-CSRF',
    'headers',
    'token',
)

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'template')],
         'APP_DIRS': True,
         'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
    

              
            ]
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fundoo',
        'USER': 'me',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}



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



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True





CACHE_TTL = 60 * 25

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}
#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

EMAIL_PORT = os.getenv('EMAIL_PORT')


# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.BasicAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ),
#     'DEFAULT_PAGINATION_CLASS':
#         'rest_framework.pagination.PageNumberPagination',
#     'PAGE_SIZE': 100,
#     'ORDERING_PARAM': 'ordering',
# }
# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'basic': {
#             'type': 'basic'
#         }
#     },
# }
# Elasticsearch configuration
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'localhost:9200'
    },
}

# # Name of the Elasticsearch index
# ELASTICSEARCH_INDEX_NAMES = {
#     'note.search': 'note',
# }


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

# CELERYBEAT_SCHEDULE = {
#     "send_mail": {
#         "task": "note.tasks.send_mail",
#         "schedule": timedelta(seconds=1),
#     },
# }
# CELERYBEAT_SCHEDULER ="django_celery_beat.schedulers:DatabaseScheduler"
BROKER_TRANSPORT = 'redis'
# BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = 'Asia/Makassar'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


CELERY_IMPORTS = ("note.tasks",)


STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


