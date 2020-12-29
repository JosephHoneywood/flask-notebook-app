from config import db_mongo

def get_notebooks_from_mongo():
    """
    Function accesses mongo and queries all distinct notebooks, returning a list.
    """

    return db_mongo.notebooks.distinct('notebook_name')


def push_document_to_mongo(document):
    """
    Function takes a dict to load to mongoDB
    """

    print(f'Moving {document} to mongodb')

    db_mongo.notes.insert_one(document)

    return

def create_notebook_if_new(notebook):

    notebooks_in_mongo = db_mongo.notebooks.distinct('notebook_name')

    if notebook in notebooks_in_mongo:
        print('Notebook already exists. No requirement to create a new one.')
        return
    else:
        db_mongo.notebooks.insert_one({'notebook_name':f"{notebook}"})
        return

def create_chapter_if_new(notebook, chapter):

    if db_mongo.chapters.find_one({"notebook_name":f"{notebook}", "chapter_name":"{chapter}"}) is None:
       db_mongo.chapters.insert_one({"chapter_name":f"{chapter}", "notebook_name":f"{notebook}"})
       return
    else:
        print('Notebook and chapter already exist')
        return
    