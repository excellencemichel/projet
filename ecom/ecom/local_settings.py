import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True

ALLOWED_HOSTS =["*"]


DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': 'projet',
'USER': 'michel',
'PASSWORD': 'SaintMichel',
'HOST': 'localhost',
'PORT': '',
}
}

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles") #Le slash (/) devant static est l'élément clé qui fait
#les dossiers static sont chargés par le navigateur
STATIFILES_DIRS = (
            os.path.join(BASE_DIR, "static"),
            )

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

