from app_backend.connection import db_connection

def test_fail():
    assert False

def test_connection():
    connection = db_connection.DbConnection()
    session = connection.get_session()

    # ensure that the session exists
    assert session