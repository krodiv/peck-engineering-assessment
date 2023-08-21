from app_backend.connection import db_connection

def test_connection():
    connection = db_connection.DbConnection()
    session = connection.get_session()

    # ensure that the session exists and no errors on bring up
    assert session