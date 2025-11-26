# SQL Query Dashboard – Phase 4

**Interactive Query Builders & Enhanced UX**

## Overviewv

Phase 4 transforms the dashboard from a raw SQL playground into a more **user-friendly interface**.  
Users can now either type SQL queries manually _or_ use **interactive forms, dropdowns, and filters** that automatically generate queries behind the scenes.

We’ve expanded the modular design:

- **`main.py`** → Streamlit UI (raw SQL input, table display, chart selection, interactive forms).
- **`query_runner.py`** → Database logic (connection, query execution, error handling).
- **`visualizer.py`** → Visualization logic (converting query results into charts).
- **`interface.py`** → Interactive query builders (forms, dropdowns, filters).

---

## Features

- All Phase 3 features (query runner, error handling, table + chart display).
- New **interactive query builders** via `interface.py`:
  - **Student filter form** → filter students by grade threshold.
  - **Class filter form** → dropdown to select a class and show its students.
  - **Attendance filter form** → date range filter for attendance records.
- Automatic SQL generation based on user selections.
- Seamless integration with `query_runner.py` and `visualizer.py`.

---

## Setup Instructions

1. **Install dependencies**

   ```bash
   pip install streamlit pandas matplotlib altair
   ```

2. **Ensure database exists**

   - If not already created, run Phase 2 setup (`create_sample_db.py` or `init_sample.sql`).

3. **Run the dashboard**
   ```bash
   streamlit run main.py
   ```

---

## Example Interactive Queries

With `interface.py`, users can now run queries without typing SQL:

- **Student filter form**: Enter minimum grade → generates

  ```sql
  SELECT * FROM Students WHERE grade >= 80;
  ```

- **Class filter form**: Select “Robotics” → generates

  ```sql
  SELECT * FROM Students WHERE class_id = 2;
  ```

- **Attendance filter form**: Pick January 2025 → generates
  ```sql
  SELECT * FROM Attendance WHERE date BETWEEN '2025-01-01' AND '2025-01-31';
  ```

---

## Next Steps

- **Phase 5 (Future)** → Add authentication and role-based dashboards (e.g., teacher vs student views).
- Export query results and charts to CSV/PDF.
- Integrate with external databases beyond SQLite.
