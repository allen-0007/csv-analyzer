import streamlit as st
import pandas as pd
import plotly.express as px

# Function to compute sales by region
def sales_by_region_pie_chart(df):
    sales_by_region = df.groupby('region')['sales'].sum().reset_index()
    st.write("sales by Region")
    fig = px.pie(sales_by_region, names='region', values='sales', title='sales by Region')
    st.plotly_chart(fig)

# Sixth page content
def sixth_page():
    st.title("sales by Region")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("sales by Region (Pie Chart)"):
            sales_by_region_pie_chart(df)

        if st.button("Previous Page"):
            st.session_state["page"] = "fifth_page"
            st.experimental_rerun()
            
        if st.button("Next Page"):
            st.session_state["page"] = "seventh_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

