import os
from decouple import config
from django.core.wsgi import get_wsgi_application


if config('DEBUG') or config('heroku_config'):
    os.environ["DJANGO_SETTINGS_MODULE"] = 'RobotixWeb.settings'
    application = get_wsgi_application()
else:
    os.environ["DJANGO_SETTINGS_MODULE"] = 'RobotixWeb.production'
    application = get_wsgi_application()
