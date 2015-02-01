"""
Python snippet to scrape url
Requirements: requests, beautifulsoup4. To install run "pip install requests" and "pip install beautifulsoup4"
"""
import sys, optparse
import requests
from bs4 import BeautifulSoup, SoupStrainer

def get_urls(url):
    request = requests.get(url)
    page = request.text

    soup = BeautifulSoup(page, parse_only=SoupStrainer('a'))
    for tag in soup:
        if tag.has_attr('href'):
            print(tag['href'])


def main():
    url = ''
    usage = "usage: %prog <url>"
    parser = optparse.OptionParser(usage)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of args")
    url = args[0]
    if options.verbose:
        print("Downloading page {0}".format(url))
    get_urls(url)

if __name__ == "__main__":
    main()
