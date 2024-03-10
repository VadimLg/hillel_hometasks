import sqlite3
import pprint


class User:
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age

    def get_user_attributes(self):
        return self.username, self.email, self.age


class Base:
    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path, isolation_level=None)
        self._cursor = self._connection.cursor()

    def __del__(self):
        if self._cursor:
            self._cursor.close()
        if self._connection:
            self._connection.close()


class Users(Base):

    def __init__(self, db_path):
        super().__init__(db_path)
        self._cursor.execute(
            "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username TEXT NOT NULL, email TEXT NOT NULL, age INTEGER);")

    def add_user(self, user: User):
        self._cursor.execute("INSERT INTO Users(username, email, age) VALUES ((?), (?), (?));",
                             user.get_user_attributes())

    def add_users(self, users):
        self._cursor.executemany("INSERT INTO Users(username, email, age) VALUES ((?), (?), (?));",
                                 [user.get_user_attributes() for user in users])

    def get_all_users(self):
        result = self._cursor.execute('SELECT * from Users;')
        return result.fetchall()


user_tab = Users('base.db')
user1 = User("Максим", "maks@gmail.com", 20)
user_tab.add_user(user1)
users = [User("Виталий", "vitalya@gmail.com", 25), User("Светлана", "sveta@gmail.com", 30)]
print(str(users))
user_tab.add_users(users)
pprint.pprint(user_tab.get_all_users())
