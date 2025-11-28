# interface.py
# Dynamic interactive query builders for SQL Query Dashboard – Phase 4

import streamlit as st
from query_runner import get_all_tables, get_table_columns

def dynamic_query_builder():
    """
    Build dynamic query forms based on whatever tables exist in the current DB.
    Returns a SQL query string if submitted, else None.
    """
    tables = get_all_tables()
    if not tables:
        st.info("No tables found in the current database.")
        return None

    st.subheader("Dynamic Query Builder")

    # Pick a table
    selected_table = st.selectbox("Choose a table:", tables)

    # Get columns for that table
    if selected_table is None:
        st.warning("Please select a table.")
        return None
    cols = get_table_columns(selected_table)
    if not cols:
        st.warning(f"No columns found for {selected_table}.")
        return None

    # Pick a column to filter
    selected_col = st.selectbox("Choose a column to filter:", cols)

    # Enter a filter value
    filter_value = st.text_input(f"Enter value for {selected_col}:")

    submitted = st.button("Run Dynamic Query")
    if submitted and filter_value:
        # Build query dynamically
        return f"SELECT * FROM {selected_table} WHERE {selected_col} = '{filter_value}';"

    return None


def quick_table_viewer():
    """
    Quick explorer: lets user pick a table and view all rows without filters.
    Returns a SQL query string if submitted, else None.
    """
    tables = get_all_tables()
    if not tables:
        st.info("No tables found in the current database.")
        return None

    st.subheader("Quick Table Viewer")

    selected_table = st.selectbox("Choose a table to view:", tables, key="quick_view")
    if st.button("Show Table Contents"):
        return f"SELECT * FROM {selected_table};"

    return None
