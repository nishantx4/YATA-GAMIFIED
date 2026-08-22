import sqlite3

def search_products(query):
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()
    # SQL Injection
    cursor.execute(f"SELECT * FROM products WHERE name LIKE '%{query}%'")
    results = cursor.fetchall()
    conn.close()
    return results
