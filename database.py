import sqlite3
from werkzeug.security import generate_password_hash


def create_database():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    # Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Create default admin account
    password_hash = generate_password_hash("admin123")

    cursor.execute("""
        INSERT OR IGNORE INTO users (username, password)
        VALUES (?, ?)
    """, ("admin", password_hash))

    # Students table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            course TEXT,
            year INTEGER,
            date_of_birth TEXT,
            address TEXT
        )
    """)
        # Attendance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Present', 'Absent')),
            UNIQUE(student_id, date),
            FOREIGN KEY(student_id) REFERENCES students(id)
        )
    """)
    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("Database created successfully!")