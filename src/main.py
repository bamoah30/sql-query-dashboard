# main.py
# SQL Query Dashboard – Phase 4 (UI + Upload Feature + Dynamic Query Builders + Database Explorer)

import streamlit as st
from query_runner import init_db, run_query, get_all_tables, dump_table, set_db_path
from visualizer import to_dataframe, plot_bar, plot_line, plot_pie
from interface import dynamic_query_builder, quick_table_viewer
import tempfile

def main():
    st.title("SQL Query Dashboard ")
    st.write("Run SQL queries against sample.db or upload your own SQLite database.")

    # -----------------------------
    # Section 0: Upload Database
    # -----------------------------
    st.subheader("Upload Your Own Database")
    uploaded_file = st.file_uploader("Upload a SQLite .db file", type=["db", "sqlite"])
    if uploaded_file is not None:
        # Save to a temporary file
        temp_db = tempfile.NamedTemporaryFile(delete=False, suffix=".db")
        temp_db.write(uploaded_file.read())
        temp_db.close()
        set_db_path(temp_db.name)
        st.success(f"Database switched to: {temp_db.name}")

    # Initialize DB if missing (default or uploaded)
    init_db()

    # -----------------------------
    # Section 1: Raw SQL Input
    # -----------------------------
    st.subheader("🔹 Raw SQL Query")
    query = st.text_area("Enter your SQL query:", "SELECT * FROM Students;")

    chart_type = st.selectbox(
        "Choose visualization type:",
        ["None (Table Only)", "Bar Chart", "Line Chart", "Pie Chart"]
    )

    if st.button("Run Raw SQL"):
        rows, cols, error = run_query(query)
        if error:
            st.error(f"Error: {error}")
        else:
            df = to_dataframe(rows, cols)
            if df is not None and cols is not None:
                st.dataframe(df, use_container_width=True)
                if chart_type == "Bar Chart" and len(cols) >= 2:
                    plot_bar(df, x_col=cols[0], y_col=cols[1], title="Bar Chart Result")
                elif chart_type == "Line Chart" and len(cols) >= 2:
                    plot_line(df, x_col=cols[0], y_col=cols[1], title="Line Chart Result")
                elif chart_type == "Pie Chart" and len(cols) >= 2:
                    plot_pie(df, category_col=cols[0], value_col=cols[1], title="Pie Chart Result")
            else:
                st.success("Query executed successfully (no results to display).")

    # -----------------------------
    # Section 2: Dynamic Query Builders
    # -----------------------------
    st.subheader(" Dynamic Query Builders (Works with Uploaded DBs)")

    # Dynamic filter builder
    dynamic_query = dynamic_query_builder()
    if dynamic_query:
        st.write("Generated SQL:", dynamic_query)
        rows, cols, error = run_query(dynamic_query)
        if not error:
            df = to_dataframe(rows, cols)
            if df is not None:
                st.dataframe(df, use_container_width=True)

    # Quick table viewer
    quick_query = quick_table_viewer()
    if quick_query:
        st.write("Generated SQL:", quick_query)
        rows, cols, error = run_query(quick_query)
        if not error:
            df = to_dataframe(rows, cols)
            if df is not None:
                st.dataframe(df, use_container_width=True)

    # -----------------------------
    # Section 3: Explore Entire Database
    # -----------------------------
    st.subheader(" Explore Entire Database")
    if st.button("Show All Tables"):
        tables = get_all_tables()
        st.write("Tables found:", tables)

        for table in tables:
            st.write(f"### Table: {table}")
            rows, cols, error = dump_table(table)
            if error:
                st.error(f"Error reading {table}: {error}")
            else:
                if rows:
                    df = to_dataframe(rows, cols)
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info(f"{table} is empty.")

    st.write("---")
    st.caption("SQL Query Dashboard | Dynamic Query Builders + Database Explorer + Upload Feature")

if __name__ == "__main__":
    main()
