import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_1&tarcy#$-%^8v%m4u7f@d%k2%oqk4ze9h+vn0_k#amw*rz%x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
        'localhost',
        '0.0.0.0',
        'https://cosasdetios.com',
        'http://cosasdetios.com',
        'https://www.cosasdetios.com',
        'http://www.cosasdetios.com',
        ]

SITE_ID = 2

# Application definition

INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django.contrib.sitemaps',

        'django_extensions',
        'autofixture',

        'robots',
        'storages',
        'podcast',
        'dynamic_preferences',
        'gunicorn',
        'fortune',
        'ckeditor',
        'ckeditor_uploader',
        'import_export',
        'posts',
        ]

MIDDLEWARE = [
        'django.middleware.gzip.GZipMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

ROOT_URLCONF = 'cosasdetios.urls'

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
                ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                    'dynamic_preferences.processors.global_preferences',
                    'cosasdetios.context_processors.nav',
                    'cosasdetios.context_processors.sidebar',
                    'cosasdetios.context_processors.footer',
                    ],
                'builtins': [
                    'cosasdetios.templatetags.cowsay_tags',
                    ]
                },
            },
        ]

WSGI_APPLICATION = 'cosasdetios.wsgi.application'

DYNAMIC_PREFERENCES = {
        'MANAGER_ATTRIBUTE': 'preferences',
        'REGISTRY_MODULE': 'dynamic_preferences_registry',
        'ADMIN_ENABLE_CHANGELIST_FORM': True,
        'ENABLE_USER_PREFERENCES': False,
        'SECTION_KEY_SEPARATOR': '_',
        'ENABLE_CACHE': True,
        'VALIDATE_NAMES': True,
        }

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

SERIALIZATION_MODULES = {
        'geojson': 'djgeojson.serializers'
        }

# Ckeditor config
CKEDITOR_CONFIGS = {
        'default': {
            'skin': 'moono',
            'toolbar_OrggueToolbar': [
                {'name': 'document', 'items': ['Source', '-', 'Save',
                    'NewPage', 'Preview', 'Print', '-', 'Templates']},
                {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste',
                    'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
                {'name': 'links', 'items': ['Link', 'Unlink']},
                {'name': 'insert', 'items': ['Image', 'Table',
                    'HorizontalRule', 'Smiley', 'SpecialChar']}, '/',
                {'name': 'basicstyles', 'items': [
                    'Bold', 'Italic', 'Underline', 'Strike',
                    'Subscript', 'Superscript', '-', 'RemoveFormat']},
                {'name': 'paragraph', 'items': [
                    'NumberedList', 'BulletedList', '-', 'Outdent',
                    'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                    'JustifyLeft', 'JustifyCenter', 'JustifyRight',
                    'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language']},
                {'name': 'colors', 'items': ['TextColor', 'BGColor']},
                {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
                {'name': 'styles', 'items': ['Styles', 'Format', 'FontSize']},
                ],
            'toolbar': 'OrggueToolbar',
            'tabSpaces': 4,
            'extraPlugins': ','.join(
                [
                    'div',
                    'autolink',
                    'autoembed',
                    'embedsemantic',
                    'autogrow',
                    'widget',
                    'lineutils',
                    'clipboard',
                    'dialog',
                    'dialogui',
                    'elementspath'
                    ]),
                }
        }
CKEDITOR_UPLOAD_SLUGIFY_FILENAME = True
CKEDITOR_ALLOW_NONIMAGE_FILES = False
CKEDITOR_UPLOAD_PATH = "uploads/"

STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'compass/out'),
        )

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# podcast
PODCAST_SINGULAR = True
PODCAST_ID = 1
PODCAST_PAGINATE_BY = 9

try:
    from local_settings import *
except ImportError:
    pass
