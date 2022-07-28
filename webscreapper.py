from ast import keyword
from random import betavariate
from re import X
from turtle import title
import requests
from bs4 import BeautifulSoup

headers = {'User-agent': 'Chrome/103.0.5060.134'}

request = requests.get('https://timesofindia.indiatimes.com/', headers=headers)
html = request.content

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify)

def toi_news_scrapper(keyword):
    news_list = []

    for h in soup.find_all('a',  class_="linktype1" ):
        for i in soup.find('figcaption'):
            news_title = h.contents[0].text

        if news_title not in news_list:
                if 'Times of India' not in news_title:
                    news_list.append(news_title)

    no_of_news = 0
    keyword_list = []
    # Goes through the list and searches for the keyword
    for i, title in enumerate(news_list):
        text = ''
        if keyword in title:
            text = ' <------------ KEYWORD'
            no_of_news += 1
            keyword_list.append(title)

        print(i + 1, ':', title, text)

    # Prints the Titles of the articles that contain the keywords
    print(f'\n--------- Total mentions of "{keyword}" = {no_of_news} ---------')
    for i, title in enumerate(keyword_list):
        print(i + 1, ':', title)
x = input("Enter what you want to search about: ")
toi_news_scrapper(x)
