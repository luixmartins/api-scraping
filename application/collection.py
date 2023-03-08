import re 
import urllib3 
import numpy as np 
import pandas as pd 
from bs4 import BeautifulSoup

class Collection: 
    def __init__(self, url: str, title: str) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        self.http = urllib3.PoolManager()
        self.url = url 
        self.last_headline = title

    def verify_headline(self, headline_from_bd, headline_from_page):
        if headline_from_bd != headline_from_page: 
            return False 
        else: 
            return True 

    def get_links(self):
        try: 
            page = self.http.request('GET', self.url)
        except: 
            print('Error!')

        soup = BeautifulSoup(page.data, 'html.parser')
        
        data = soup.find('div', {'class': 'lista-wrapper middle'}).find_all({'a'})
        
        return ['https://www.noticiasagricolas.com.br' + str(link.get('href')) for link in data]
    
    def scraping_commoditie(self):
        for url in self.get_links():
            try: 
                page = self.http.request('GET', url)
            except: 
                print('Error')
            
            soup = BeautifulSoup(page.data, 'html.parser')

            date = soup.find('div', {'class': 'datas'})

            if date is not None: 
                date = date.get_text(strip=True).split(' ')[2]
                date = pd.to_datetime(date, format='%d/%m/%Y')

                headline = soup.find('h1', {'class': 'page-title'})
                if headline is not None:
                    headline = headline.get_text(strip=True)

                    if self.verify_headline(headline_from_bd=self.last_headline, headline_from_page=headline):
                        pass 
                    else: break;


                article = soup.find('div', {'class': 'materia'})
                if article is not None:
                    article = article.find_all('p')
                    text = ''

                    for paragraph in article:
                        text += ' '.join(paragraph.find_all(text=True)).strip()
                    text = ' '.join(text.split(' '))
            else: 
                return None 
                


        

        