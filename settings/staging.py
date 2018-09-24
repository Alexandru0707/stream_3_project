from base import *
import dj_database_url

DEBUG = False

# Load the ClearDB connection details from the environment variable
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_AC799DLHoVLESzRQViBEKl1e')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_mas6PxM1yX0PbOTnZfxFgMbP')


# PayPal Settings

PAYPAL_NOTIFY_URL = 'https://cozma-alexandru-photography.herokuapp.com'
PAYPAL_RECEIVER_EMAIL = 'alex_boys30@yahoo.com'

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