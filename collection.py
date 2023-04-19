import re 
import urllib3 
import numpy as np 
import pandas as pd 
import managedb
from bs4 import BeautifulSoup
from datetime import datetime 

class Collection: 
    def __init__(self, url: str, commoditie: str) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        self.http = urllib3.PoolManager()
        self.url = url 
        self.commoditie = commoditie

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
            print(url)
            soup = BeautifulSoup(page.data, 'html.parser')

            date = soup.find('div', {'class': 'datas'})

            if date is not None: 
                date = date.get_text(strip=True).split(' ')[2]
                date = pd.to_datetime(date, format='%d/%m/%Y')

                if pd.to_datetime(datetime.today().strftime('%Y-%m-%d')) != date:
                    break;

                headline = soup.find('h1', {'class': 'page-title'})
                if headline is not None:
                    headline = headline.get_text(strip=True)

                article = soup.find('div', {'class': 'materia'})
                if article is not None:
                    article = article.find_all('p')
                    text = ''

                    for paragraph in article:
                        text += ' '.join(paragraph.find_all(text=True)).strip()
                    text = ' '.join(text.split(' '))

                managedb.insert_data(date=date, headline=headline, text=text, link=url, lang='pt', commoditie=self.commoditie)
                


        

        