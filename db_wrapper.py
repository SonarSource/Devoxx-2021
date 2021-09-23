import sqlite3

class ConnectionWrapper:
    """A simple connection wrapper class"""
    __default_statement = 'SELECT * FROM MY_TABLE WHERE id = 1'

    def __init__(self):
        self.__conn = conn = sqlite3.connect('database.db')

    def get_single(self, value_id: str):
        statement = "SELECT * FROM MY_TABLE WHERE id = '%s'" % value_id
        return self.__conn.execute(statement).fetchone()

    def cleanup(self, should_close: bool):
        if should_close:
            self.__conn.close()
