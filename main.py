from collection import Collection 

if __name__ == '__main__':
    Collection(url='https://www.noticiasagricolas.com.br/noticias/soja/', commoditie='soja').scraping_commoditie()
    Collection(url='https://www.noticiasagricolas.com.br/noticias/milho/', commoditie='milho').scraping_commoditie()