import os
from pathlib import Path
from decouple import config

# ✅ BASE_DIR must be Path object (never overwrite this!)
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='dev-secret')
DEBUG = config('DEBUG', default='True') == 'True'
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',

    # Your app
    'core',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    # Session must come BEFORE LocaleMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 🔥 Enables multi-language switching
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'farmlink.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',   # works because BASE_DIR is Path object
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'farmlink.wsgi.application'

# Database Switch (SQLite / PostgreSQL)
if config('USE_POSTGRES', default='False') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('POSTGRES_HOST', default='localhost'),
            'PORT': config('POSTGRES_PORT', default='5432'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',   # path object clean
        }
    }

AUTH_USER_MODEL = 'core.User'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

CORS_ALLOW_ALL_ORIGINS = True

# DRF Global Permissions
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    ]
}

# 🔥 MULTILINGUAL SUPPORT ENABLED HERE
LOCALE_PATHS = [
    BASE_DIR / "locale",
]

LANGUAGE_CODE = 'en'

USE_I18N = True
USE_L10N = True

# 🌍 All Indian languages + English
LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('kn', 'Kannada'),
    ('te', 'Telugu'),
    ('ta', 'Tamil'),
    ('ml', 'Malayalam'),
    ('mr', 'Marathi'),
    ('gu', 'Gujarati'),
    ('bn', 'Bengali'),
    ('pa', 'Punjabi'),
    ('or', 'Odia'),
    ('as', 'Assamese'),
    ('ur', 'Urdu'),
    ('ne', 'Nepali'),
    ('sd', 'Sindhi'),
    ('sa', 'Sanskrit'),
]
