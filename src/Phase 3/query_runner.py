# query_runner.py
# Handles database connection and query execution for SQL Query Dashboard

import sqlite3
import os

DB_PATH = "data/sample.db"
SQL_INIT_FILE = "init_sample.sql"

def init_db():
    """
    Initialize the database if it doesn't exist.
    If sample.db is missing, create it and populate using init_sample.sql (if available).
    """
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        if os.path.exists(SQL_INIT_FILE):
            with open(SQL_INIT_FILE, "r") as f:
                cursor.executescript(f.read())
        conn.commit()
        conn.close()

def run_query(query: str):
    """
    Execute a SQL query against sample.db.
    Returns:
        - rows: list of tuples with query results
        - cols: list of column names (if applicable)
        - error: error message string if query fails
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        cols = [description[0] for description in cursor.description] if cursor.description else []
        conn.close()
        return rows, cols, None
    except Exception as e:
        conn.close()
        return None, None, str(e)
