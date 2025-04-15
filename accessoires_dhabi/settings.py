from pathlib import Path
import os

# === Chemins de base ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Clé secrète (garde-la confidentielle) ===
SECRET_KEY = 'django-insecure-qmp%r$7sxb207f=1n+@w$68u8sn&6)qn%9a@3pwbd0i4z$s7s@'

# === Mode debug ===
DEBUG = True  # Met à False en production

ALLOWED_HOSTS = []

# === Applications installées ===
INSTALLED_APPS = [
    # Django de base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compte',


    # Applications du projet
    'boutique',
    'accessoires_dhabi',
    'blog',
    'rest_framework',
    'drf_yasg',

    # API REST si besoin plus tard
    # 'rest_framework',
]

# === Middlewares ===
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'accessoires_dhabi.urls'

# === Templates ===
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'  # 💡 Ton dossier templates personnalisé
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

WSGI_APPLICATION = 'accessoires_dhabi.wsgi.application'

# === Base de données ===
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# === Validation des mots de passe ===
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# === Paramètres de langue et fuseau horaire ===
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# === Fichiers statiques ===
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

# Configurations media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# === Clé primaire par défaut ===
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# === Configuration SMTP (Gmail par exemple) ===
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'yannickkouassi52@gmail.com'            # ← Remplace avec ton Gmail
EMAIL_HOST_PASSWORD = 'scxg zdyj cuqr ikib'            # ← Mot de passe d’application Gmail


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}