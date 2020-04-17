import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time

# https://github.com/miguelfzafra/Latest-News-Classifier/blob/master/0.%20Latest%20News%20Classifier/05.%20News%20Scraping/17.%20WS%20-%20El%20Pais.ipynb


class ElPaisScraper():
    
    def __init__(self):
        # url definition
        self.url = "https://elpais.com/elpais/inenglish.html"

        # Request
        r1 = requests.get(self.url)
        print('Request status code: {}'.format(r1.status_code))

        # We'll save in coverpage the cover page content
        coverpage = r1.content

        # Soup creation
        soup1 = BeautifulSoup(coverpage, 'html5lib')

        # News identification
        self.coverpage_news = soup1.find_all('h2', class_='headline')
        print('Number of articles found on cover page: {}'.format(len(self.coverpage_news)))

    def scrape_elpais(self, number_of_articles = 5):
        # Empty lists for content, links and titles
        news_contents = []
        list_links = []
        list_titles = []

        for n in np.arange(0, number_of_articles):
            
            # Getting the link of the article
            link = 'https://english.elpais.com' + self.coverpage_news[n].find('a')['href']
            list_links.append(link)
            print(link)
            
            # Getting the title
            title = self.coverpage_news[n].find('a').get_text()
            list_titles.append(title)
            print(title)
            
            # Reading the content (it is divided in paragraphs)
            article = requests.get(link)
            article_content = article.content
            soup_article = BeautifulSoup(article_content, 'html5lib')
            body = soup_article.select('div[class*="a_b article_body"]')
            x = body[0].find_all('p')
            
            # Unifying the paragraphs
            list_paragraphs = []
            for p in np.arange(0, len(x)):
                paragraph = x[p].get_text()
                list_paragraphs.append(paragraph)
                final_article = " ".join(list_paragraphs)
                
            news_contents.append(final_article)

        # df_show_info
        articles = pd.DataFrame({
            'link': list_links,
            'title': list_titles,
            'body': news_contents 
            })


        print(articles)

        return articles

if __name__ == "__main__":

    elpais_scraper = ElPaisScraper()

    elpais_scraper.scrape_elpais()