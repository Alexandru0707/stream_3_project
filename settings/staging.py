from base import *
import dj_database_url
import os


DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')


# PayPal Settings

PAYPAL_NOTIFY_URL = 'https://cozma-alexandru-photography.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = os.getenv('PAYPAL_NOTIFY_URL', 'Optional default value')

SITE_URL = 'https://cozma-alexandru-photography.herokuapp.com'
ALLOWED_HOSTS.append('cozma-alexandru-photography.herokuapp.com')

# Log DEBUG information to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}