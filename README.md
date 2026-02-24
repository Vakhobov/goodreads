# Goodreads Clone (Django)

A Goodreads-inspired web application built with Django.  
This project allows users to browse books, create reviews, rate books, and manage personal reading lists.

The goal of this project is to practice backend development, database modeling, authentication, and building scalable Django applications.

---

## 🚀 Tech Stack

- Python
- Django
- SQLite / PostgreSQL
- Django ORM
- HTML / CSS
- Bootstrap 
- Git & GitHub

---

## ⚙️ Features

- User registration & authentication
- Book listing and detail pages
- Create, update, and delete reviews
- Book rating system
- User profile page
- Reading list management
- Admin panel for content management
- Pagination support

---

## 📂 Project Structure
- goodreads/
- │
- ├── books/ # Book management
- ├── reviews/ # Review system
- ├── users/ # Authentication & profiles
- ├── templates/ # HTML templates
- ├── static/ # CSS & static files
- ├── manage.py
= └── requirements.txt
## ▶️ How to Run

1. Clone the repository
    ```bash
    git clone https://github.com/Vakhobov/goodreads.git
2. Navigate to the project directory:
   ```bash
   cd goodreads
3. Create and activate virtual environment (recommended)
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```
   Or using venv
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux / macOS
   venv\Scripts\activate     # Windows
   ```
4. Install dependencies
   ```bash
   pip install -r requirements.txt

5. Apply migrations:
   ```bash
   python manage.py migrate
6. Run the development server
   ```bash
   python manage.py runserver
7. Open in browser
   ```bash
   http://127.0.0.1:8000/



---

## 🎯 Purpose of the Project

This project was built to strengthen knowledge in:

- Django framework fundamentals
- Database design & relationships
- Authentication systems
- CRUD operations
- Clean project architecture
- Backend logic implementation

---
