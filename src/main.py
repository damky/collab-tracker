from scraper import InfluencerScraper
from database import Database
from dashboard import InfluencerDashboard
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Initialize components
    scraper = InfluencerScraper()
    db = Database()
    dashboard = InfluencerDashboard()
    
    try:
        # TODO: Add platform URLs to scrape
        platform_urls = []
        
        # Scrape data from platforms
        all_influencers = []
        for url in platform_urls:
            influencers = scraper.scrape_platform(url)
            all_influencers.extend(influencers)
        
        # Filter influencers by price
        affordable_influencers = scraper.filter_by_price(all_influencers)
        
        # Store in database
        for influencer in affordable_influencers:
            db.add_influencer(influencer)
        
        # Create and run dashboard
        dashboard.create_layout(affordable_influencers)
        dashboard.run_server()
        
    except Exception as e:
        logger.error(f"Error in main application: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    main() 