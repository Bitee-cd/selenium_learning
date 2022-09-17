from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# definition of site url as constans 
URL = "https://www.youtube.com/playlist?list=PLC3y8-rFHvwgC9mj0qv972IO5DmD-H0ZH"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(URL)
print(driver.title)
driver.close()

