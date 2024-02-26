# main.py
from src.scraper import WebScraper

def main():
    # URL you want to scrape
    url = 'https://example.com'
    
    # Initialize the scraper
    scraper = WebScraper(url)
    
    # Perform the scraping
    data = scraper.scrape()
    
    # Displays the collected data
    print(data)

if __name__ == '__main__':
    main()
