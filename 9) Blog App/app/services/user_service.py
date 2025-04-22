from app.database import get_db_connection
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def get_user_by_email(email, id=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    if id:
        cursor.execute("SELECT * FROM users WHERE email = ? AND id != ?", (email, id))
    else:
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    
    user = cursor.fetchone()
    conn.close()
    return user

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            u.id, 
            u.name, 
            u.email, 
            u.role, 
            u.is_active,
            COUNT(b.id) AS blog_count
        FROM users u
        LEFT JOIN blogs b ON u.id = b.user_id
        WHERE u.role = 2
        GROUP BY u.id, u.name, u.email, u.role, u.is_active
    ''')
    
    users = cursor.fetchall()
    conn.close()
    return users


def get_user_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE role = 2")
    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users u WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user


def add_user(name, email, password, role=2):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)", 
    (name, email, hashed_password, role))
    
    conn.commit()
    conn.close()


def update_user(id, name, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=?, email=?, updated_at=CURRENT_TIMESTAMP WHERE id=?",
    (name, email, id))
    conn.commit()
    conn.close()

def update_user_password(user_id, hashed_password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET password = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?", (hashed_password, user_id))
    conn.commit()
    conn.close()

def delete_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()