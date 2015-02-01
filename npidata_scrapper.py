from urllib2 import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import re

BASE_URL = "http://nppes.viva-it.com/NPI_Files.html"

def get_weekly_incremental_file():
    page = urlopen(BASE_URL)
    page = page.read()

    soup = BeautifulSoup(page, parse_only=SoupStrainer('a'))
    urls = []
    for url in soup:
        if url.has_attr('href'):
            pattern = re.search(r'\bWeekly.zip\b', url.get('href'))
            print pattern
            #urls.append(url.get('href'))
    #print urls

get_weekly_incremental_file()