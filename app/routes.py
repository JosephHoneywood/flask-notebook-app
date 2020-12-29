from datetime import date
from bson import json_util, objectid

from app import app
from config import db_mongo
from flask import render_template, redirect, request, jsonify, url_for
from app.tools.mongo_tools import get_notebooks_from_mongo, push_document_to_mongo, create_chapter_if_new, create_notebook_if_new

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

        document = {"notebook_name":f"{notebook}",
                    "chapter_name":f"{chapter}",
                    "note_title":f"{notetitle}",
                    "note_body":f"{body}",
                    "note_tags":f"{tags}",
                    "note_created-date":f"{date_created}"
                   }

        push_document_to_mongo(document)
        create_notebook_if_new(notebook)
        create_chapter_if_new(notebook, chapter)

        return redirect(url_for('index'))

    return render_template('createnote.html')

@app.route('/_getchapters', methods=['POST', 'GET'])
def get_chapters():

    #From the request, get the notebook that the user has selected
    jsdata = request.form['send_notebook_name']

    # With the notebook, filter mongo for the chapter names
    notebook = db_mongo.chapters.distinct('chapter_name', {"notebook_name":jsdata})
    str_chapters = ','.join(notebook)

    return str_chapters

@app.route('/_getnotes', methods=['POST','GET'])
def get_notes():

    #from the request, get the chapter that the user has selected
    jsdata = request.form['send_chapter_name']

    #with the chapter, filter mongo for the associated notes
    notes = list(db_mongo.notes.find({'chapter_name':jsdata}))

    return jsonify(json_util.dumps(notes))

@app.route('/displaynote/<id>')
def display_notes(id):

    #With the ID, render a new view with the note loaded to the page.
    note_data = db_mongo.notes.find_one({'_id': objectid.ObjectId(id)})

    title = note_data['note_title']
    body = note_data['note_body']

    return render_template('displaynote.html', id=id, title=title, body=body)

@app.route('/deletenote', methods=['POST'])
def delete_note():

    id = request.form['id_to_del']
    db_mongo.notes.delete_one({'_id': objectid.ObjectId(id)})

    return 'ok'

@app.route('/updatenote', methods=['POST'])
def update_note():
    
    id = request.form['id_to_upd']
    updated_body = request.form['updated_content']

    db_mongo.notes.update({'_id': objectid.ObjectId(id)}, {'$set': {'note_body': updated_body}})

    return 'ok'