from bs4 import BeautifulSoup
import requests

# Como obtener HTML de una pagina web

url_website = 'https://subslikescript.com/movie/Titanic-46435'

response = requests.get(url_website)
content = response.text

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())


box = soup.find('article', class_="main-article")
title = box.find('h1').get_text()
# print('title: ', title)

transcript = box.find('div', class_='full-script').get_text()

print(transcript)


with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)

