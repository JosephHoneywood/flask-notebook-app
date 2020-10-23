from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CreateNotebookForm(FlaskForm):
    notebook = StringField('Notebook Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class CreateChapterForm(FlaskForm):
    notebook = StringField('Notebook Name', validators=[DataRequired()])
    chapter = StringField('Chapter Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class CreateNoteForm(FlaskForm):
    notebook = StringField('Notebook Name', validators=[DataRequired()])
    chapter = StringField('Chapter Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    tags = StringField('Tags')
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create')

