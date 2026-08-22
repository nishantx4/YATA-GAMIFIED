import sqlite3

def check_login(database_file, username, password):
    with sqlite3.connect(database_file) as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        return cursor.fetchone()
