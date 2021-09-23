import sys
import json
import requests
from bs4 import BeautifulSoup
from logger import get_logger # we import own module logger

#Global kullandıyımız değişkenler
URL = "https://www.nytimes.com/crosswords/game/mini"
APP_NAME = "result"
LOGGER = get_logger()

# For get HTML
def get_html(url):
    LOGGER.info("Request sent for get HTML")
    return requests.get(url)

# JSON doyasına gönderdiğimiz array yazdırır
def write_to_json(array):
    with open(APP_NAME+'.json', 'a') as file:
        json.dump(array, file)

    LOGGER.info("JSON file was write")

# aldığımız HTML'lin içinden gereken taglara ulaşıp verilerini alma işlemi yapar
def get_content(html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all('div', class_='ClueList-wrapper--3m-kd')
        result = []

        for item in items:
            # bu loop içinde artık parse işlemleri yaparız ve array'e kayıt ederiz
            array = []
            print('=== '+item.find('h3').get_text()+' ===')
            li_list = item.find_all('li')
            for i in li_list:
                print(i.find('span', class_='Clue-label--2IdMY').get_text() + '. ' + i.find('span', class_='Clue-text--3lZl7').get_text())
                array.append({int(i.find('span', class_='Clue-label--2IdMY').get_text()):str(i.find('span', class_='Clue-text--3lZl7').get_text())})
            result.append({item.find('h3').get_text():[j for j in array]})
        print("-------------------------------------------------------------------------------------------------------")
        LOGGER.info("Parse was successful")
        return result
    except:
        LOGGER.error('ERROR is ', sys.exc_info()[0])


# burda yukardaki fonksyonları adım adım çalıştırır
def parser():
    response = get_html(URL)

    # aldığımız status code kontrol edip ona göre işlem yaparız
    if response.status_code == 200:
        LOGGER.debug("Response status is 200")
        content = get_content(response.content)
        write_to_json(content)
    else:
        LOGGER.warning('Failed, response status code is ' + str(response.status_code))

parser()
