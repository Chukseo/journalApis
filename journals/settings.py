import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "chukseo@gmail.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "Brownweb87")

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY",)
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

# Applications
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "publishing",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "journals.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


ALLOWED_HOSTS = ['localhost','https://journalapis-p8bu.onrender.com/','journalapis-p8bu.onrender.com']   

WSGI_APPLICATION = "journals.wsgi.application"
ASGI_APPLICATION = "journals.asgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Database (PostgreSQL via DATABASE_URL or individual env vars)
DATABASE_URL = os.getenv("postgresql://postgredb1_x8d4_user:SMfTsJ6rPDki7Tg2Wzze8RIdRu4ANhUD@dpg-d49h51hr0fns738ih6r0-a/postgredb1_x8d4")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("POSTGRES_DB", "postgredb1_x8d4"),
            "USER": os.getenv("POSTGRES_USER", "postgredb1_x8d4_user"),
            "PASSWORD": os.getenv("POSTGRES_PASSWORD", "SMfTsJ6rPDki7Tg2Wzze8RIdRu4ANhUD"),
            "HOST": os.getenv("POSTGRES_HOST", "dpg-d49h51hr0fns738ih6r0-a"),
            "PORT": os.getenv("POSTGRES_PORT", "5432"),
        }
    }

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Media files (use an object storage in production for durability)
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# Timezone/Localization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Lagos"
USE_I18N = True
USE_TZ = True

# Security (production)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_SSL_REDIRECT = os.getenv("SECURE_SSL_REDIRECT", "True").lower() == "true"
X_FRAME_OPTIONS = "DENY"

# REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        # Enable Browsable API in development
        *(["rest_framework.renderers.BrowsableAPIRenderer"] if DEBUG else []),
    ],
}


CORS_ALLOWED_ORIGINS = [
    "http://localhost:4000",
    "https://mejhpgs.netlify.app",
]


# CORS (adjust for your frontend domain)
# CORS_ALLOWED_ORIGINS = [origin for origin in os.getenv("CORS_ALLOWED_ORIGINS", "").split(",") if origin]
# CORS_ALLOW_ALL_ORIGINS = not CORS_ALLOWED_ORIGINS

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {"handlers": ["console"], "level": os.getenv("LOG_LEVEL", "INFO")},
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
