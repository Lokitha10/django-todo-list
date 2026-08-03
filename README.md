# 📝 Django Todo List

A simple and user-friendly **To-Do List Web Application** developed using **Django**, **Python**, **SQLite**, **HTML**, and **CSS**. This application helps users create, manage, update, and delete daily tasks efficiently.

---

## 📌 Project Description

The Django Todo List is a CRUD-based web application that allows users to organize their daily activities. Users can add new tasks, edit existing tasks, delete completed tasks, and monitor their task status.

---

## 🚀 Features

- ➕ Add New Task
- 📋 View All Tasks
- ✏️ Edit Existing Task
- 🗑️ Delete Task
- ✅ Update Task Status
- ❌ Cancel Button (Redirects to Home Page)
- 🎨 Simple and Clean User Interface
- 💾 SQLite Database Integration

---

## 🛠️ Technologies Used

- Python 3
- Django 5
- SQLite3
- HTML5
- CSS3

---

## 📁 Project Structure

```
todo_project/
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── todo_app/
│   ├── migrations/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   ├── index.html
│   │   ├── addtask.html
│   │   └── edit.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

## 🗄️ Database

**Database:** SQLite

### Todo Model

| Field | Type |
|--------|------|
| id | Auto Increment |
| tasktitle | CharField(100) |
| taskdesc | TextField |
| status | CharField(20) |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Lokitha10/django-todo-list.git
```

### Move into Project

```bash
cd django-todo-list
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📷 Application Workflow

1. Home Page
2. Click **Add New Task**
3. Enter Task Details
4. Save Task
5. View All Tasks
6. Edit Task
7. Update Task
8. Delete Task

---

## CRUD Operations

### ➕ Create

Creates a new task and stores it in the database.

### 📖 Read

Displays all available tasks.

### ✏️ Update

Updates task title, description, and status.

### 🗑️ Delete

Deletes the selected task from the database.

---

## 🎯 Learning Outcomes

This project helped in learning:

- Django Project Structure
- Django Models
- URL Routing
- Views
- Templates
- Static Files
- Form Handling
- CRUD Operations
- SQLite Database
- Git & GitHub
- Render Deployment

---

## 🌟 Future Enhancements

- User Authentication
- Task Priority
- Due Date
- Search Tasks
- Filter by Status
- Responsive Design
- Dark Mode
- User Dashboard

---

## 👨‍💻 Author

**T. Lokitha**

- Python Developer
- Django Developer
- Artificial Intelligence & Machine Learning Student

**GitHub**

https://github.com/Lokitha10

---

## 📄 License

This project is developed for educational and learning purposes.
