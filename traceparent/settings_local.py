ADMINS = (
     ('Bert Poller', 'bpoller@ekito.fr'),
)
DEFAULT_FROM_EMAIL = ADMINS[0][1]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'traceparent.sqlite',                      # Or path to database file if using sqlite3.
        #'USER': 'traceparent',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
       # 'STORAGE_ENGINE': 'MyISAM', # For MySQL.
    }
}

SECRET_KEY = 'q)#r434^2x)4eu^#x_akx6p#2wu%u(358hkywbmgxya8=*592k'
