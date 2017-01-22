from selenium import webdriver


driver = webdriver.Firefox()
driver.get('http://www.bing.com/')
driver.quit()