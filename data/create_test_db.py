# create_test_db.py
# Script to generate a new SQLite database for testing Phase 4 upload feature

import sqlite3

# Name of the new database file
DB_NAME = "test_upload.db"

# Connect to the new database (creates file if not exists)
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# -----------------------------
# Create tables
# -----------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT,
    budget REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Assignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_id INTEGER,
    project_id INTEGER,
    role TEXT,
    FOREIGN KEY(employee_id) REFERENCES Employees(id),
    FOREIGN KEY(project_id) REFERENCES Projects(id)
);
""")

# -----------------------------
# Insert sample data
# -----------------------------
employees = [
    ("Alice Johnson", "Engineering", 75000),
    ("Bob Smith", "Marketing", 60000),
    ("Charlie Brown", "Engineering", 80000),
    ("Diana Prince", "HR", 50000)
]
cursor.executemany("INSERT INTO Employees (name, department, salary) VALUES (?, ?, ?);", employees)

projects = [
    ("AI Research", "2025-01-01", "2025-06-30", 200000),
    ("Robotics Upgrade", "2025-02-15", "2025-12-31", 500000),
    ("Marketing Campaign", "2025-03-01", None, 100000)
]
cursor.executemany("INSERT INTO Projects (project_name, start_date, end_date, budget) VALUES (?, ?, ?, ?);", projects)

assignments = [
    (1, 1, "Lead Engineer"),
    (2, 3, "Campaign Manager"),
    (3, 2, "Robotics Specialist"),
    (4, 1, "HR Coordinator")
]
cursor.executemany("INSERT INTO Assignments (employee_id, project_id, role) VALUES (?, ?, ?);", assignments)

# Commit and close
conn.commit()
conn.close()

print(f"Database '{DB_NAME}' created successfully with sample data!")
