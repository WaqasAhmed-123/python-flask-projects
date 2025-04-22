import os
import uuid
from werkzeug.utils import secure_filename
from app.database import get_db_connection

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

def get_blogs(user_id = None):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if user_id is not None:
        cursor.execute('''
            SELECT 
                b.*, 
                u.name AS auther 
            FROM blogs b
            JOIN users u ON b.user_id = u.id
            WHERE b.user_id = ?
        ''', (user_id,))
    else:
        cursor.execute('''
            SELECT 
                b.*, 
                u.name AS auther 
            FROM blogs b
            JOIN users u ON b.user_id = u.id
        ''')


    blogs = cursor.fetchall()
    conn.close()
    return blogs


def get_blog_count(user_id = None):
    print(user_id)
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if user_id:
        cursor.execute("SELECT COUNT(*) FROM blogs WHERE user_id = ?", (user_id,))
    else:
        cursor.execute("SELECT COUNT(*) FROM blogs")

    count = cursor.fetchone()[0]
    conn.close()
    return count


def get_blog_by_id(blog_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT b.*, u.name AS author 
        FROM blogs b 
        JOIN users u ON b.user_id = u.id 
        WHERE b.id = ?
        """, (blog_id,))
    
    blog = cursor.fetchone()
    conn.close()
    return blog


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def add_blog(user_id, title, content, image_file=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    image_path = None
    # Handle Image Upload
    if image_file and allowed_file(image_file.filename):
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
            
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4().hex}_{filename}")
        image_file.save(image_path)

    cursor.execute(
        "INSERT INTO blogs (user_id, title, content, image_path) VALUES (?, ?, ?, ?)",
        (user_id, title, content, image_path)
    )

    conn.commit()
    conn.close()


def update_blog(id, title, content, image_file=None, previous_file=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    image_path = None
    # Handle Image Upload
    if image_file and allowed_file(image_file.filename):
        #removing old image
        if previous_file and os.path.exists(previous_file):
            os.remove(previous_file)

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
            
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(UPLOAD_FOLDER, f"{uuid.uuid4().hex}_{filename}")
        image_file.save(image_path)
    else:
        image_path = previous_file if previous_file else None

    cursor.execute("UPDATE blogs SET title=?, content=?, image_path=?, updated_at=CURRENT_TIMESTAMP WHERE id=?", 
    (title, content, image_path, id))

    conn.commit()
    conn.close()


def delete_blog(blog_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT image_path FROM blogs WHERE id=?", (blog_id,))
    blog = cursor.fetchone()

    if blog and blog['image_path']:
        image_path = blog['image_path']
        if os.path.exists(image_path):
            os.remove(image_path)

    cursor.execute("DELETE FROM blogs WHERE id=?", (blog_id,))
    conn.commit()
    conn.close()