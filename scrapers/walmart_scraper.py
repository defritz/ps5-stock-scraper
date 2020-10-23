from bs4 import BeautifulSoup as soup
import requests

class WalmartScraper:

    def __init__(self):
        self.site = 'Walmart'

    def find_ps5(self):
        # Webpage Info
        page_url = 'https://www.walmart.com/ip/Sony-PlayStation-5/363472942?irgwc=1&sourceid=imp_RZvQMTSelxyOT-ewUx0Mo36HUkExtIXBTWkkw00&veh=aff&wmlspartner=imp_62662&clickid=RZvQMTSelxyOT-ewUx0Mo36HUkExtIXBTWkkw00&sharedid='
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        headers = {'User-Agent': agent}

        # opens the connection and downloads html page from url
        page = requests.get(page_url, headers=headers)

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        page_soup = soup(page.text, 'html.parser')

        # finds each product from the store page
        order_button = page_soup.find('input', {'value': 'Add to cart'})

        if order_button is not None:
            is_available = True
            return is_available
        
        return "False"
