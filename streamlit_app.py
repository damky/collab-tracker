import streamlit as st

st.title("Influencer Collaboration Dashboard")

# Sample data
data = {
    "Name": ["John Doe", "Jane Smith", "Mike Johnson"],
    "Platform": ["Instagram", "TikTok", "YouTube"],
    "Price": [250, 450, 150],
    "Engagement Rate": [3.5, 4.2, 2.8],
    "Followers": [50000, 75000, 25000]
}

# Display data in a table
st.write("### Influencer List")
st.table(data)

# Display price bar chart
st.write("### Collaboration Prices")
st.bar_chart(data["Price"]) 