import os
import json
import requests
from datetime import date
from bson import json_util, objectid

from app import app
from config import db_mongo
from flask import render_template, redirect, request, jsonify
from app.tools.mongo_tools import get_notebooks_from_mongo, push_document_to_mongo

@app.route('/')
@app.route('/index')
def index():
    notebooks = get_notebooks_from_mongo()
    return render_template('index.html', notebook_list=notebooks)

@app.route('/createnote', methods=['POST', 'GET'])
def create_note2():

    if request.method == 'POST':

        notebook = request.form.get('notebookname')
        chapter = request.form.get('chaptername')
        notetitle = request.form.get('notetitle')
        body = request.form.get('editordata')
        tags = request.form.get('tags')
        date_created = date.today()

        document = {"notebook":f"{notebook}",
                    "chapter":f"{chapter}",
                    "note-title":f"{notetitle}",
                    "note-body":f"{body}",
                    "note-tags":f"{tags}",
                    "note-created-date":f"{date_created}"
                   }

        push_document_to_mongo(document)

        return 'Posted data'
    return render_template('createnote.html')

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
    #with the chapter, filter mongo for the associated notes
    notes = list(db_mongo.notebooks_refactor.find({'chapter':jsdata}))

    return jsonify(json_util.dumps(notes))

@app.route('/displaynote/<id>')
def display_notes(id):

    #With the ID, render a new view with the note loaded to the page.
    note_data = db_mongo.notebooks_refactor.find_one({'_id': objectid.ObjectId(id)})
    title = note_data['note-title']
    body = note_data['note-body']

    return render_template('displaynote.html', id=id, title=title, body=body)

@app.route('/deletenote', methods=['POST'])
def delete_note():
    id = request.form['id_to_del']
    db_mongo.notebooks_refactor.delete_one({'_id': objectid.ObjectId(id)})

    return 'ok'

@app.route('/updatenote', methods=['POST'])
def update_note():
    id = request.form['id_to_upd']
    updated_body = request.form['updated_content']

    db_mongo.notebooks_refactor.update({'_id': objectid.ObjectId(id)}, {'$set': {'note-body': updated_body}})

    return 'ok'