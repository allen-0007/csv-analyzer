import streamlit as st
import pandas as pd
import plotly.express as px

# Function to compute profit by segment and region
def profit_by_segment_and_region(df):
    profit_by_segment_region = df.groupby(['segment', 'region'])['profit'].sum().reset_index()
    profit_by_segment_region.columns = ['Segment', 'Region', 'Total Profit']
    st.write("Profit by Segment and Region Analysis")
    st.dataframe(profit_by_segment_region)
    fig = px.bar(profit_by_segment_region, x='Region', y='Total Profit', color='Segment', title='Profit by Segment and Region', barmode='group')
    st.plotly_chart(fig)

# Seventh page content
def seventh_page():
    st.title("Profit by Segment and Region")

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        
        if st.button("Profit by Segment and Region"):
            profit_by_segment_and_region(df)

        if st.button("Previous Page"):
            st.session_state["page"] = "sixth_page"
            st.experimental_rerun()
            
        if st.button("Next Page"):
            st.session_state["page"] = "eighth_page"
            st.experimental_rerun()
    else:
        st.write("No CSV file uploaded yet. Please go back to the main page and upload a file.")

