import mysql.connector 
from mysql.connector import Error 
from term_filter import Filter 

def create_connection():
    try:
        conn = mysql.connector.connect(host='162.241.2.193',
                                       database='agrote43_agrotendencia',
                                       user='agrote43_root', 
                                       password='T.xwycn[sDct',
                                       charset='utf8mb4')
        
        if conn.is_connected():
            return conn
    except Error as e: 
        print("Error message - ", e)

def close_connection(conn, cursor):
    if conn.is_connected():
        cursor.close()
        conn.close()

def select_news(last_id: int):
    connection = create_connection()
    cursor = connection.cursor()

    sql = 'SELECT text FROM news INNER JOIN commodities ON commodities.idCommodities = news.commodities_idCommodities WHERE idNews = ' + str(last_id)
    
    cursor.execute(sql)
    result = cursor.fetchall()

    close_connection(connection, cursor)

    return result

def insert_data(**kwargs):
    connection = create_connection()
    cursor = connection.cursor()

    sql = f'INSERT INTO news(date, headline, text, url, language, commodities_idCommodities, fonte_idFonte) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    
    if kwargs['commoditie'] == 'soja':
        commoditie = 2
    else: commoditie = 1

    cursor.execute(sql, (kwargs['date'], kwargs['headline'], kwargs['text'], kwargs['link'], kwargs['lang'], commoditie, kwargs['id_fonte']))
    connection.commit()

    last_id = cursor.lastrowid
    close_connection(connection, cursor)

    filter = Filter()
    filter.check_terms(last_id, select_news(last_id))

    return True

def insert_terms(id_news, id_class):
    connection = create_connection()
    cursor = connection.cursor()

    sql = f'INSERT INTO terms(news_idNews, class_idClass) VALUES (%s, %s)'

    cursor.execute(sql, (id_news, id_class))
    connection.commit()

    last_id = cursor.lastrowid

    close_connection(connection, cursor)

    return last_id


def get_last_headline():
    connection = create_connection()

    cursor = connection.cursor()

    cursor.execute('SELECT headline FROM news ORDER BY idNews DESC LIMIT 1;')

    result = cursor.fetchall()

    close_connection(connection, cursor)