"""
Loyihaning sozlamalari.

Bu fayl to'liq tayyor — buni o'zgartirish shart emas.

DIQQAT (LoginRequiredMixin haqida): vazifada Create/Update/Delete
view'lari LoginRequiredMixin bilan himoyalanishi kerak. Bu loyihada
alohida login sahifasi qurish vazifaning maqsadi emas, shuning uchun
LOGIN_URL Django admin panelining tayyor login sahifasiga
yo'naltirilgan — sinab ko'rishda shu orqali tizimga kirasiz
(pastga, README.md ga qarang).
"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-uy-vazifasi-cbv-2qism-talaba-crud'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'talabalar',  # bizning ilovamiz
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'talaba_crud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'talaba_crud.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'uz'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LoginRequiredMixin ishlatilgan view'lar shu manzilga yo'naltiradi.
# Alohida login sahifa qurish shart emas — Django admin login sahifasi
# ishlatiladi (pastga, README.md ga qarang).
LOGIN_URL = '/admin/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'royxat'
LOGOUT_REDIRECT_URL = 'login'

