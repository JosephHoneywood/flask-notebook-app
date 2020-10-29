import os
import json
import requests
from bson import json_util

from app import app
from app.forms import CreateNotebookForm, CreateChapterForm, CreateNoteForm
from config import db_mongo
from flask import render_template, redirect, request, jsonify

@app.route('/')
@app.route('/index')
def index():
    #Queries a mongoDB to get all the notebook names in the collection
    notebooks = db_mongo.notebooks_refactor.distinct('notebook')
    #Local data is legacy from when we were testing the UI with a json object... will remove when fully moved to mongo
    return render_template('index.html', notebook_list=notebooks)

@app.route('/createnotebook', methods=['GET', 'POST'])
def create_notebook():
    form = CreateNotebookForm()
    if form.validate_on_submit():
        print(f'Form received with {form.notebook_name.data}')
        # notebook_name = Notebooks(notebook_name=form.notebook_name.data)
        # db.session.add(notebook_name)
        # db.session.commit()
        # print(f'DB updated with {notebook_name.data}')
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

@app.route('/_getchapters', methods=['POST', 'GET'])
def get_chapters():
    #From the request, get the notebook that the user has selected
    jsdata = request.form['send_notebook_name']

    # With the notebook, filter mongo for the chapter names
    notebook = db_mongo.notebooks_refactor.distinct('chapter', {"notebook":jsdata})

    str_chapters = ','.join(notebook)

    return str_chapters

@app.route('/_getnotes', methods=['POST','GET'])
def get_notes():
    #from the request, get the chapter that the user has selected
    jsdata = request.form['send_chapter_name']
    print(jsdata)

    #with the chapter, filter mongo for the associated notes
    notes = list(db_mongo.notebooks_refactor.find({'chapter':jsdata}))
    print(notes)

    return jsonify(json_util.dumps(notes))

