import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Plotly Figure using graph_objects
fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='lines')])

# Add a title to the figure
fig.update_layout(title='Sine Wave')

# Display the Plotly chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
