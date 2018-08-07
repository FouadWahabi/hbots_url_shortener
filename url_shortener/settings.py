# -*- coding: utf-8 -*-

BASE_URL = 'http://short-test.hbots.co'

PREFIX = '_'

DEBUG = True
TESTING = False

SECRET_KEY = 'Sykmx)yj%mZ/Mo|'
CSRF_ENABLED = True
CSRF_SESSION_KEY = '_csrf_token'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@127.0.0.1:5432/socialbots'

try:
    from .local_settings import *
except ImportError:
    pass
