from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json



#definiton of variables
URL ="https://stephanieesha.wixsite.com/stephanie-portfolio"
Mitobi ="https://mitobiltd.com"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
class Portfolio_Test():
   
    def scroll_to_bottom(self):
        driver.get(URL)
        driver.maximize_window()

        # Scroll to Bottom of Webpage
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

    def click_top_button(self):
        #click on scroll to top button
        scroll = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Up'] div[class='StylableButton2545352419__container']")
        scroll.click()
        time.sleep(5)

    def cick_about_link(self):
        #click on the about link
        about = driver.find_element(By.CSS_SELECTOR,"a[class='StylableButton2545352419__root style-kyocs4f6__root StylableButton2545352419__link'] div[class='StylableButton2545352419__container']")
        about.click()
        time.sleep(5)

        #switch to new window
    def switch_to_new_window(self):
        driver.switch_to.window(driver.window_handles[1])
        print(driver.title)

    def click_on_back_button(self):
        #click on the back button
        back = driver.find_element(By.XPATH,"(//*[name()='svg'][@role='presentation'])[4]")
        back.click()
        time.sleep(5)

    def switch_to_previous_window(self):
        #switch back to the previous window
        driver.switch_to.window(driver.window_handles[0])
        print(driver.title)

    def click_on_contact_button(self):
        #click on the contact button
        contact = driver.find_element(By.CSS_SELECTOR,"a[class='StylableButton2545352419__root style-kyocul6f__root StylableButton2545352419__link'] div[class='StylableButton2545352419__container']")
        contact.click()
        time.sleep(5)

    def scroll_to_top(self):
        #scroll to the top of the page
        driver.execute_script("scrollBy(0,250);")
        time.sleep(5)

    def go_to_selected_projets(self):
        #go to selected projects
        projects = driver.find_element(By.CSS_SELECTOR,"div[data-mesh-id='comp-kyocojgtinlineContent-gridContainer']")
        project = projects.find_elements(By.CLASS_NAME,"_3Gr0h")

        #wait definition
        wait= WebDriverWait(driver,10)

        # #looping through the projects and clicking cancel
        for i in project:
            i.click()
            time.sleep(5)
            close= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_2DPZA']//*[name()='svg']")))
            close.click()
            time.sleep(3)

        #needs working
    def hover_automation_testing(self):
        #find automating testing and hover over
        section = driver.find_element(By.CSS_SELECTOR,"section[id='comp-l3onkfps'] div[class='_1uldx']")
        automated_testing = section.find_element(By.CSS_SELECTOR,"#comp-l3onn2sv_video")
        hover=ActionChains(driver).move_to_element(automated_testing)
        hover.perform
        time.sleep(10)
    

    def scroll_to_article_Section(self):
        #scroll to article section and click view more
        articles = driver.find_element(By.XPATH,"//section[@id='comp-kyocojn1']")
        ActionChains(driver)\
            .scroll_to_element(articles)\
            .perform()
        time.sleep(5)
        view_more = driver.find_element(By.CSS_SELECTOR,"a[aria-label='View More'] span[class='StylableButton2545352419__label']")
        view_more.click()
        time.sleep(5)



try_it_out = Portfolio_Test()
try_it_out.eshas_test()
