import re 
import urllib3 
import pandas as pd 
import managedb
from bs4 import BeautifulSoup
from datetime import datetime 

class Collection_SCA:
    def __init__(self, url: str) -> None:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        self.http = urllib3.PoolManager()
        self.url = url
    
    def get_links(self):
        try:
            page = self.http.request('GET', self.url)
        except: 
            print("Error")
        
        soup = BeautifulSoup(page.data, 'html.parser')

        data = soup.find('div', {'class': 'container-fluid'}).find_all({'a'})

        return ['https://www.soybeansandcorn.com' + str(link.get('href')) for link in data]
    
    def convert_months(self, month):
        month_number = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7, 
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12
        }

        return month_number[month]
    
    def scraping_commoditie(self): 
        for url in self.get_links():
            try: 
                page = self.http.request('GET', url)
            except: 
                print('Error')
        
            soup = BeautifulSoup(page.data, 'html.parser')
            original_date = soup.find('div', {'class': 'container-fluid'}).find('h5').get_text()
            
            if original_date: 
                month = self.convert_months(original_date[:3])
                day = original_date[4:6]
                year = original_date[8:]

                date = pd.to_datetime(f'{day}/{month}/{year}', format='%d/%m/%Y')
                
                if pd.to_datetime(datetime.today().strftime('%Y-%m-%d')) != date:
                   break;
                article = soup.find('div', {'class': 'container-fluid'}).find_all({'p'})

                text = ""
                for paragraph in article:
                    #print(paragraph)
                    text += ' '.join(paragraph.get_text().split())    
                
                
                headline = soup.find('div', {'class': 'container-fluid'}).find('h3').get_text(strip=True)

                
                if "soy" or "soybean" in headline.lower():
                    commoditie = "soja"
                elif "corn" in headline.lower():
                    commoditie = "milho"
                else: 
                    soy = len(re.findall('soy', text.lower()))
                    corn = len(re.findall('corn', text.lower()))

                    commoditie = 'soja' if soy >= corn else 'milho'

                managedb.insert_data(date=date, headline=headline, text=text, link=url, lang='en', commoditie=commoditie, id_fonte=3)
                
