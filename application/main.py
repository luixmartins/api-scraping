from fastapi import FastAPI 
from collection import Collection 

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/dataupdate")
async def update_database():

    links = Collection(url='https://www.noticiasagricolas.com.br/noticias/boi/').get_links()

    return {links}