# Парсим сайт БМК в csv документ

from sqlite3.dbapi2 import Cursor
import requests
import sqlite3
from bs4 import BeautifulSoup as BS



# Пишем в файл название колбасс +++++++++++++++++++++++++++++++++++++++++++++++
def WriteToFileBMK(data, data_href, data_img, data_sostav, data_cat):
   
    try:
       conn = sqlite3.connect("d:\Учеба\Python\BMK\database_bmk.db")
       cursor = conn.cursor()

       data = data[1 : -1]
       zapros = "INSERT INTO 'kolbasi' (name, linktosite, linktopng, sostav, grypa) VALUES ( '" + data + "','" + data_href + "','" + data_img + "','" + data_sostav + "','" + data_cat + "')" 
       cursor.execute( zapros )
       print(data)
       conn.commit() 
    except sqlite3.Error as error:
        print("error", error)

    finally:
        if (conn):
            conn.close()


def MyParsUrl(data):
    i=0
    result=''
    data = str(data)
    data = data[9 : -1]
    while data[i] !='"':
        result = result + data[i]
        i = i + 1 
    return result


# Парсим колбасы без первой страницы ++++++++++++++++++++++++++++++++++++++++++
i=0
while i < 10:
    i=i+1
    url="http://bmk.md/bmk/kolbasn-izdelia/page/" + str(i) + "/"
    r = requests.get(url)
    html = BS(r.text, 'html.parser')
    kolbasa_url = html.find_all("div", class_= "opisanienews") 
    kolbasa_img = html.find_all("div", class_= "box-thumb")
   
    index_img = 0
    for el in kolbasa_url:
        print('List = '+ str(index_img))
        url2=MyParsUrl(el.a)
        r2 = requests.get(url2)
        html2 = BS(r2.text, 'html.parser')
        sostav = html2.find_all("div", class_="flst")
        kolbasa_cat = html2.find_all("div", class_= "page_title_inner baseline")
        StringTemp = str(kolbasa_img[index_img].img)
        StringTemp = (StringTemp[26 : -3])
        Stringcat = kolbasa_cat[0].text[1 : -1]
        WriteToFileBMK(el.text, MyParsUrl(el.a), 'http://bmk.md' + StringTemp, sostav[0].text, Stringcat )
        index_img = index_img + 1

print('End')
