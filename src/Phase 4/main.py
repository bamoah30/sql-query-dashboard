# main.py
# SQL Query Dashboard – Phase 4 (UI + Interactive Query Builders)

import streamlit as st
from query_runner import init_db, run_query
from visualizer import to_dataframe, plot_bar, plot_line, plot_pie
from interface import student_filter_form, class_filter_form, attendance_filter_form

def main():
    st.title("SQL Query Dashboard – Phase 4")
    st.write("Run SQL queries against sample.db using raw SQL or interactive query builders.")

    # Initialize DB if missing
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
    # Section 2: Interactive Query Builders
    # -----------------------------
    st.subheader("🔹 Interactive Query Builders")

    # Student filter form (e.g., grade threshold)
    student_query = student_filter_form()
    if student_query:
        st.write("Generated SQL:", student_query)
        rows, cols, error = run_query(student_query)
        if error:
            st.error(f"Error: {error}")
        else:
            df = to_dataframe(rows, cols)
            if df is not None:
                st.dataframe(df, use_container_width=True)

    # Class filter form (dropdown for class selection)
    class_query = class_filter_form()
    if class_query:
        st.write("Generated SQL:", class_query)
        rows, cols, error = run_query(class_query)
        if error:
            st.error(f"Error: {error}")
        else:
            df = to_dataframe(rows, cols)
            if df is not None:
                st.dataframe(df, use_container_width=True)

    # Attendance filter form (date range)
    attendance_query = attendance_filter_form()
    if attendance_query:
        st.write("Generated SQL:", attendance_query)
        rows, cols, error = run_query(attendance_query)
        if error:
            st.error(f"Error: {error}")
        else:
            df = to_dataframe(rows, cols)
            if df is not None:
                st.dataframe(df, use_container_width=True)

    st.write("---")
    st.caption("SQL Query Dashboard | Phase 4 – Raw SQL + Interactive Query Builders")

if __name__ == "__main__":
    main()
