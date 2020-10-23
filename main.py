from scrapers.amazon_scraper import AmazonScraper
from scrapers.bestbuy_scraper import BestBuyScraper
from scrapers.gamestop_scraper import GamestopScraper
from scrapers.target_scraper import TargetScraper
from scrapers.walmart_scraper import WalmartScraper

scrapers = [
    AmazonScraper(),
    BestBuyScraper(),
    GamestopScraper(),
    TargetScraper(),
    WalmartScraper()
]

results = []

for scraper in scrapers:
    results.append({
        'Website': scraper.site,
        'Available': scraper.find_ps5()
    })

print(results)
