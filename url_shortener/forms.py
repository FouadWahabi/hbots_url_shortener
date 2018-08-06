# -*- coding: utf-8 -*-

import re
from flask_wtf import Form
from wtforms import TextField, SubmitField
from wtforms.validators import Required, Optional, Length, URL, Regexp


RE_SLUG = re.compile(r'^[-\w]+$')

class URLForm(Form):
    url = TextField('URL', validators=[Required(), Length(max=255), URL()])
    slug = TextField('Slug', validators=[Optional(), Length(max=30), Regexp(RE_SLUG)])
    submit = SubmitField('shorten')
