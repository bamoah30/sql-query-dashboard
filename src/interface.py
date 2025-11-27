# interface.py
# Interactive query builders for SQL Query Dashboard – Phase 4

import streamlit as st

def student_filter_form():
    """
    Form to filter students by minimum grade.
    Returns a SQL query string if submitted, else None.
    """
    with st.form("student_filter"):
        st.subheader("Filter Students by Grade")
        min_grade = st.number_input("Minimum Grade", min_value=0, max_value=100, value=50)
        submitted = st.form_submit_button("Apply Filter")
        if submitted:
            return f"SELECT * FROM Students WHERE grade >= {min_grade};"
    return None


def class_filter_form():
    """
    Dropdown to select a class and filter students.
    Returns a SQL query string if selected, else None.
    """
    st.subheader("Filter Students by Class")
    class_options = {
        1: "Database Systems",
        2: "Robotics",
        3: "AI Fundamentals",
        4: "Control Systems"
    }
    selected_class = st.selectbox("Choose a class:", options=list(class_options.keys()), format_func=lambda x: class_options[x])
    if st.button("Show Students in Class"):
        return f"SELECT * FROM Students WHERE class_id = {selected_class};"
    return None


def attendance_filter_form():
    """
    Date range filter for attendance records.
    Returns a SQL query string if submitted, else None.
    """
    with st.form("attendance_filter"):
        st.subheader("Filter Attendance by Date Range")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")
        submitted = st.form_submit_button("Apply Date Filter")
        if submitted:
            return f"SELECT * FROM Attendance WHERE date BETWEEN '{start_date}' AND '{end_date}';"
    return None
