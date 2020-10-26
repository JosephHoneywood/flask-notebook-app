from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from app.models import Notebooks, Chapters, Notes

class CreateNotebookForm(FlaskForm):
    notebook_name = StringField('Notebook Name', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_notebook_name(self, notebook_name):
        notebook = Notebooks.query.filter_by(notebook_name=notebook_name.data).first()
        if notebook is not None:
            raise ValidationError('Please use a different notebook name')


class CreateChapterForm(FlaskForm):
    notebook_name = StringField('Notebook Name', validators=[DataRequired()])
    chapter_name = StringField('Chapter Name', validators=[DataRequired()])
    submit = SubmitField('Create')

class CreateNoteForm(FlaskForm):
    notebook_name = StringField('Notebook Name', validators=[DataRequired()])
    chapter_name = StringField('Chapter Name', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    tags = StringField('Tags')
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create')

