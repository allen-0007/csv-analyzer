import streamlit as st
import pandas as pd
import plotly.express as px

# Function to perform Impact of Discount over Sales analysis
def discount_over_sales(df):
    discount_sales = df.groupby('discount')['sales'].sum().reset_index()
    discount_sales.columns = ['Discount', 'Total Sales']
    st.write("Impact of Discount over Sales")
    st.dataframe(discount_sales)
    fig = px.bar(discount_sales, x='Discount', y='Total Sales', title='Total Sales by Discount')
    st.plotly_chart(fig)

# Fourth page content
def fourth_page():
    st.title("Impact of Discount over Sales")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Impact of Discount over Sales"):
            discount_over_sales(df)
        
        if st.button("Previous Page"):
            st.session_state["page"] = "third_page"
            st.experimental_rerun()

        if st.button("Next Page"):
            st.session_state["page"] = "fifth_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

