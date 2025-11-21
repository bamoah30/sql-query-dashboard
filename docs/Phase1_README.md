# Phase 1 – Foundations & Setup

## Project Scope

The **SQL Query Dashboard** is an interactive tool for database exploration and visualization.

- **Purpose**: Allow users to run SQL queries against a local SQLite database and view results in both tabular and graphical formats.
- **Phase 1 Focus**: Establish the environment, initialize the repository, and prepare the foundation for query execution and visualization.
- **Vision**: Build a portfolio‑ready project that demonstrates skills in database management, data visualization, and Python development, with potential extensions to multi‑database support and natural language query input.

---

## Environment Setup

1. **Virtual Environment**

   - Created a Python virtual environment (`venv`) for isolated dependencies.
   - Selected the interpreter in VS Code to ensure reproducibility.

2. **Dependencies Installed**

   - `pandas` – for handling query results as DataFrames.
   - `matplotlib` – for core plotting.
   - `seaborn` – optional, for polished statistical visualizations.
   - `streamlit` – for building the interactive dashboard.
   - `python-dotenv` – for environment variable management.

3. **Repository Initialization**
   - Initialized Git locally (`git init`).
   - Created a new repository on GitHub and connected the local folder.
   - Cloned the repository for active development.

---

## Minimum Viable Product (MVP)

The MVP for this project is a **local dashboard** that:

- Connects to a SQLite database.
- Accepts SQL queries from the user.
- Displays query results in a tabular format.
- Generates at least one visualization (bar chart) from query results.
- Runs locally via Streamlit with clear documentation for setup and usage.

---

## Next Steps (Phase 2 Preview)

- Implement the SQL query runner connected to SQLite.
- Add error handling for invalid queries.
- Display raw query results in tabular format.
- Document usage examples for basic queries.
