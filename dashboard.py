import streamlit as st
import pandas as pd
from typing import Dict
import logging

class InfluencerDashboard:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def create_layout(self, data: Dict):
        try:
            self.logger.info("Creating dashboard layout...")
            self.logger.info(f"Input data: {data}")
            
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
            
        except Exception as e:
            self.logger.error(f"Error creating dashboard layout: {str(e)}")
            self.logger.exception("Full traceback:")
            raise
    
    def run_server(self, debug: bool = True, port: int = 8050):
        self.create_layout() 