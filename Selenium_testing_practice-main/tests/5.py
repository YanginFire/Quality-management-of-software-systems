from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Тест кейс 5
# Проверка работоспособности Footer'a
driver.get('https://www.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=logo&utm_content=head')


rss_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[6]/footer/div/div/div[2]/div[2]/a[4]').click()

youtube_button =driver.find_element(By.XPATH, '//*[@id="main"]/div[6]/footer/div/div/div[2]/div[2]/a[2]').click()

instagramm_button =driver.find_element(By.XPATH, '//*[@id="main"]/div[6]/footer/div/div/div[2]/div[2]/a[1]').click()

ok_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[6]/footer/div/div/div[2]/div[1]/a[4]').click()

twi_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[6]/footer/div/div/div[2]/div[1]/a[3]').click()

facebook_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[6]/footer/div/div/div[2]/div[1]/a[2]').click()

vk_button = driver.find_element(By.XPATH,'//*[@id="main"]/div[6]/footer/div/div/div[2]/div[1]/a[1]').click()
