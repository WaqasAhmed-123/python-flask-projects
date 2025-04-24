# Flask CRUD App with Multi-Role Authentication

A full-featured Flask-based web application that supports multi-role user access, secure authentication, blog management, and a clean Bootstrap 5 UI.

## Demo Link 
  https://www.youtube.com/watch?v=c9c74r-EMjo


## Features

- ✅ Multi-role authentication (admin, users)
- ✅ Role-based protected routes using custom Flask decorators
- ✅ Secure login system using Flask session
- ✅ Password hashing with Bcrypt
- ✅ Flask-WTF for form handling and validation
- ✅ Image upload and secure file handling (UUID + extension preservation)
- ✅ Jinja templating with layout support
- ✅ Modular routing using Blueprints
- ✅ SMTP email sending for password reset
- ✅ Encrypted URLs using Fernet (for secure password reset and route protection)
- ✅ Database seeding for default admin account
- ✅ Foreign key relationships (User - Blog)
- ✅ Global exception handling with custom 404 page
- ✅ Bootstrap 5 UI with flash messages and alerts


## Project Structure

```
flask_crud_app/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── routes/
│   ├── forms/
│   ├── services.py
│   ├── utils/
│   └── templates/
├── static/uploads/
├── templates/errors/404.html
├── .env
├── run.py
└── requirements.txt
```

## Tech Stack
- Python 3.10+
- Flask
- SQLite (can easily switch to PostgreSQL/MySQL)
- Flask-WTF
- Bcrypt
- Bootstrap 5
- jQuery
- SMTP (Gmail or other)
- Cryptography (Fernet)


## How to Run

1. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure `.env` file**
```env
APP_SECRET_KEY=your-secret-key
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
FERNET_KEY=generated-fernet-key
```

5. **Run the app**
```bash
python run.py
```

6. Visit following link;
```bash
http://localhost:5000
```

## Default Admin (Seeded)
- Email: `admin@gmail.com`
- Password: `admin@123`
