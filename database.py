from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import logging
from typing import Dict

Base = declarative_base()

class Influencer(Base):
    __tablename__ = 'influencers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)
    username = Column(String)
    price = Column(Float)
    engagement_rate = Column(Float)
    followers = Column(Integer)

class Database:
    def __init__(self, db_url: str = 'sqlite:///influencers.db'):
        self.logger = logging.getLogger(__name__)
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.logger.info("Database initialized")
    
    def add_influencer(self, influencer_data: Dict):
        try:
            self.logger.info(f"Adding influencer to database: {influencer_data}")
            influencer = Influencer(
                name=influencer_data['name'],
                platform=influencer_data['platform'],
                username=influencer_data['username'],
                price=influencer_data['price'],
                engagement_rate=influencer_data['engagement_rate'],
                followers=influencer_data['followers']
            )
            self.session.add(influencer)
            self.session.commit()
            self.logger.info(f"Successfully added influencer: {influencer_data['name']}")
            return influencer
        except Exception as e:
            self.logger.error(f"Error adding influencer to database: {str(e)}")
            self.session.rollback()
            raise
    
    def close(self):
        self.logger.info("Closing database connection")
        self.session.close() 