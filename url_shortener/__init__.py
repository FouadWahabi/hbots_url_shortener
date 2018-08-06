# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from url_shortener import settings
from url_shortener.context_processors import static_files
from url_shortener.core import setup_routing

# setup application
app = Flask('url_shortener')
app.config.from_object(settings)

# setup database
db = SQLAlchemy(app)

# register application views and blueprints
from url_shortener.urls import routes
setup_routing(app, routes)

# register context processors
app.context_processor(static_files)
