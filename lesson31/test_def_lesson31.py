import sqlite3
import pytest


@pytest.fixture
def db_connection():
    conn = sqlite3.connect("base.db", isolation_level=None)
    cursor = conn.cursor()
    yield conn
    conn.close()


@pytest.mark.parametrize("username, result", [
    pytest.param("Максим", "maks@gmail.com", id="positive user 1"),
    pytest.param("Виталий", "vitalya@gmail.com", id="positive user 2"),
    pytest.param("Светлана", "sveta@gmail.com", id="positive user 3")
])
def test_user_email(db_connection, username, result):
    cursor = db_connection.cursor()
    cursor.execute(f"SELECT email FROM Users WHERE username='{username}'")
    assert cursor.fetchone()[0] == result
