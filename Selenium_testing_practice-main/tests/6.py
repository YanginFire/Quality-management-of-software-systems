from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

# Тест кейс 6 (-)
# Проверка поиска сайта hh.ru
driver.get('https://rambler.ru/')

vhod_but = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div/div[4]/div/a').click()

time.sleep(5)

pochta = driver.find_element(By.XPATH, '//*[@id="login"]')

time.sleep(5)

pochta.click()

parol = driver.find_element(By.LINK_TEXT, "Пароль").click()


