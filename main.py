import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.nytimes.com/crosswords/game/mini"

def get_html(url):
    return requests.get(url)

def write_to_json(array):
    with open('result.json', 'a') as file:
        json.dump(array, file)

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='ClueList-wrapper--3m-kd')
    result = []
    for item in items:
        array = []
        print('=== '+item.find('h3').get_text()+' ===')
        li_list = item.find_all('li')
        for i in li_list:
            print(i.find('span', class_='Clue-label--2IdMY').get_text() + '. ' + i.find('span', class_='Clue-text--3lZl7').get_text())
            array.append({int(i.find('span', class_='Clue-label--2IdMY').get_text()):str(i.find('span', class_='Clue-text--3lZl7').get_text())})
        result.append({item.find('h3').get_text():[j for j in array]})
    print("-------------------------------------------------------------------------------------------------------")
    return result

def parser():
    response = get_html(URL)
    if response.status_code == 200:
        content = get_content(response.content)
        write_to_json(content)
    else:
        print('Failed, response status code is ' + str(response.status_code))
parser()