import os
from django.utils.translation import gettext_lazy as _

DIRNAME = os.path.dirname(__file__)

DEBUG = True
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False
COMPRESS_CACHE_BACKEND = 'locmem:///'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'webshop2',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'pgwpujci',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = DIRNAME + "/media"

# static files settings
STATIC_URL = '/static/'
STATIC_ROOT = DIRNAME + "/sitestatic"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+0zsw5n@v7*rhl6r6ufqhoc6jlqq0f-u8c+gh(hjb+_jmg@rh6'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "pagination.middleware.PaginationMiddleware",
    "muecke.utils.middleware.AJAXSimpleExceptionResponse",
    "muecke.utils.middleware.ProfileMiddleware",
   # 'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    "compressor",
    "muecketheme",
    "django.contrib.admin",
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    "django.contrib.flatpages",
    "django.contrib.redirects",
    "django.contrib.sitemaps",
    'django_countries',
    'django_extensions',
    'django_jenkins',
    "pagination",
    'reviews',
    "tagging",
    "portlets",
    "muecke",
    "muecke.tests",
    'muecke.core',
    'muecke.caching',
    'muecke.cart',
    'muecke.catalog',
    'muecke.checkout',
    "muecke.criteria",
    "muecke.customer",
    "muecke.customer_tax",
    "muecke.discounts",
    "muecke.export",
    'muecke.gross_price',
    'muecke.integrationtests',
    'muecke.mail',
    'muecke.manage',
    'muecke.marketing',
    'muecke.manufacturer',
    'muecke.net_price',
    'muecke.order',
    'muecke.page',
    'muecke.payment',
    'muecke.portlet',
    'muecke.search',
    'muecke.shipping',
    'muecke.supplier',
    'muecke.tagging',
    'muecke.tax',
    'muecke.utils',
    'muecke.voucher',
    "muecke_contact",
    "muecke_order_numbers",
    'paypal.standard.ipn',
    'paypal.standard.pdt',
    'gunicorn',
    'debug_toolbar',
	'postal',
    "django_nose",
    "muecke_paymill",
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

FORCE_SCRIPT_NAME=""
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/manage/"

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'muecke.core.context_processors.main',
)

AUTHENTICATION_BACKENDS = (
    'muecke.customer.auth.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# For sql_queries
INTERNAL_IPS = (
    "127.0.0.1",
)

# CACHE_BACKEND = 'file:///'
# CACHE_BACKEND = 'locmem:///'
CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
# CACHE_BACKEND = 'dummy:///'
CACHE_MIDDLEWARE_KEY_PREFIX = "muecke"

EMAIL_HOST = ""
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

PAYPAL_RECEIVER_EMAIL = "stefan.perndl@bud-and-terence.com"
PAYPAL_IDENTITY_TOKEN = "set_this_to_your_paypal_pdt_identity_token"

# TODO: Put this into the Shop model
LFS_PAYPAL_REDIRECT = True
LFS_AFTER_ADD_TO_CART = "muecke_added_to_cart"
LFS_RECENT_PRODUCTS_LIMIT = 5

LFS_ORDER_NUMBER_GENERATOR = "muecke_order_numbers.models.OrderNumberGenerator"
LFS_DOCS = "http://docs.getmuecke.com/en/latest/"

REVIEWS_SHOW_PREVIEW = False
REVIEWS_IS_NAME_REQUIRED = False
REVIEWS_IS_EMAIL_REQUIRED = False
REVIEWS_IS_MODERATED = False

LFS_INVOICE_COMPANY_NAME_REQUIRED = False
LFS_INVOICE_EMAIL_REQUIRED = True
LFS_INVOICE_PHONE_REQUIRED = True

LFS_SHIPPING_COMPANY_NAME_REQUIRED = False
LFS_SHIPPING_EMAIL_REQUIRED = False
LFS_SHIPPING_PHONE_REQUIRED = False

LFS_PAYMENT_METHOD_PROCESSORS = [
    ["muecke_paymill.models.PaymillPaymentMethodProcessor", "Paymill"],
    ["muecke_sofortueberweisung.models.SofortUeberweisungPaymentMethodProcessor", "sofortueberweisung.de"],
]

PAYMILL_PUBLIC_KEY = "092429092507668104ca685855f1b8da"
PAYMILL_PRIVATE_KEY = "9e365cc88f82e926c9f2756341b9b19b"

SOFORTUEBERWEISUNG_USERID = "your_user_id"
SOFORTUEBERWEISUNG_PROJECT_ID = "your_project_id"

LFS_PRICE_CALCULATORS = [
    ['muecke.gross_price.GrossPriceCalculator', _(u'Price includes tax')],
    ['muecke.net_price.NetPriceCalculator', _(u'Price excludes tax')],
]

LFS_SHIPPING_METHOD_PRICE_CALCULATORS = [
    ["muecke.shipping.GrossShippingMethodPriceCalculator", _(u'Price includes tax')],
    ["muecke.shipping.NetShippingMethodPriceCalculator", _(u'Price excludes tax')],
]

LFS_UNITS = [
    u"l",
    u"m",
    u"qm",
    u"cm",
    u"lfm",
    u"Package",
    u"Piece",
]

LFS_PRICE_UNITS = LFS_BASE_PRICE_UNITS = LFS_PACKING_UNITS = LFS_UNITS

# apps that we want jenkins ci to test
PROJECT_APPS = ['muecke.core',]
JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',
                 #'django_jenkins.tasks.with_coverage',
                 'django_jenkins.tasks.django_tests',
                 'django_jenkins.tasks.run_pep8',
                 'django_jenkins.tasks.run_pyflakes',
                 #'django_jenkins.tasks.windmill_tests',
                )

PISTON_DISPLAY_ERRORS = True

LFS_LOG_FILE = DIRNAME + "/../muecke.log"

LOGGING = {
    "version": 1,
    "formatters": {
        "plain": {
            "format": "%(asctime)s %(message)s"
        },
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(message)s",
            "datefmt": "%a, %d %b %Y %H:%M:%S",
        },
    },
    "handlers": {
         "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter": "verbose",
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'verbose',
            'filename': LFS_LOG_FILE,
            'mode': 'a',
        },
    },
    "loggers": {
        "default": {
            "handlers": ["logfile", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
        "deprecated": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
