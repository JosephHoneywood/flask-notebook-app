from datetime import datetime
from app import db

class Notebooks(db.Model):
    notebook_id = db.Column(db.Integer, primary_key=True)
    notebook_name = db.Column(db.String(64), index=True, unique=True)
    notebook_created_at_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    chapters = db.relationship('Chapters', backref='notebook', lazy='dynamic')

    def __repr__(self):
        return '<Notebook {}>'.format(self.notebook_name)

class Chapters(db.Model):
    chapter_id = db.Column(db.Integer, primary_key=True)
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.notebook_id'))
    chapter_name = db.Column(db.String(120))
    chapter_created_at_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    notes = db.relationship('Notes', backref='chapter', lazy='dynamic')

    def __repr__(self):
        return '<Chapter {}>'.format(self.chapter_name)

class Notes(db.Model):
    note_id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapters.chapter_id'))
    notebook_id = db.Column(db.Integer, db.ForeignKey('notebooks.notebook_id'))
    note_name = db.Column(db.String(120))
    note_tags = db.Column(db.String(120))
    note_body = db.Column(db.Text)
    note_created_at_date = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Note {}>'.format(self.note_name)
