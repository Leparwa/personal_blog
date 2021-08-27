from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, SelectField
from wtforms.fields.simple import FileField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Post title',validators=[Required()])

    summary = StringField('Summary of the post')

    description = TextAreaField('Enter the post')

    submit = SubmitField('Submit')