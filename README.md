# SQL Query Dashboard

The **SQL Query Dashboard** is an interactive tool for exploring databases and visualizing query results. Built with **Python, SQLite, and Matplotlib**, it allows users to run SQL queries, view results in tabular form, and generate customizable charts.

This project demonstrates practical skills in **database management, data visualization, and Python development**, while serving as a foundation for future extensions such as multi‑database support or natural language query input.

---

## Features

- Execute SQL queries against a local SQLite database.
- Display query results in a clean tabular format.
- Generate visualizations (bar, line, scatter, etc.) using Matplotlib.
- Interactive dashboard interface for switching between raw data and charts.
- Export charts for reporting.
- Local deployment with full documentation.

---

## Tech Stack

- **Language**: Python
- **Database**: SQLite
- **Visualization**: Matplotlib
- **Interface**: Streamlit or Tkinter (depending on phase)

---

## Project Structure

```
sql-query-dashboard/
│
├── data/                     # Sample databases and datasets
    ├──create_sample_db.py    #For populating the sample.db
│   └── sample.db
│
├── src/                      # Source code
│   ├── main.py               # Entry point for the dashboard
│   ├── query_runner.py       # SQL query execution logic
│   ├── visualizer.py         # Matplotlib visualization functions
│   └── interface.py          # Interactive UI (Streamlit/Tkinter)
│
├── docs/                     # Documentation for each phase
│   ├── Phase1_README.md
│   ├── Phase2_README.md
│   ├── Phase3_README.md
│   ├── Phase4_README.md
│   └── Phase5_README.md
│
├── tests/                    # Unit tests
│   └── test_query_runner.py
│
├── requirements.txt          # Python dependencies
├── README.md                 # Main project description (this file)
├── LICENSE
└── .gitignore                # Git ignore rules
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YourUsername/sql-query-dashboard.git
cd sql-query-dashboard
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
python src/main.py
```

---

## Roadmap

- **Phase 1**: Foundations & Setup
- **Phase 2**: Core Query Execution
- **Phase 3**: Visualization Layer
- **Phase 4**: Interactive Dashboard
- **Phase 5**: Deployment & Documentation

---

## License

This project is open‑source and available under the MIT License.
