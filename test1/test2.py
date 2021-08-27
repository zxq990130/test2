from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get('http://localhost:8080')
driver.maximize_window()
print('加油，不要哭')
time.sleep(5)