import managedb
import pandas as pd 
from datetime import datetime 

date = pd.to_datetime(datetime.today().strftime('%Y-%m-%d')) 
headline = "Alcool is Fun"
text = "I love alcool sistema de carga unitarizada comércio internacional alimentação na seca"
url = "www.link.com.br"

response = managedb.insert_data(date=date, headline=headline, text=text, link=url, lang='pt')
