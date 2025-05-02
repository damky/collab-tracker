from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class Influencer(Base):
    __tablename__ = 'influencers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    platform = Column(String)
    username = Column(String, unique=True)
    price = Column(Float)
    engagement_rate = Column(Float)
    followers = Column(Integer)
    last_updated = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Influencer(name='{self.name}', platform='{self.platform}', price={self.price})>"

class Database:
    def __init__(self, db_url: str = "sqlite:///influencers.db"):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
    
    def add_influencer(self, influencer_data: dict):
        influencer = Influencer(**influencer_data)
        self.session.add(influencer)
        self.session.commit()
    
    def get_influencers_by_price(self, max_price: float = 500.0):
        return self.session.query(Influencer).filter(Influencer.price <= max_price).all()
    
    def close(self):
        self.session.close() 