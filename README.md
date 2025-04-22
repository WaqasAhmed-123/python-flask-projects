# Python Flask Learning Projects

This repository contains various hands-on learning projects built using **Python and Flask**. Each folder focuses on a specific concept such as routing, templates, CRUD operations, database handling, and Flask application structure.

## Note
Each project is placed in its own folder at the root level, prefixed with a number for easy navigation and learning progression.

## About

This repository showcases a wide range of backend concepts in **Python Flask**, perfect for beginners and intermediate developers looking to strengthen their web development skills. Topics covered include **Flask fundamentals, Jinja templating, SQLite/SQLAlchemy integration, REST-style routing, blueprints, and structured application architecture**. These mini-projects are ideal for practical learning and future reference.


## Projects Included

1. **Hello App** – Introduction to Python programming including variables, conditions, functions, data types, loops, and module imports.

2. **File Handling** – Working with file operations using Python's `os` module.

3. **Flask Basic** – Building a simple *Flask* app with parameterized routes.

4. **View Templates** – Using *Flask* Jinja templates to render dynamic HTML pages with data passing.

5. **Blueprints** – Modularizing routes using *Flask* blueprints for cleaner project structure.

6. **Basic DRUD (SQLAlchemy)** – Creating basic DRUD (Create, Read, Update, Delete) operations in *Flask* using SQLAlchemy with Jinja templates and blueprints.

7. **Basic CRUD (SQLite)** – Implementing full CRUD operations using SQLite in *Flask*.

8. **Basic CRUD (structured SQLite)** – Performing structured CRUD operations using models with SQLite database in *Flask*.

9. **Blog App** – A full-featured blog application showcasing real-world *Flask* development practices. Includes:

   - **Multi-role authentication** (admin, users)
   - **Role-based route protection** using custom Flask decorators
   - **Secure login system** using Flask session management
   - **Password hashing** with Bcrypt for enhanced security
   - **Flask-WTF** for robust form handling and validation
   - **Image uploads** with secure file handling (UUID + extension preservation)
   - **Jinja templating** with base layouts and inheritance support
   - **Blueprints** for modular route organization
   - **SMTP email integration** for password reset workflows
   - **Encrypted URLs** using Fernet for secure token-based actions
   - **Database seeding** to auto-create a default admin account
   - **Relational database modeling** (User ↔ Blog) with foreign key constraints
   - **Custom 404 error page** with global exception handling
   - **Bootstrap 5 UI** featuring flash messages, alerts, and responsive design



## Technologies Used

- **Python 3.x**
- **Flask**
- **Jinja2 Templates**
- **SQLite**
- **SQLAlchemy**
- **Blueprints (Modular Flask Apps)**
- **OS Module for File Handling**


## Setup Instructions

1. Clone the Repository
  ```sh
  git clone https://github.com/WaqasAhmed-123/python-flask-projects.git
  ```
2. Navigate to any project folder
  ```sh
  cd "1) Hello App"
  ```
3. Create a virtual environment
  ```sh
  python -m venv venv
  source venv/bin/activate  # Windows: venv\Scripts\activate
  ```
4. Install dependencies
  ```sh
  pip install -r requirements.txt
  ```
5. Configure `.env` file (if required)
  ```env
  APP_SECRET_KEY=your-secret-key
  MAIL_SERVER=smtp.gmail.com
  MAIL_PORT=587
  MAIL_USE_TLS=True
  MAIL_USERNAME=your-email@gmail.com
  MAIL_PASSWORD=your-app-password
  FERNET_KEY=generated-fernet-key
  ```
6. Run the project
  ```sh
  Flask run -debug
  ```
  

## Contact
For any queries, reach out via:
- GitHub: [WaqasAhmed-123](https://github.com/WaqasAhmed-123)
- Email: waqaxahmed786@gmail.com