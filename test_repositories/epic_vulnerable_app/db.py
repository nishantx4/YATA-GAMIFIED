import sqlite3

def check_login(database_file, username, password):
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        return cursor.fetchone()
