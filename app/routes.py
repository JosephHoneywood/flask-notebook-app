from app import app
from app.forms import CreateNotebookForm, CreateChapterForm, CreateNoteForm
from flask import render_template, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/createnotebook', methods=['GET', 'POST'])
def create_notebook():
    form = CreateNotebookForm()
    if form.validate_on_submit():
        print(f'Form received with {form.notebook.data}')
        return redirect ('/index')
    return render_template('createnotebook.html', form=form)

@app.route('/createchapter', methods=['GET', 'POST'])
def create_chapter():
    form = CreateChapterForm()
    if form.validate_on_submit():
        print(f'Form received with {form.notebook.data} and {form.chapter.data}')
        return redirect ('/index')
    return render_template('createchapter.html', form=form)

@app.route('/createnote', methods=['GET', 'POST'])
def create_note():
    form = CreateNoteForm()
    if form.validate_on_submit():
        print(f'Form received with {form.notebook.data} and {form.chapter.data} and {form.tags.data} and {form.body.data}')
        return redirect ('/index')
    return render_template('createnote.html', form=form)
