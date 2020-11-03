from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError

class CreateNoteForm(FlaskForm):
    notebook_name = StringField('Notebook Name', validators=[DataRequired()])
    chapter_name = StringField('Chapter Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    tags = StringField('Tags')
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create')

