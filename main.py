from collection import Collection 
from scraping_canalrural import Collection_Cr
from scraping_sca import Collection_SCA

if __name__ == '__main__':
    Collection(url='https://www.noticiasagricolas.com.br/noticias/soja/', commoditie='soja').scraping_commoditie()
    Collection(url='https://www.noticiasagricolas.com.br/noticias/milho/', commoditie='milho').scraping_commoditie()
    Collection_Cr(commoditie="soja", url="https://www.canalrural.com.br/projeto-soja-brasil/noticia/").scraping_commoditie()
    Collection_Cr(commoditie="milho", url="https://www.canalrural.com.br/tag/milho/").scraping_commoditie()
    Collection_SCA(url="https://www.soybeansandcorn.com/articles/?page=1&").scraping_commoditie()