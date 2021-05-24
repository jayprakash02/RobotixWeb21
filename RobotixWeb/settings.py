import dj_database_url
import django_on_heroku
from decouple import config
from .production import *


ALLOWED_HOSTS.append('.herokuapp.com')


if config('DEBUG'):
    SECRET_KEY = config('SECRET_KEY')
    DEBUG=True


## Installed apps
INSTALLED_APPS.append('whitenoise.runserver_nostatic')


## Middlewares
temp = ['whitenoise.middleware.WhiteNoiseMiddleware']
for i in range(len(MIDDLEWARE)):
    temp.append(MIDDLEWARE[i])
MIDDLEWARE = temp


WSGI_APPLICATION = 'RobotixWeb.wsgi.application'


# Database
if config('DEBUG'):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD' :config('DB_PASSWORD'),
            'HOST' : config('DB_HOST'),
            'PORT' : config('DB_PORT')
        }
    }
else:
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)
    WHITENOISE_USE_FINDERS = True
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


STATIC_URL = '/static/static/'
MEDIA_URL = '/media/media/'


STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'staticfiles'))
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, 'mediafiles'))

django_on_heroku.settings(locals())
