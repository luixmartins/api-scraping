from fastapi import FastAPI 
from collection import Collection 
import managedb

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/dataupdate")
async def update_database():
    response_soybean = Collection(url='https://www.noticiasagricolas.com.br/noticias/soja/', commoditie='soja').scraping_commoditie()
    response_corn = Collection(url='https://www.noticiasagricolas.com.br/noticias/milho/', commoditie='milho').scraping_commoditie()
    
    return {"Message": {response_soybean, response_corn}}
