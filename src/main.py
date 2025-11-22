# main.py
# SQL Query Dashboard – Phase 1 (Foundations & Setup)

import streamlit as st

def main():
    # Title and description
    st.title("SQL Query Dashboard")
    st.write("Welcome to Phase 1 – Foundations & Setup")
    st.write("This dashboard will allow you to run SQL queries and visualize results in later phases.")

    # Placeholder sections
    st.header("Database Connection")
    st.info("Database connection will be implemented in Phase 2.")

    st.header("Query Execution")
    st.info("SQL query runner will be added in Phase 2.")

    st.header("Visualization")
    st.info("Charts and plots will be introduced in Phase 3.")

    # Footer
    st.write("---")
    st.caption("SQL Query Dashboard | Phase 1 Setup Complete")

if __name__ == "__main__":
    main()
