import streamlit as st
import pandas as pd
import plotly.express as px

# Function to compute top selling products with customer name, region, state, and segment
def top_selling_products(df):
    top_products = df.groupby(['product_name', 'customer_name', 'region', 'state', 'segment'])['sales'].sum().reset_index()
    top_products = top_products.sort_values(by='sales', ascending=False).head(10)
    st.write("Top Selling Products with Customer Name, Region, State, and Segment")
    st.dataframe(top_products)

# Function to compute sales distribution by segment
def sales_by_segment_pie_chart(df):
    sales_by_segment = df.groupby('segment')['sales'].sum().reset_index()
    st.write("Sales Distribution by Segment")
    fig = px.pie(sales_by_segment, names='segment', values='sales', title='Sales Distribution by Segment')
    st.plotly_chart(fig)

# Ninth page content
def nineth_page():
    st.title("Top Selling Products with Customer Name, Region, State, and Segment")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Top Selling Products"):
            top_selling_products(df)

        if st.button("Sales Distribution by Segment"):
            sales_by_segment_pie_chart(df)

        if st.button("Previous Page"):
            st.session_state["page"] = "eighth_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

