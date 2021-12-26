from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Тест кейс 3(-)
# Проверка регистрационной формы на валидность вводимых данных
driver.get('https://mail.rambler.ru/?utm_source=head&utm_campaign=self_promo&utm_medium=header&utm_content=mail')

log_in_button = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div/div/div/div[4]/div/a').click()

login_input = driver.find_element (By.XPATH,'//*[@id="login"]"').click()
login_input.send_keys('yan')


password_input = driver.find_element(By.XPATH, '//*[@id="password"]').click()

password_input.send_keys('yanyan')

enter_data = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[2]/div/div/div/div[1]/form/button/span').click()