from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.secret_key = "change-this-secret-key"


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password"], password):

            session["user_id"] = user["id"]
            session["username"] = user["username"]

            return redirect(url_for("dashboard"))

        return "Invalid username or password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    total_students = connection.execute(
        "SELECT COUNT(*) FROM students"
    ).fetchone()[0]
    total_attendance = connection.execute(
    "SELECT COUNT(*) FROM attendance"
     ).fetchone()[0]
    total_marks = connection.execute(
    "SELECT COUNT(*) FROM marks"
).fetchone()[0]

    connection.close()

    return render_template(
    "dashboard.html",
    total_students=total_students,
    total_attendance=total_attendance,
    total_marks=total_marks
)
@app.route("/students")
def students():

    if "user_id" not in session:
        return redirect(url_for("login"))

    search = request.args.get("search", "").strip()

    connection = get_db_connection()

    if search:
     search_term = f"%{search}%"

     students = connection.execute("""
        SELECT * FROM students
        WHERE CAST(student_id AS TEXT) LIKE ?
           OR name LIKE ?
           OR email LIKE ?
           OR phone LIKE ?
           OR course LIKE ?
        ORDER BY id DESC
     """, (
        search_term,
        search_term,
        search_term,
        search_term,
        search_term
    )).fetchall()

    else:
        students = connection.execute("""
            SELECT * FROM students
            ORDER BY id DESC
        """).fetchall()

    connection.close()

    return render_template(
        "students.html",
        students=students,
        search=search
    )
@app.route("/students/add", methods=["GET", "POST"])
def add_student():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        course = request.form["course"]
        year = request.form["year"]
        date_of_birth = request.form["date_of_birth"]
        address = request.form["address"]

        connection = get_db_connection()

        connection.execute("""
            INSERT INTO students
            (student_id, name, email, phone, course, year, date_of_birth, address)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student_id,
            name,
            email,
            phone,
            course,
            year,
            date_of_birth,
            address
        ))

        connection.commit()
        connection.close()

        return redirect(url_for("students"))

    return render_template("add_student.html")
@app.route("/students/edit/<int:id>", methods=["GET", "POST"])
def edit_student(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    ).fetchone()

    if student is None:
        connection.close()
        return "Student not found", 404

    if request.method == "POST":

        student_id = request.form["student_id"]
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        course = request.form["course"]
        year = request.form["year"]
        date_of_birth = request.form["date_of_birth"]
        address = request.form["address"]

        connection.execute("""
            UPDATE students
            SET student_id = ?,
                name = ?,
                email = ?,
                phone = ?,
                course = ?,
                year = ?,
                date_of_birth = ?,
                address = ?
            WHERE id = ?
        """, (
            student_id,
            name,
            email,
            phone,
            course,
            year,
            date_of_birth,
            address,
            id
        ))

        connection.commit()
        connection.close()

        return redirect(url_for("students"))

    connection.close()

    return render_template(
        "edit_student.html",
        student=student
    )
@app.route("/students/delete/<int:id>", methods=["POST"])
def delete_student(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    connection.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect(url_for("students"))
@app.route("/attendance", methods=["GET", "POST"])
def attendance():

    if "user_id" not in session:
        return redirect(url_for("login"))

    selected_date = request.form.get("date") if request.method == "POST" else request.args.get("date", "")

    connection = get_db_connection()

    students = connection.execute("""
        SELECT * FROM students
        ORDER BY name ASC
    """).fetchall()

    if request.method == "POST" and selected_date:

        for student in students:

            status = request.form.get(
                f"status_{student['id']}"
            )

            if status:
                connection.execute("""
                    INSERT INTO attendance
                    (student_id, date, status)
                    VALUES (?, ?, ?)
                    ON CONFLICT(student_id, date)
                    DO UPDATE SET status = excluded.status
                """, (
                    student["id"],
                    selected_date,
                    status
                ))

        connection.commit()

    connection.close()

    return render_template(
        "attendance.html",
        students=students,
        selected_date=selected_date
    )
@app.route("/marks", methods=["GET", "POST"])
def marks():

    if "user_id" not in session:
        return redirect(url_for("login"))

    subject = (
        request.form.get("subject")
        if request.method == "POST"
        else request.args.get("subject", "")
    )

    connection = get_db_connection()

    students = connection.execute("""
        SELECT * FROM students
        ORDER BY name ASC
    """).fetchall()

    if request.method == "POST" and subject:

        for student in students:

            marks_value = request.form.get(
                f"marks_{student['id']}"
            )

            if marks_value:
                connection.execute("""INSERT INTO marks(student_id, subject, marks, max_marks)VALUES (?, ?, ?, 100)
                  ON CONFLICT(student_id, subject)
                 DO UPDATE SET marks = excluded.marks """, (student["id"], subject,marks_value
                 ))

        connection.commit()

    saved_marks = {}

    if subject:
        rows = connection.execute("""
            SELECT student_id, marks
            FROM marks
            WHERE subject = ?
        """, (subject,)).fetchall()

        for row in rows:
            saved_marks[row["student_id"]] = row["marks"]

    connection.close()

    return render_template(
        "marks.html",
        students=students,
        subject=subject,
        saved_marks=saved_marks
    )
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)