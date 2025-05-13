from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import re


class CreateWhatsappGroup:
    def __init__(self, url):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('--user-data-dir=C:/Users/NSG/AppData/Local/Google/Chrome/User Data/profile for selenium')
        self.option.add_argument('--profile-directory=Profile 1')
        self.url = url
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.get(self.url)
        self.action = ActionChains(self.driver)
    
    def find_elem(self,xpath):
        elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH,xpath)))
        return elem

    def new_group_page(self, menu_button_xpath, new_group_button):
        menu_button = self.find_elem(menu_button_xpath)
        menu_button.click()
        sleep(2)
        new_group_btn = self.find_elem(new_group_button)
        new_group_btn.click()
        sleep(2)

    def create_group(self, fill_num_box_xpath, arrow_xpath, group_name_box_xpath, group_name, create_group):
        fill_box = self.find_elem(fill_num_box_xpath)
        with open("सरकारी रिजल्ट (SKResult.Com)  42.csv") as file:
            for num in file:
                if num:
                    num = num.strip()
                    self.action.move_to_element(fill_box).click().send_keys(num).perform()
                    sleep(4)
                    self.action.move_to_element(fill_box).send_keys(Keys.ENTER).perform()
                    sleep(4)
                else:
                    print("All number filled")
                    break
        
        arrow = self.find_elem(arrow_xpath)
        arrow.click()
        sleep(3)

        group_name_box = self.find_elem(group_name_box_xpath)
        group_name_box.click()
        sleep(4)
        group_name_box.send_keys(group_name)
        sleep(5)

        create_group_btn = self.find_elem(create_group)
        create_group_btn.click()
        sleep(6)

url = "https://web.whatsapp.com/"
menu_button_xpath = '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[2]/button'
new_group_button = '//*[@id="app"]/div/span[5]/div/ul/div/div[2]/li/div/span'
fill_num_box_xpath = '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/div[2]/input'
arrow_xpath = '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div/span/div/div/span'
group_name_box_xpath = '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div/div[1]/div[2]/div/div[2]/div/div/div'
create_group = '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div/span/div/div/div'
group_name = 'Part Time Earning1'
whatsappobj = CreateWhatsappGroup(url)
whatsappobj.new_group_page(menu_button_xpath, new_group_button)
whatsappobj.create_group(fill_num_box_xpath, arrow_xpath, group_name_box_xpath, group_name, create_group)


        