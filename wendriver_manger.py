from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager() .install())

driver.get('http://www.jumia.com.ng')
print(driver.title)
driver.close()
