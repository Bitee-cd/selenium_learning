from typing import final
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#definition of variables
URL = "https://stephanieesha.wixsite.com/stephanie-portfolio"
PATH = "C:\chromedriver.exe"

#start service and open the page
service= Service(PATH)
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(URL)

try:
    #scroll to bottom of the page
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    #locate back to top button
    button = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.LINK_TEXT,"contact"))
    )
    button.click()

except:
    driver.close()
#clicking the back to top bottom
