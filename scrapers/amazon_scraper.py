from bs4 import BeautifulSoup as soup
import requests

class AmazonScraper:

    def __init__(self):
        self.site = 'Amazon'

    def find_ps5(self):
        # Webpage Info
        page_url = 'https://www.amazon.com/dp/B08FC6MR62?tag=nismain-20&linkCode=ogi&th=1&psc=1'
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        headers = {
            'User-Agent': agent,
            "Accept-Encoding":"gzip, deflate",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "DNT":"1",
            "Connection":"close",
            "Upgrade-Insecure-Requests":"1"
        }

        # opens the connection and downloads html page from url
        page = requests.get(page_url, headers=headers)

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        page_soup = soup(page.text, 'html.parser')

        # finds each product from the store page
        availability_notice = page_soup.find('div', {'id': 'availability_feature_div'})

        if availability_notice is not None:
            is_available = False
            return is_available
        
        return "True"
