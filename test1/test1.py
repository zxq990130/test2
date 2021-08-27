from selenium import webdriver
import  time
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
print('我一定可以的')
time.sleep(5)