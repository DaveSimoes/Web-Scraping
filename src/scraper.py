# scraper.py
import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        # Make the HTTP request
        response = requests.get(self.url)
        
        # Checks if the request was successful
        if response.status_code == 200:
            # Parses the HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Here, you can implement the specific logic to collect the desired data
            
            # For example, to collect all the links on the page
            links = [link['href'] for link in soup.find_all('a', href=True)]
            
            return links
        else:
            print(f'Error making request. Status code: {response.status_code}')
            return None
