# student-management-system
A web-based Student Management System built using Python Flask, SQLite, HTML, CSS and JavaScript.
# Student Management System

A web-based Student Management System built using Flask, SQLite, HTML, and CSS.

## Features

- Admin Login and Logout
- Add, View, Edit, and Delete Students
- Search Students
- Attendance Management
- Attendance History
- Marks Management
- Student Performance Reports
- Dashboard Statistics
- SQLite Database

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- Git and GitHub

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

## instalation
1.Clone the repository:
  git clone https://github.com/sureshbabu2006/student-management-system.git
2.Open the project folder:
   cd student-management-system
3.Create a virtual environment:
   python -m venv venv
4.Activate the virtual environment on Windows:
   venv\Scripts\activate
5.Install Flask:
   pip install flask werkzeug
6.Create the database:
   python database.py
7.Start the application:
   python app.py
8.Open the application in your browser:
   http://127.0.0.1:5000

## Database

The project uses SQLite for storing:

User accounts
Student information
Attendance records
Marks

The local database.db file is ignored by Git and is not uploaded to GitHub.

## Author

Sureshbabu