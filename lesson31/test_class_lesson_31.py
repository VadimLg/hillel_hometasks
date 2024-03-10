import pytest


@pytest.mark.usefixtures("db_connection")
class TestUsers:

    @pytest.mark.parametrize("username, result", [
        pytest.param("Максим", "maks@gmail.com", id="positive user 1"),
        pytest.param("Виталий", "vitalya@gmail.com", id="positive user 2"),
        pytest.param("Светлана", "sveta@gmail.com", id="positive user 3")
    ])
    def test_table_existence(self, db_connection, username, result):
        cursor = db_connection.cursor()
        cursor.execute(f"SELECT email FROM Users WHERE username='{username}'")
        assert cursor.fetchone()[0] == result
