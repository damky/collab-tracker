import streamlit as st
import pandas as pd
import os

# Disable the email prompt
os.environ["STREAMLIT_SERVER_EMAIL"] = ""

# Set page config
st.set_page_config(
    page_title="Influencer Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("Influencer Collaboration Dashboard")

# Sample data
data = {
    "Name": ["John Doe", "Jane Smith", "Mike Johnson"],
    "Platform": ["Instagram", "TikTok", "YouTube"],
    "Price": [250, 450, 150],
    "Engagement Rate": [3.5, 4.2, 2.8],
    "Followers": [50000, 75000, 25000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display data
st.write("### Influencer List")
st.dataframe(df)

# Display price chart
st.write("### Price Distribution")
st.bar_chart(df.set_index("Name")["Price"]) 