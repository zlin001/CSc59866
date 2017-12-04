from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

# url = "https://www.yelp.com/biz/aria-kabab-flushing-3"
#
# def extract_reviews(page_url):
#     html = requests.get(page_url)
#
#     soup = BeautifulSoup(html.text, "html.parser")
#
#
#     # print(soup.prettify().encode("utf-8"))
#     container = soup.findAll('div', attrs={ 'class': 'review-content'})
#
#     next_button = soup.findAll('a', attrs={'class': 'next'})
#     print(next_button)
#     count = 0
#     # for review in container:
#     #     print(count)
#     #     print(review.find('p').text)
#     #     count = count + 1
#     # print(container)
#
# extract_reviews(url)

def crawl_pages(base_url):
    count = 0
    reviews_in_page = []
    next_button = True

    while next_button:
        current_url = base_url + str(count)
        html = requests.get(current_url)
        soup = BeautifulSoup(html.text, "html.parser")

        review_container = soup.findAll('div', attrs={ 'class': 'review-content'})

        for review in review_container:
            reviews_in_page.append(review.find('p').text)

        next_button = soup.findAll('a', attrs={'class': 'next'})
        count = count + 20

    return reviews_in_page

url = "https://www.yelp.com/biz/aria-kabab-flushing-3?start="
print(crawl_pages(url))
