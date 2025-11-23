# SQL Query Dashboard – Phase 2

**Core Query Execution**

## Overview

Phase 2 upgrades the dashboard from a simple placeholder (Phase 1) into a working **SQL query runner**.  
At this stage, the app connects to a local SQLite database (`sample.db`), accepts SQL queries from the user, executes them, and displays results in a clean table format.

We’ve refactored the project to separate responsibilities:

- **`main.py`** → Streamlit UI (inputs, buttons, displaying results).
- **`query_runner.py`** → Database logic (connection, query execution, error handling).

This modular design makes the project easier to maintain and sets the foundation for Phase 3 (`visualizer.py`) and Phase 4 (`interface.py`).

---

## Features

- Connects automatically to `sample.db` (created in Phase 2 setup).
- Accepts SQL queries via a Streamlit text area.
- Executes queries safely using Python’s built‑in `sqlite3` module.
- Displays results in a table (`st.dataframe`).
- Handles errors gracefully (invalid queries show error messages).
- Auto‑initializes `sample.db` from `init_sample.sql` if missing.
- Clean separation of **UI vs backend logic** via `query_runner.py`.

---

## Setup Instructions

1. **Install dependencies**

   ```bash
   pip install streamlit
   ```

   _(No need to install SQLite — Python includes `sqlite3` by default.)_

2. **Create the database**

   - Option A: Run the Python script
     ```bash
     python create_sample_db.py
     ```
   - Option B: Use the SQL script
     ```bash
     python -c "import sqlite3; conn=sqlite3.connect('data/sample.db'); conn.executescript(open('init_sample.sql').read()); conn.close()"
     ```

3. **Run the dashboard**
   ```bash
   streamlit run src/main.py
   ```

---

## Example Queries

Try these inside the dashboard:

- Show all students:

  ```sql
  SELECT * FROM Students;
  ```

- Average grade per class:

  ```sql
  SELECT class_id, AVG(grade) AS avg_grade
  FROM Students
  GROUP BY class_id;
  ```

- Join students with classes:
  ```sql
  SELECT Students.name, Classes.name AS class, Classes.teacher
  FROM Students
  JOIN Classes ON Students.class_id = Classes.id;
  ```

---

## Next Steps

- **Phase 3** → Add visualizations (bar charts, line graphs) for query results via `visualizer.py`.
- **Phase 4** → Build interactive filters and query templates via `interface.py`.
