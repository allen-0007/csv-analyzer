import streamlit as st
import pandas as pd
import plotly.express as px

# Function to perform Sales vs Profit analysis
def sales_vs_profit(df):
    sales_by_profit = df.groupby('profit')['sales'].sum().reset_index()
    sales_by_profit.columns = ['Profit', 'Total Sales']
    st.write("Sales vs Profit Analysis")
    st.dataframe(sales_by_profit)
    fig = px.bar(sales_by_profit, x='Profit', y='Total Sales', title='Total Sales by Profit')
    st.plotly_chart(fig)

# Second page content
def second_page():
    st.title("Sales vs Profit Analysis")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Sales vs Profit"):
            sales_vs_profit(df)
        
        if st.button("Previous Page"):
            st.session_state["page"] = "main"
            st.experimental_rerun()

        if st.button("Next Page"):
            st.session_state["page"] = "third_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

