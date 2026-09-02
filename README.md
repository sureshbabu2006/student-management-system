# Student Management System

A web-based Student Management System built using **Python, Flask, SQLite, HTML, CSS, and JavaScript**.

## Features

- **Admin Login and Logout**
- **Student Management** — Add, view, edit, and delete students
- **Student Search** — Search students by ID, name, email, or course
- **Attendance Management** — Mark and update daily attendance
- **Attendance History** — View attendance records for each student
- **Marks Management** — Add and update subject marks
- **Student Performance Reports** — View marks, percentages, and attendance performance
- **Dashboard Statistics** — View student, attendance, and marks statistics

## Technologies Used

- **Python**
- **Flask**
- **SQLite**
- **HTML**
- **CSS**
- **JavaScript**
- **Git & GitHub**

## Installation

### Clone the Repository

```bash
git clone https://github.com/sureshbabu2006/student-management-system.git
```

### Open the Project Folder

```bash
cd student-management-system
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### Install Required Packages

```bash
pip install flask werkzeug
```

### Create the Database

```bash
python database.py
```

### Start the Application

```bash
python app.py
```

### Open the Application

Open this address in your browser:

```text
http://127.0.0.1:5000
```

## Database

The application uses **SQLite** to store:

- User accounts
- Student information
- Attendance records
- Marks

The local `database.db` file is ignored by Git and is not uploaded to GitHub.

## Project Structure

```text
student-management-system/
│
├── app.py
├── database.py
├── README.md
├── LICENSE
├── .gitignore
│
├── static/
│   └── css/
│       └── style.css
│
└── templates/
    ├── login.html
    ├── dashboard.html
    ├── students.html
    ├── add_student.html
    ├── edit_student.html
    ├── student_details.html
    ├── attendance.html
    ├── attendance_history.html
    ├── marks.html
    └── student_performance.html
```

## Author

**Sureshbabu**