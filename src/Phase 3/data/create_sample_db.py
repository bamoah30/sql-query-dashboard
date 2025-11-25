import sqlite3

# Connect to (or create) sample.db inside the data folder
conn = sqlite3.connect("data/sample.db")
cursor = conn.cursor()

# Drop tables if they already exist (for reset purposes)
cursor.execute("DROP TABLE IF EXISTS Students;")
cursor.execute("DROP TABLE IF EXISTS Classes;")
cursor.execute("DROP TABLE IF EXISTS Attendance;")

# Create Classes table
cursor.execute("""
CREATE TABLE Classes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher TEXT NOT NULL
);
""")

# Create Students table
cursor.execute("""
CREATE TABLE Students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade REAL,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES Classes(id)
);
""")

# Create Attendance table
cursor.execute("""
CREATE TABLE Attendance (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    date TEXT,
    status TEXT,
    FOREIGN KEY (student_id) REFERENCES Students(id)
);
""")

# Insert sample data into Classes
cursor.executemany("""
INSERT INTO Classes (id, name, teacher) VALUES (?, ?, ?);
""", [
    (1, "Database Systems", "Dr. Mensah"),
    (2, "Robotics Fundamentals", "Dr. Owusu")
])

# Insert sample data into Students
cursor.executemany("""
INSERT INTO Students (id, name, age, grade, class_id) VALUES (?, ?, ?, ?, ?);
""", [
    (1, "Alice", 20, 85.5, 1),
    (2, "Bob", 22, 78.0, 2),
    (3, "Charlie", 21, 92.0, 1)
])

# Insert sample data into Attendance
cursor.executemany("""
INSERT INTO Attendance (id, student_id, date, status) VALUES (?, ?, ?, ?);
""", [
    (1, 1, "2025-11-20", "Present"),
    (2, 2, "2025-11-20", "Absent"),
    (3, 3, "2025-11-20", "Present")
])

# Commit changes and close connection
conn.commit()
conn.close()

print(" sample.db created successfully with sample data!")
