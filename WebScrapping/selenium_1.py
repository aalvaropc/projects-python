from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get('https://es.investing.com/crypto/bitcoin')

time.sleep(8)

precio_bitcoin = driver.find_element("xpath", '//*[@id="last_last"]')
# //*[@id="last_last"]

print(precio_bitcoin.text)

driver.quit()