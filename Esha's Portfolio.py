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
wait = WebDriverWait(driver,10)
data=["Stephanie","Ayuba","stephanieesha@gmail.com"]
message="this is you from the future, aliens have attacked humanity the world has changed we are now buying air. My advice for you is to stock up on oxygen else you will die"
class Portfolio_Test():
   
    def open_page(self):
        driver.get(URL)
        driver.maximize_window()
        time.sleep(3)
    def scroll_to_bottom(self):
        # Scroll to Bottom of Webpage
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)

    def click_top_button(self):
        #click on scroll to top button
        scroll = driver.find_element(By.CSS_SELECTOR,"a[aria-label='Up'] div[class='StylableButton2545352419__container']")
        scroll.click()
        time.sleep(5)

    def click_about_link(self):
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

        # #looping through the projects and clicking cancel
        for i in project:
            i.click()
            time.sleep(5)
            # try:
            #     next = wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_2fmZJ']//*[name()='svg']")))
            #     for j in range(2):
            #         next.click()
            #         time.sleep(7)
            # finally:
            close= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='_2DPZA']//*[name()='svg']")))
            close.click()
        time.sleep(3)


    def hover_automation_testing(self):
        #find automating testing and hover over
        section = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"section[id='comp-l3onkfps'] div[class='_1uldx']")))
        automated_testing = section.find_element(By.CSS_SELECTOR,"#comp-l3onn2sv_video")
        ActionChains(driver) \
            .move_to_element(automated_testing) \
            .perform()
        time.sleep(10)
    

    def scroll_to_article_Section(self):
        #needs work
        #scroll to article section and click view more
        articles = driver.find_element(By.XPATH,"//section[@id='comp-kyocojn1']")
        ActionChains(driver) \
            .scroll_to_element(articles) \
            .perform()
        time.sleep(5)

        view_more = driver.find_element(By.CSS_SELECTOR,"a[aria-label='View More'] span[class='StylableButton2545352419__label']")
        view_more.click()
        time.sleep(5)
    def click_like_button(self):
        like= wait.until(EC.presence_of_element_located((By.XPATH,"//div[@class='like-button LtaU1R']//*[name()='svg']")))
        like.click()
        time.sleep(5)
        back = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class='_2wYm8']//div[@class='_3bLYT _2OIRR']//*[name()='svg']")))
        time.sleep(5)
        back.click()

    def fill_in_contact_details(self):
        contact =wait.until(EC.presence_of_element_located((By.XPATH,"//section[@id='comp-kyocojnl']")))
        ActionChains(driver) \
            .move_to_element(contact) \
            .perform()
        time.sleep(5)

        #fill in contact form
        inputs = contact.find_elements(By.TAG_NAME,"input")
        count=0
        for i in inputs:
            i.send_keys(data[count])
            count += 1
        time.sleep(5)
        textarea = contact.find_element(By.TAG_NAME,"textarea")
        textarea.send_keys(message)
        time.sleep(5)
        submit = contact.find_element(By.XPATH,"//button[@aria-disabled='false']")
        submit.click()
        time.sleep(5)

    def click_on_social_links(self):
        contact = wait.until(EC.presence_of_element_located((By.XPATH, "//section[@id='comp-kyocojnl']")))
        socials = contact.find_element(By.XPATH,"//ul[@aria-label='Social Bar']")
        list = socials.find_elements(By.TAG_NAME,"li")
        for i in list:
            i.click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(5)
            driver.switch_to.window(driver.window_handles[0])

    def close_work(self):
        driver.quit()
        print("Completed test successfully")



work = Portfolio_Test()
work.open_page()
work.scroll_to_bottom()
work.click_top_button()
work.click_about_link()
work.switch_to_new_window()
work.click_on_back_button()
work.switch_to_previous_window()
work.click_on_contact_button()
work.scroll_to_top()
work.go_to_selected_projets()
work.hover_automation_testing()
work.scroll_to_article_Section()
work.click_like_button()
work.fill_in_contact_details()
work.click_on_social_links()
work.scroll_to_top()
work.close_work()
