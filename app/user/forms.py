from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, TextAreaField, SelectField
from wtforms.fields.simple import FileField
from wtforms.validators import Required

class blogPostsForm(FlaskForm):
    title = StringField('Post title',validators=[Required()])

    summary = StringField('Summary of the post',validators=[Required()] )

    post = TextAreaField('Enter the post details', validators=[Required()])

    image = StringField('Enter Image link', validators=[Required()])

    submit = SubmitField('Submit')