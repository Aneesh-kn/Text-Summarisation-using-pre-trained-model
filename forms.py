# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:54:43 2023

@author: anees
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    input_text = StringField('Input Text',
                           validators=[DataRequired(), Length(min=2, max=2000000)])
    submit = SubmitField('Submit')

