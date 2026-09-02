Student Management System

A web-based Student Management System built using Python, Flask, SQLite, HTML, CSS and JavaScript.

Features
Admin Login and Logout
Add, View, Edit, and Delete Students
Search Students
Attendance Management
Attendance History
Marks Management
Student Performance Reports
Dashboard Statistics
Technologies Used
Python
Flask
SQLite
HTML
CSS
JavaScript
Git and GitHub
Installation

Clone the repository

git clone https://github.com/sureshbabu2006/student-management-system.git

Open the project folder

cd student-management-system

Create a virtual environment

python -m venv venv

Activate the virtual environment on Windows

venv\Scripts\activate

Install required packages

pip install flask werkzeug

Create the database

python database.py

Start the application

python app.py

Open the application

http://127.0.0.1:5000

Database

The project uses SQLite to store:

User accounts
Student information
Attendance records
Marks

The local database.db file is ignored by Git and is not uploaded to GitHub.

Project Structure

student-management-system/

├── app.py
├── database.py
├── README.md
├── LICENSE
├── .gitignore
│
├── static/
│ └── css/
│ └── style.css
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

Author

Sureshbabu