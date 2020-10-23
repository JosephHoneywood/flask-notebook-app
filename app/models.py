from datetime import datetime
from app import db

class Notebooks(db.model):
    notebook_id = db.column(db.Integer, primary_key=True)
    notebook_name = db.column(db.String(64), index=True, unique=True)
    notebook_created_at_date = db.column(db.DateTime, index=True, default=datetime.utcnow)
    chapters = db.relationship('Chapter', backref='notebook', lazy='dynamic')

    def __repr__(self):
        return '<Notebook {}>'.format(self.notebook_name)

class Chapters(db.model):
    chapter_id = db.column(db.Integer, primary_key=True)
    notebook_id = db.column(db.Integer, db.ForeignKey('notebook.notebook_id'))
    chapter_name = db.column(db.String(120))
    chapter_created_at_date = db.column(db.DateTime, index=True, default=datetime.utcnow)
    notes = db.relationship('Note', backref='chapter', lazy='dynamic')

    def __repr__(self):
        return '<Chapter {}>'.format(self.chapter_name)

class Notes(db.notes):
    note_id = db.column(db.Integer, primary_key=True)
    chapter_id = db.column(db.Integer, db.ForeignKey('chapters.chapter_id'))
    notebook_id = db.column(db.Integer, db.ForeignKey('notebooks.notebook_id'))
    note_name = db.column(db.String(120))
    note_tags = db.column(db.String(120))
    note_body = db.column(db.Text)
    note_created_at_date = db.column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Note {}>'.format(self.note_name)
    
    



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    