import streamlit as st
import pandas as pd
import plotly.express as px

# Function to perform Profit by Region and State analysis
def profit_by_region_and_state(df):
    profit_by_region_state = df.groupby(['region', 'state'])['profit'].sum().reset_index()
    profit_by_region_state.columns = ['Region', 'State', 'Total Profit']
    st.write("Profit by Region and State Analysis")
    st.dataframe(profit_by_region_state)
    fig = px.bar(profit_by_region_state, x='State', y='Total Profit', color='Region', title='Total Profit by Region and State', barmode='group')
    st.plotly_chart(fig)

# Third page content
def third_page():
    st.title("Profit over Region Analysis")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Profit by Region and State"):
            profit_by_region_and_state(df)
        
        if st.button("Previous Page"):
            st.session_state["page"] = "second_page"
            st.experimental_rerun()

        if st.button("Next Page"):
            st.session_state["page"] = "fourth_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

