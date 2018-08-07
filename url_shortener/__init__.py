# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from url_shortener import settings
from url_shortener.context_processors import static_files
from url_shortener.core import setup_routing
from url_shortener.core import setup_apis

# setup application
app = Flask('url_shortener')
api = Api(app)
app.config.from_object(settings)

# setup database
db = SQLAlchemy(app)

# register application views and blueprints
from url_shortener.urls import routes
from url_shortener.urls import apis
setup_routing(app, routes)
setup_apis(api, apis)

# register context processors
app.context_processor(static_files)
