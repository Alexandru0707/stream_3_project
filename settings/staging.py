from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
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