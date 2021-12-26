from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

# Тест кейс 6
# Проверка сайта Дом питомцев на работоспособность Header'a
driver.get('http://130.193.37.179/app/pets')

time.sleep(5)

about_us = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul[1]/li/form/a[1]').click()

time.sleep(5)

animals_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul[1]/li/form/a[2]').click()

time.sleep(5)

contacts = driver.find_element(By.XPATH, '//*[@id="app"]/div/nav/ul[1]/li/form/a[3]').click()

