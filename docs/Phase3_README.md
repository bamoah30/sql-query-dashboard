# SQL Query Dashboard – Phase 3

**Data Visualization (Refactored)**

## Overview

Phase 3 extends the dashboard beyond simple query execution.  
At this stage, the app not only runs SQL queries against `sample.db` but also transforms results into **visualizations** (bar charts, line charts, pie charts, etc.).

We’ve refactored the project to keep responsibilities modular:

- **`main.py`** → Streamlit UI (query input, table display, chart selection).
- **`query_runner.py`** → Database logic (connection, query execution, error handling).
- **`visualizer.py`** → Visualization logic (converting query results into charts).

---

## Features

- All Phase 2 features (query runner, error handling, table display).
- New **visualization support**:
  - Bar charts (e.g., average grades per class).
  - Line charts (e.g., attendance trends over time).
  - Pie charts (e.g., distribution of students per class).
- Chart type selection via a **Streamlit dropdown**.
- Modular design: `visualizer.py` keeps plotting logic separate from UI.

---

## Setup Instructions

1. **Install dependencies**

   ```bash
   pip install streamlit pandas matplotlib altair
   ```

   _(Altair is used for interactive charts; Matplotlib is available for static plots.)_

2. **Ensure database exists**

   - If not already created, run Phase 2 setup (`create_sample_db.py` or `init_sample.sql`).

3. **Run the dashboard**
   ```bash
   streamlit run src/main.py
   ```

---

## Example Queries + Visualizations

Try these inside the dashboard:

- **Bar Chart**: Average grade per class

  ```sql
  SELECT class_id, AVG(grade) AS avg_grade
  FROM Students
  GROUP BY class_id;
  ```

- **Line Chart**: Attendance trend over time

  ```sql
  SELECT date, COUNT(*) AS total
  FROM Attendance
  GROUP BY date
  ORDER BY date;
  ```

- **Pie Chart**: Student distribution per class
  ```sql
  SELECT class_id, COUNT(*) AS student_count
  FROM Students
  GROUP BY class_id;
  ```

---

## Next Steps

- **Phase 4** → Introduce `interface.py` for interactive query builders (dropdowns, filters, forms).
- Improve UX with query templates and dynamic dashboards.
- Add export options for charts and query results.
