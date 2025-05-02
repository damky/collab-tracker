import streamlit as st
import pandas as pd

# Sample data
data = {
    'names': ['John Doe', 'Jane Smith', 'Mike Johnson'],
    'platforms': ['Instagram', 'TikTok', 'YouTube'],
    'usernames': ['johndoe', 'janesmith', 'mikejohnson'],
    'prices': [250, 450, 150],
    'engagement_rates': [3.5, 4.2, 2.8],
    'followers': [50000, 75000, 25000]
}

# Create DataFrame
df = pd.DataFrame({
    'Name': data['names'],
    'Platform': data['platforms'],
    'Price': data['prices'],
    'Engagement Rate': data['engagement_rates'],
    'Followers': data['followers']
})

# Set page title
st.title('Influencer Collaboration Dashboard')

# Display price bar chart
st.subheader('Collaboration Prices')
st.bar_chart(df.set_index('Name')['Price'])

# Display data table
st.subheader('Influencer List')
st.dataframe(df) 