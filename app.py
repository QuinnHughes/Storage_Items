import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Shelf Viewer", layout="wide")

# Connect to SQLite database
conn = sqlite3.connect("shelf_books.db")
df = pd.read_sql_query("SELECT * FROM books", conn)

# Sidebar filters
st.sidebar.header("Filter by Location")
floor = st.sidebar.selectbox("Floor", sorted(df['floor'].unique()))
range_ = st.sidebar.selectbox("Range", sorted(df['range'].unique()))
ladder = st.sidebar.selectbox("Ladder", sorted(df['ladder'].unique()))
shelf = st.sidebar.selectbox("Shelf", sorted(df['shelf'].unique()))

# Filter the dataframe
filtered_df = df[
    (df['floor'] == floor) &
    (df['range'] == range_) &
    (df['ladder'] == ladder) &
    (df['shelf'] == shelf)
].sort_values(by='position')

# Page title
st.title(f"Shelf Viewer: {range_} - Ladder {ladder} - Shelf {shelf}")

# Display table
st.dataframe(filtered_df[['position', 'barcode']], use_container_width=True)
