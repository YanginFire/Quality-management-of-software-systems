from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Тест кейс 2
# Пустой запрос
driver.get('https://www.rambler.ru/')

search_box = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div/div[2]/div/form/input[5]')
search_box.send_keys(' ')

search_button = driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/div/div/div/div/div[2]/div/form/button[2]').click()
