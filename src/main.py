# main.py
# SQL Query Dashboard – Phase 2 (Refactored to use query_runner.py)

import streamlit as st
from query_runner import init_db, run_query

def main():
    st.title("SQL Query Dashboard – Phase 2")
    st.write("Run SQL queries against sample.db and view results.")

    # Initialize DB if missing
    init_db()

    # Query input
    query = st.text_area("Enter your SQL query:", "SELECT * FROM Students;")

    if st.button("Run Query"):
        rows, cols, error = run_query(query)
        if error:
            st.error(f"Error: {error}")
        else:
            if cols:
                st.dataframe(rows, use_container_width=True)
                st.caption(f"Columns: {', '.join(cols)}")
            else:
                st.success("Query executed successfully (no results to display).")

    st.write("---")
    st.caption("SQL Query Dashboard | Phase 2 – Query Execution")

if __name__ == "__main__":
    main()
