from base import *

DEBUG = True

INSTALLED_APPS.append('')

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
SITE_URL = 'http://127.0.0.1:8000'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'alex_boys30@yahoo.com'