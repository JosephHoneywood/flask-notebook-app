from app import app, db
from app.models import Notebooks, Chapters, Notes
from livereload import Server

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Notebooks': Notebooks, 'Chapters': Chapters, 'Notes': Notes}

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()