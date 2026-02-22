# 📝 Note Taker Web Application

## 📌 Project Overview

Note Taker is a web-based application built using **Flask** and **SQL** that allows users to securely create, manage, and store personal notes.  

The application demonstrates backend development concepts including user authentication, database integration, CRUD operations, and structured application architecture using Flask Blueprints.

---

## 🚀 Features

- User Registration & Login Authentication
- Secure Session Management
- Create, Read, Update, Delete (CRUD) Notes
- Database Integration using SQL
- Modular Flask Application Structure
- Organized Templates & Static Files

---

## 🛠️ Technologies Used

- Python
- Flask
- SQL (SQLite / PostgreSQL depending on configuration)
- HTML5
- CSS3
- Jinja2 Templating Engine

---

## 📂 Project Structure

```
project-root/
│
├── website/
│   ├── __pycache__/
│   ├── static/              # CSS, JS, Images
│   ├── templates/           # HTML Templates
│   ├── __init__.py          # App factory
│   ├── auth.py              # Authentication routes
│   ├── models.py            # Database models
│   └── views.py             # Application routes
│
├── .gitignore
├── config.ini               # Configuration settings
├── main.py                  # Entry point of application
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone <your-repository-url>
cd <project-folder>
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 5️⃣ Run Application
```bash
python main.py
```

Application will run on:
```
http://127.0.0.1:5000
```

---

## 🗄️ Database Design

The application uses SQL-based relational database with:

- User Model
- Notes Model
- Relationship between Users and Notes

Each user can create and manage their own notes securely.

---

## 🔐 Authentication Flow

- User registers with email and password
- Password is securely stored (hashed)
- Session management maintains login state
- Logout functionality clears session

---

## 🎯 Learning Outcomes

- Flask application factory pattern
- Blueprints for modular routing
- SQL database modeling
- Authentication & session handling
- CRUD implementation in web apps
- Project structuring for scalability

---

## 🔮 Future Improvements

- Add password reset functionality
- Implement REST API endpoints
- Add pagination for notes
- Deploy to cloud (Render / AWS / Azure)
- Add Docker support

---

## 👨‍💻 Author

Pratik Vishwas Salunkhe

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.
