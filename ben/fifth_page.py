import streamlit as st
import pandas as pd
import plotly.express as px

# Function to compute yearly sales
def compute_yearly_sales(df):
    df['order_dae'] = pd.to_datetime(df['order_dae'])
    yearly_sales = df.groupby(df['order_dae'].dt.year)['sales'].sum().reset_index()
    yearly_sales.columns = ['Year', 'Sales']
    st.write("Yearly Sales")
    st.dataframe(yearly_sales)
    fig = px.bar(yearly_sales, x='Year', y='Sales', title="Yearly Sales")
    st.plotly_chart(fig)

# Function to compute monthly sales for a specific year
def compute_monthly_sales_for_year(df, year):
    df['order_dae'] = pd.to_datetime(df['order_dae'])
    df_year = df[df['order_dae'].dt.year == int(year)]
    monthly_sales = df_year.groupby(df_year['order_dae'].dt.month)['sales'].sum().reset_index()
    monthly_sales.columns = ['Month', 'Sales']
    st.write(f"Monthly Sales for {year}")
    st.dataframe(monthly_sales)
    fig = px.bar(monthly_sales, x='Month', y='Sales', title=f"Monthly Sales for {year}")
    st.plotly_chart(fig)

# Function to compute weekly sales
def compute_weekly_sales(df):
    df['order_dae'] = pd.to_datetime(df['order_dae'])
    weekly_sales = df.groupby(pd.Grouper(key='order_dae', freq='W'))['sales'].sum().reset_index()
    weekly_sales.columns = ['Order Date', 'Sales']
    st.write("Weekly Sales")
    st.dataframe(weekly_sales)
    fig = px.line(weekly_sales, x='Order Date', y='Sales', title="Weekly Sales")
    st.plotly_chart(fig)

# Function to compute monthly sales
def compute_monthly_sales(df):
    st.write("Monthly Sales")
    sales_year = st.selectbox("Select Year", ["2014", "2015", "2016", "2017"])
    compute_monthly_sales_for_year(df, sales_year)

# Fifth page content
def fifth_page():
    st.title("Sales over Time")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Yearly Sales"):
            compute_yearly_sales(df)
        
       
        compute_monthly_sales(df)
        
        if st.button("Weekly Sales"):
            compute_weekly_sales(df)

        if st.button("Previous Page"):
            st.session_state["page"] = "fourth_page"
            st.experimental_rerun()
            
        if st.button("Next Page"):
            st.session_state["page"] = "sixth_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

