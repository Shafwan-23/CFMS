# Colege Facility Management System

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



