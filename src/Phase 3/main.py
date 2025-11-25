# main.py
# SQL Query Dashboard – Phase 3 (UI + Visualization)

import streamlit as st
from query_runner import init_db, run_query
from visualizer import to_dataframe, plot_bar, plot_line, plot_pie

def main():
    st.title("SQL Query Dashboard – Phase 3")
    st.write("Run SQL queries against sample.db and view results as tables or charts.")

    # Initialize DB if missing
    init_db()

    # Query input
    query = st.text_area("Enter your SQL query:", "SELECT * FROM Students;")

    # Chart type selection
    chart_type = st.selectbox(
        "Choose visualization type:",
        ["None (Table Only)", "Bar Chart", "Line Chart", "Pie Chart"]
    )

    if st.button("Run Query"):
        rows, cols, error = run_query(query)
        if error:
            st.error(f"Error: {error}")
        else:
            df = to_dataframe(rows, cols)
            if df is not None:
                # Always show table
                st.dataframe(df, use_container_width=True)

                # Show chart if selected and columns are available
                if cols is not None and len(cols) >= 2:
                    if chart_type == "Bar Chart":
                        plot_bar(df, x_col=cols[0], y_col=cols[1], title="Bar Chart Result")
                    elif chart_type == "Line Chart":
                        plot_line(df, x_col=cols[0], y_col=cols[1], title="Line Chart Result")
                    elif chart_type == "Pie Chart":
                        plot_pie(df, category_col=cols[0], value_col=cols[1], title="Pie Chart Result")
            else:
                st.success("Query executed successfully (no results to display).")

    st.write("---")
    st.caption("SQL Query Dashboard | Phase 3 – Query Execution + Visualization")

if __name__ == "__main__":
    main()
