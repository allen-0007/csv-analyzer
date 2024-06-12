import streamlit as st
import pandas as pd
import plotly.express as px
from login_page import login_page

# Function to visualize graph
def visualize_graph(df):
    st.write("Graph Visualizer")
    graph_type = st.selectbox("Select Graph Type", ["Scatter Plot", "Line Chart", "Bar Chart", "Area Chart", "Pie Chart"])
    x_column = st.selectbox("Select X Column for Graph", df.columns)
    y_column = st.selectbox("Select Y Column for Graph", df.columns)
    
    if graph_type == "Scatter Plot":
        fig = px.scatter(df, x=x_column, y=y_column, title=f"{graph_type} of {x_column} vs {y_column}")
    elif graph_type == "Line Chart":
        fig = px.line(df, x=x_column, y=y_column, title=f"{graph_type} of {x_column} vs {y_column}")
    elif graph_type == "Bar Chart":
        fig = px.bar(df, x=x_column, y=y_column, title=f"{graph_type} of {x_column} vs {y_column}")
    elif graph_type == "Area Chart":
        fig = px.area(df, x=x_column, y=y_column, title=f"{graph_type} of {x_column} vs {y_column}")
    elif graph_type == "Pie Chart":
        fig = px.pie(df, names=x_column, values=y_column, title=f"{graph_type} of {x_column}")

    st.plotly_chart(fig)

# Function for CSV uploader page
def csv_uploader_page():
    st.sidebar.markdown("## Upload CSV")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        for col in ['sales', 'profit', 'quantity']:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        st.session_state["uploaded_df"] = df
        st.session_state["view"] = "tabs"

    if "uploaded_df" in st.session_state:
        df = st.session_state["uploaded_df"]
        st.title("CSV Data Analyzer")

        # Tabs for different views
        tab1, tab2 = st.columns(2)
        with tab1:
            st.write("DataFrame:")
            st.dataframe(df)

        with tab2:
            visualize_graph(df)

        # Navigation buttons
        if st.button("Next Page"):
            st.session_state["page"] = "second_page"
            st.experimental_rerun()

def main():    
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        login_page()
    else:
        if "page" not in st.session_state:
            st.session_state["page"] = "main"

        if st.session_state["page"] == "main":
            csv_uploader_page()
        elif st.session_state["page"] == "second_page":
            from second_page import second_page
            second_page()
        elif st.session_state["page"] == "third_page":
            from third_page import third_page
            third_page()
        elif st.session_state["page"] == "fourth_page":
            from fourth_page import fourth_page
            fourth_page()
        elif st.session_state["page"] == "fifth_page":
            from fifth_page import fifth_page
            fifth_page()
        elif st.session_state["page"] == "sixth_page":
            from sixth_page import sixth_page
            sixth_page()
        elif st.session_state["page"] == "seventh_page":
            from seventh_page import seventh_page
            seventh_page()
        elif st.session_state["page"] == "eighth_page":
            from eighth_page import eighth_page
            eighth_page()
        elif st.session_state["page"] == "nineth_page":
            from nineth_page import nineth_page
            nineth_page()

if __name__ == "__main__":
    main()

