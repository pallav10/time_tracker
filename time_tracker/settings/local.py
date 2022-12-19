from .common import *

INSTALLED_APPS += ["django_extensions"]

DEFAULT_DATABASE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

DATABASES = {'default': DEFAULT_DATABASE}
