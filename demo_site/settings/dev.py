from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tec5z#b$p_em4nuf(f4p3rw!!@z=nw1!1iicq%uta-%&w72f&a'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_URL = 'http://127.0.0.1:8000/media/'


try:
    from .local import *
except ImportError:
    pass
