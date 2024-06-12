import streamlit as st
import pandas as pd
import plotly.express as px

# Function to compute sales by city
def sales_by_city(df):
    sales_by_city = df.groupby('city')['sales'].sum().reset_index()
    st.write("Sales by City")
    fig = px.bar(sales_by_city, x='city', y='sales', title='Sales by City')
    st.plotly_chart(fig)

# Eighth page content
def eighth_page():
    st.title("Sales by City")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Sales by City"):
            sales_by_city(df)

        if st.button("Previous Page"):
            st.session_state["page"] = "seventh_page"
            st.experimental_rerun()
            
        if st.button("Next Page"):
            st.session_state["page"] = "nineth_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

