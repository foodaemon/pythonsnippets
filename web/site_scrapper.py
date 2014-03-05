"""
Python snippet to scrape url
Requirements: requests, beautifulsoup4. To install run "pip install requests" and "pip install beautifulsoup4"
"""
import requests     # pip install requests
from bs4 import BeautifulSoup, SoupStrainer     # pip install beautifulsoup4


def get_urls(url):
    request = requests.get(url)     # make get request
    page = request.text

    soup = BeautifulSoup(page, parse_only=SoupStrainer('a'))
    for tag in soup:
        if tag.has_attr('href'):
            print(tag['href'])

"""
calls the get_urls method
"""
get_urls("http://url_that_you_are_trying_to_scrap.com")
