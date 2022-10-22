from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.software-engineering.ie/")
        driver.maximize_window()
        text = driver.find_element(By.XPATH,"//h1[@class='elementor-heading-title elementor-size-default']")
        print(text.text)
        time.sleep(5)

find_by_id = DemoFindElementByID()
find_by_id.locate_by_id_demo()