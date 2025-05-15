# CFMS
Here's a well-structured `README.md` file for your Flask-based Facility Management System, suitable for a GitHub repository:

---

```markdown
# Facility Management System

A role-based web application built with **Flask** and **MySQL** to manage university or organizational facilities, maintenance requests, asset tracking, announcements, and bookings. Supports three types of users: **Admin**, **Student**, and **Maintenance Staff**.

---

## 🔧 Features

### 👤 Authentication & Session
- User registration and login
- Role-based session handling (Admin, Student, Maintenance)
- Flash messaging for user feedback

### 🛠 Admin Panel
- **Dashboard:** Overview of users, facilities, and pending maintenance
- **User Management:** Add, update, and delete users
- **Facility Management:** Create and delete facilities
- **Maintenance Management:** Assign requests, update status
- **Asset Management:** Track and manage assets
- **Reports:** View usage reports of facilities
- **Announcements:** Post and view announcements

### 🎓 Student Dashboard
- View available facilities
- Book facilities (pending approval)
- Raise maintenance issues
- Track status of raised issues
- View admin announcements

### 🔧 Maintenance Dashboard
- View assigned maintenance requests
- Update request status and comments

---

## 🛠 Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** MySQL (via `flask-mysqldb`)
- **Session Management:** Flask sessions
- **Flash Messaging:** Flask Flash

---

## 📁 Project Structure (simplified)

```

├── templates/
│   ├── login.html
│   ├── register.html
│   ├── admin/
│   ├── student/
│   └── maintenance/
├── static/
├── app.py
├── config.py
└── requirements.txt

````

---

## 🔒 Roles & Permissions

| Role         | Permissions                                                                 |
|--------------|------------------------------------------------------------------------------|
| Admin        | Full control: users, facilities, maintenance, assets, reports, announcements |
| Student      | Book facilities, raise/view maintenance issues, view announcements           |
| Maintenance  | View and update assigned maintenance requests                                 |

---

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/facility-management-system.git
cd facility-management-system
````

### 2. Create & Configure `config.py`

```python
# config.py
MYSQL_HOST = 'localhost'
MYSQL_USER = 'your_user'
MYSQL_PASSWORD = 'your_password'
MYSQL_DB = 'your_database'
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

---

## 🗃️ Database Tables (Required)

Ensure you create the following tables in your MySQL database:

* `users`
* `facilities`
* `maintenance_requests`
* `bookings`
* `assets`
* `announcements`

(*Add table creation SQLs as needed in a `schema.sql` file*)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Contributions

Feel free to fork, open issues, or submit pull requests. Your feedback is welcome!

```

---

Let me know if you'd like me to generate a `requirements.txt` file or SQL schema (`schema.sql`) based on your code.
```
