# 📝 Django Todo List

A simple **To-Do List** web application developed using **Django** and **MySQL**. This project allows users to manage their daily tasks with basic CRUD (Create, Read, Update, Delete) operations.

---

## 📌 Project Overview

The Todo List application helps users organize and manage their daily activities. Users can add new tasks, view all tasks, update existing tasks, and delete completed or unwanted tasks.

---

## ✨ Features

- ➕ Add New Task
- 📋 View All Tasks
- ✏️ Edit Existing Task
- 🗑️ Delete Task
- ✅ Task Status (Pending / Completed)
- ❌ Cancel button redirects to Home Page
- 💾 Data stored in MySQL Database

---

## 🛠️ Technologies Used

- Python 3
- Django 5
- MySQL
- HTML5
- CSS3

---

## 📂 Project Structure

```
todo_project/
│
├── todo_project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
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
│   └── admin.py
│
├── manage.py
└── README.md
```

---

## 🗄️ Database

Database: **MySQL**

Table: **Todo**

### Fields

| Field | Type |
|-------|------|
| id | Auto Increment |
| tasktitle | CharField |
| taskdesc | TextField |
| status | CharField |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/todo-project.git
```

### Move to project directory

```bash
cd todo_project
```

### Install Django

```bash
pip install django
```

### Install MySQL Client

```bash
pip install mysqlclient
```

---

## 🔧 Configure Database

Update **settings.py**

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'tododb',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 📦 Apply Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

## ▶️ Run the Project

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## 📷 Application Workflow

1. Open Home Page
2. Click **Add New Task**
3. Enter Task Details
4. Save Task
5. View Task List
6. Edit Task
7. Delete Task

---

## 📚 CRUD Operations

### Create
Adds a new task to the database.

### Read
Displays all tasks.

### Update
Modifies task details.

### Delete
Removes a task from the database.

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Django Project Structure
- Django Models
- URL Routing
- Views
- Templates
- CRUD Operations
- MySQL Database Integration
- Static Files (CSS)
- Form Handling
- Redirects

---

## 🚀 Future Enhancements

- User Authentication
- Search Tasks
- Due Date
- Task Priority
- Categories
- Dashboard
- Responsive Design
- Dark Mode

---

## 👨‍💻 Author

**T. Lokitha**

B.Tech – Artificial Intelligence & Machine Learning

Python & Django Developer

GitHub: https://github.com/Lokitha10

---

## 📄 License

This project is developed for learning and educational purposes.
