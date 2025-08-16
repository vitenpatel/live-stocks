import streamlit as st
import plotly.express as px
import pandas as pd

# Set page configuration (optional but good practice)
st.set_page_config(page_title="Streamlit Plotly Example", layout="centered")

st.title("Interactive Plotly Chart in Streamlit")

# Create some sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value1': [10, 25, 15, 30, 20],
    'Value2': [5, 18, 12, 22, 10]
}
df = pd.DataFrame(data)

# Allow user to select a column for plotting
selected_column = st.selectbox("Select a value to plot:", options=['Value1', 'Value2'])

# Create a Plotly bar chart
fig = px.bar(df, x='Category', y=selected_column, 
             title=f'Bar Chart of {selected_column} by Category',
             labels={'Category': 'Product Category', selected_column: 'Measured Value'})

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write("This is a simple Streamlit app demonstrating how to embed interactive Plotly charts. You can deploy this app directly to Streamlit Cloud.")