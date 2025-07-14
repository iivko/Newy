import os
from pathlib import Path
from dotenv import load_dotenv


ENV_STATE = os.getenv("ENV_STATE")

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

ALLOWED_HOSTS = ["*"]

ADMIN_URL = os.getenv("ADMIN_URL", "admin")

if ENV_STATE == "production":
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend"
]


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "django.contrib.postgres",
    'django.contrib.staticfiles',
    "django.contrib.humanize",
    "django.contrib.sites",
    "whitenoise.runserver_nostatic",
]

THIRD_PARTY_APPS = [
    "allauth",
    "anymail",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.github",
    "widget_tweaks",
]

MAIN_APPS = [
    'app'
]

SITE_ID = 1


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MAIN_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
]


if DEBUG:
    INSTALLED_APPS += [
        "debug_toolbar",
        "django_browser_reload",
    ]

    MIDDLEWARE += [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "django_browser_reload.middleware.BrowserReloadMiddleware",
    ]

    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())

    docker_ips = [ip[:-1] + "1" for ip in ips]

    INTERNAL_IPS = docker_ips + ["127.0.0.1"]

ROOT_URLCONF = 'bloger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bloger.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DATABASE_NAME"),
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("DATABASE_HOST"),
        "PORT": os.getenv("DATABASE_PORT"),
    }
}


AUTH_USER_MODEL = "app.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


DEFAULT_FROM_EMAIL = os.getenv("MAILGUN_EMAIL", "None")

ANYMAIL = {
    "MAILGUN_API_KEY": os.getenv("MAILGUN_API_KEY", "None"),
    "SEND_DEFAULTS": {"tags": ["newy"]}
}

EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"


# Allauth
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*"]
ACCOUNT_EMAIL_VERIFICATION = True


LOGIN_REDIRECT_URL = "read_news"
LOGOUT_REDIRECT_URL = "account_login"

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'bg'

TIME_ZONE = 'Europe/Sofia'

USE_I18N = True

USE_TZ = True


LOCALE_PATHS = [
    BASE_DIR / "locale"
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR/ "staticfiles"


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage"
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage"
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
