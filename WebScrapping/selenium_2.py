from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
import pandas as pd
from datetime import date
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

home_link = 'https://www.falabella.com.pe/falabella-pe'

search = "iphone x".replace(" ", "+")

driver.maximize_window()
driver.get(home_link + "/search?Ntt=" + search)

iphone_name = []
iphone_price = []
links = []

time.sleep(5)

page = BeautifulSoup(driver.page_source, 'lxml')

bloque = page.find('div', attrs = {'class': 'jsx-4099777552 search-results--products'})
print(bloque)

for phone in bloque:
    title = phone.find('b', attrs = {'class': 'jsx-1327784995 copy2 primary jsx-2889528833 normal pod-subTitle subTitle-rebrand'})
    price = phone.find('span', attrs = {'class': 'copy10 primary medium jsx-2889528833 normal line-height-22'})
    link = phone.find('a', attrs = {'class': 'jsx-1327784995 jsx-97019337 pod-summary pod-link pod-summary-4_GRID'})
    iphone_name.append(title.text)
    iphone_price.append((price.text).replace(" ", ""))
    links.append(link['href'])

data = {
    'Nombre': iphone_name,
    'Precio': iphone_price,
    'enlace': links
}
df = pd.DataFrame(data)
print(df)

df.to_csv('datos2.csv', index=False)