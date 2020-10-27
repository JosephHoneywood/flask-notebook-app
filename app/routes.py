import os
import json

from app import app, db
from app.models import Notebooks, Chapters, Notes
from app.forms import CreateNotebookForm, CreateChapterForm, CreateNoteForm
from flask import render_template, redirect

json_data = "/Users/josephhoneywood/Desktop/Home/V26/flask-notebook-app/app/static/js/data_2.json"
local_data = json.load(open(json_data))

@app.route('/')
@app.route('/index')
def index():
    notebook_list = [notebook.notebook_name for notebook in Notebooks.query.all()]
    print(notebook_list)
    return render_template('index.html', notebook_list=notebook_list, local_data=local_data)

@app.route('/createnotebook', methods=['GET', 'POST'])
def create_notebook():
    form = CreateNotebookForm()
    if form.validate_on_submit():
        print(f'Form received with {form.notebook_name.data}')
        notebook_name = Notebooks(notebook_name=form.notebook_name.data)
        db.session.add(notebook_name)
        db.session.commit()
        print(f'DB updated with {notebook_name.data}')
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
