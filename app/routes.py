import os
import json
import requests
from datetime import date
from bson import json_util, objectid

from app import app
from app.forms import CreateNoteForm
from config import db_mongo
from flask import render_template, redirect, request, jsonify
from app.tools.mongo_tools import get_notebooks_from_mongo, push_document_to_mongo

@app.route('/')
@app.route('/index')
def index():
    notebooks = get_notebooks_from_mongo()

    return render_template('index.html', notebook_list=notebooks)

@app.route('/createnote', methods=['GET', 'POST'])
def create_note():
    form = CreateNoteForm()
    notebooks = get_notebooks_from_mongo()
    if form.validate_on_submit():

        print(f'Form received with {form.notebook_name.data} and {form.chapter_name.data} and {form.tags.data} and {form.body.data}')
        notebook = form.notebook_name.data
        chapter = form.chapter_name.data
        title = form.title.data
        body = form.body.data
        tags = form.tags.data
        date_created = date.today()

        document = {"notebook": f"{notebook}",
                    "chapter":f"{chapter}",
                    "note-title":f"{title}",
                    "note-body":f"{body}",
                    "note-tags":f"{tags}",
                    "note-created-date":f"{date_created}"
                    }

        push_document_to_mongo(document)

        return redirect ('/index')
    return render_template('createnote.html', form=form, notebook_list=notebooks)

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

@app.route('/displaynote/<id>')
def display_notes(id):

    #With the ID, render a new view with the note loaded to the page.
    note_data = db_mongo.notebooks_refactor.find_one({'_id': objectid.ObjectId(id)})

    title = note_data['note-title']
    body = note_data['note-body']

    print(note_data)

    return render_template('displaynote.html', id=id, title=title, body=body)

@app.route('/deletenote', methods=['POST'])
def delete_note():
    id = request.form['id_to_del']
    
    db_mongo.notebooks_refactor.delete_one({'_id': objectid.ObjectId(id)})

    return 'ok'