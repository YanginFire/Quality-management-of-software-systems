from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Тест кейс 4
# Проверка работоспособности Header'a
driver.get('https://www.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=logo&utm_content=head')

movie_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/div[3]/a').click()

news_button =driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/div[2]/a').click()

sport_button =driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/div[4]/a').click()

auto_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/div[5]/a').click()

show_bussiness_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/div[6]/a').click()

horoscope_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div/div/div[1]/div/div[2]/div[7]/a').click()