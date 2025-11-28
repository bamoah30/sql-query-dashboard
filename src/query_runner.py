# query_runner.py
# Handles database connection and query execution for SQL Query Dashboard

import sqlite3
import os

DB_PATH = "data/sample.db"  # default database
SQL_INIT_FILE = "init_sample.sql"

def set_db_path(path: str):
    """
    Update the global DB_PATH to point to a new database file.
    """
    global DB_PATH
    DB_PATH = path

def init_db():
    """
    Initialize the database if it doesn't exist.
    
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
    Execute a SQL query against the current DB_PATH.
    Returns rows, column names, and error message (if any).
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

def get_all_tables():
    """
    Return a list of all table names in the database.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tables

def dump_table(table_name: str):
    """
    Return all rows and columns from a given table.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        cols = [description[0] for description in cursor.description]
        conn.close()
        return rows, cols, None
    except Exception as e:
        conn.close()
        return None, None, str(e)

def get_table_columns(table_name: str):
    """
    Return a list of column names for a given table.
    Useful for dynamic query builders.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        cursor.execute(f"PRAGMA table_info({table_name});")
        cols = [row[1] for row in cursor.fetchall()]
        conn.close()
        return cols
    except Exception:
        conn.close()
        return []
