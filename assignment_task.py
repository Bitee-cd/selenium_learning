from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PATH = "C:\chromedriver.exe"
URL ="https://stephanieesha.wixsite.com/stephanie-portfolio"

service = Service(PATH)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(URL)

try:
    button = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH,'//*[@id="comp-kyocojds"]/a'))
    )
    button.click()
finally:
    driver.close()
