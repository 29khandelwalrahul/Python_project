from ast import keyword
from email import header
from random import betavariate
from re import X
from turtle import title
import requests
from bs4 import BeautifulSoup
from csv import writer
import re


headers = {'User-agent': 'Chrome/103.0.5060.134'}

request = requests.get('https://timesofindia.indiatimes.com/', headers=headers)
html = request.content

soup = BeautifulSoup(html, 'html.parser')

for i in range(1):
    x = input("Enter The news you want to search for: ")


# print(soup.prettify)
def toi_news_scrapper(keyword):
    news_list = []
    with open('news_scraping.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Index', 'Head Lines', 'Keyword']
        thewriter.writerow(header)
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
                text = ' <---------- KEYWORD'
                no_of_news += 1
                keyword_list.append(title)

            info = [i + 1, title, text]
            thewriter.writerow(info)

        # Prints the Titles of the articles that contain the keywords
    with open('Searched_news.csv', 'w',encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header1 = ['Keyword', 'Number of articles found']
        thewriter.writerow(header1)
        info1 = [keyword, no_of_news]
        thewriter.writerow(info1)
        header2 = ['Searched News', 'Article Link']
        thewriter.writerow(header2)
            # links_list = soup.find_all('a')
        for i, title in enumerate(keyword_list):
            # # for link in soup.findAll('a', attrs={'href': re.compile("^https://timesofindia.indiatimes.com/")}):
                # for link in links_list:
                #     if 'href' in link.attrs:
            for link in soup.find_all('a', attrs={'href': re.compile("^https://")}):
        # display the actual urls
        # print(link.get('href')) 
                info = [title, link.get('href')]
                thewriter.writerow(info)                    
                

toi_news_scrapper(x)
