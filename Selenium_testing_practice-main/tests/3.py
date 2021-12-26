from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Тест кейс 3
# Проверка заполнения заявки на животного сайт Дом питомца
driver.get('http://130.193.37.179/app/pets')

pets_without_home = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[1]/div[1]/div[1]/button')

time.sleep(5)

happy_pets = driver.find_element(By.XPATH, '//*[@id="app"]/div/main/div/div[1]/div[1]/div[2]/button')


