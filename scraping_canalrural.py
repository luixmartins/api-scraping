import urllib3 
import numpy as np 
import pandas as pd 
import managedb
from bs4 import BeautifulSoup
from datetime import datetime 

class Collection_Cr:
    def __init__(self, commoditie, url) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
        self.http = urllib3.PoolManager()
        self.url = url 
        self.commoditie = commoditie
        self.data_source = "Canal Rural"
    
    def get_links(self):
        try: 
            page = self.http.request('GET', self.url)
        except: 
            print('Error!')

        soup = BeautifulSoup(page.data, 'html.parser')

        return [link.find("a").get('href') for link in soup.find_all('h2', {'class': 'fl-post-title'})]
    
    def scraping_commoditie(self):
        for url in self.get_links():
            try: 
                page = self.http.request('GET', url)
            except: 
                print('Error')

            soup = BeautifulSoup(page.data, 'html.parser')

            date = soup.find("p", {'class': 'data-autor'}).find('span').get_text()[0:10]
            
            if date is not None:
                date = pd.to_datetime(date, format='%d/%m/%Y')
                
                if pd.to_datetime(datetime.today().strftime('%Y-%m-%d')) != date:
                   break;

                headline = soup.find('h1', {'class': 'titulo'}).get_text()

                content_text = soup.find('div', {'class': 'texto-noticia'}).find_all('p')

                text = ""
                for i in content_text:
                    text += ' '.join(i.get_text().split())

                text = text.replace('.', '. ').split()
                text = ' '.join(text)
                
                managedb.insert_data(date=date, headline=headline, text=text, link=url, lang='pt', commoditie=self.commoditie, id_fonte=2)
