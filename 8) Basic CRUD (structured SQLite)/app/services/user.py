from app.database import get_db_connection

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

def add_user(name, age):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def update_user(id, name, age):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()
    conn.close()

def delete_user(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()