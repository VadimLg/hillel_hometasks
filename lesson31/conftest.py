import pytest
import sqlite3


@pytest.fixture(scope="class")
def db_connection():
    conn = sqlite3.connect("base.db", isolation_level=None)
    cursor = conn.cursor()
    yield conn
    conn.close()
