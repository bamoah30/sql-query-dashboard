# visualizer.py
# Handles visualization of SQL query results for SQL Query Dashboard – Phase 3

import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import streamlit as st

def to_dataframe(rows, cols):
    """
    Convert query results (rows + column names) into a Pandas DataFrame.
    Returns None if no data.
    """
    if rows is None or cols is None or len(rows) == 0:
        return None
    return pd.DataFrame(rows, columns=cols)

# -----------------------------
# Altair-based visualizations
# -----------------------------

def plot_bar(df, x_col, y_col, title="Bar Chart"):
    """Generate an Altair bar chart."""
    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X(x_col, sort=None),
        y=y_col
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

def plot_line(df, x_col, y_col, title="Line Chart"):
    """Generate an Altair line chart."""
    chart = alt.Chart(df).mark_line(point=True).encode(
        x=x_col,
        y=y_col
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

def plot_pie(df, category_col, value_col, title="Pie Chart"):
    """Generate an Altair pie chart (using mark_arc)."""
    chart = alt.Chart(df).mark_arc().encode(
        theta=value_col,
        color=category_col
    ).properties(title=title)
    st.altair_chart(chart, use_container_width=True)

# -----------------------------
# Matplotlib-based visualizations (optional)
# -----------------------------

def plot_bar_matplotlib(df, x_col, y_col, title="Bar Chart"):
    """Generate a Matplotlib bar chart."""
    fig, ax = plt.subplots()
    ax.bar(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)
    st.pyplot(fig)

def plot_line_matplotlib(df, x_col, y_col, title="Line Chart"):
    """Generate a Matplotlib line chart."""
    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker="o")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)
    st.pyplot(fig)

def plot_pie_matplotlib(df, category_col, value_col, title="Pie Chart"):
    """Generate a Matplotlib pie chart."""
    fig, ax = plt.subplots()
    ax.pie(df[value_col], labels=df[category_col], autopct="%1.1f%%")
    ax.set_title(title)
    st.pyplot(fig)
