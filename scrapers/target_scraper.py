from bs4 import BeautifulSoup as soup
import requests

class TargetScraper:

    def __init__(self):
        self.site = 'Target'

    def find_ps5(self):
        # Webpage Info
        page_url = 'https://www.target.com/p/playstation-5-console/-/A-81114595#lnk=sametab'
        agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        headers = {'User-Agent': agent}

        # opens the connection and downloads html page from url
        page = requests.get(page_url, headers=headers)

        # parses html into a soup data structure to traverse html
        # as if it were a json data type.
        page_soup = soup(page.text, 'html.parser')

        # finds each product from the store page
        order_button = page_soup.find('div', {'data-test': 'PDPFulfillmentSection'})

        if order_button is not None:
            is_available = not order_button.has_attr('disabled')
            return is_available
        
        return "Not Found"
