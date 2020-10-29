from config import db_mongo

def get_notebooks_from_mongo():
    """
    Function accesses mongo and queries all distinct notebooks, returning a list.
    """

    return db_mongo.notebooks_refactor.distinct('notebook')


def push_document_to_mongo(document):
    """
    Function takes a dict to load to mongoDB
    """

    print(f'Moving {document} to mongodb')

    db_mongo.notebooks_refactor.insert_one(document)

    return
