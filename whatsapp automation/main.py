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

class WhatsappAutomation:
    def __init__(self,url, group_list, xpath,scroll_xpath):
        self.url = url 
        self.group_list = group_list
        self.xpath = xpath
        self.scroll_xpath = scroll_xpath
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/Users/NSG/AppData/Local/Google/Chrome/User Data/profile for selenium') 
        options.add_argument('--profile-directory=Profile 1')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.action = ActionChains(self.driver)
        self.driver.get(self.url)
        for group in self.group_list:
            if group:
                self.search(group)
                self.find_num(self.xpath)
                self.scroll_to_bottum(self.scroll_xpath)
                number = self.extract_number()
                self.close_button()
                self.write_into_csv(number)
            else:
                print("successfuly write search all groups")
            
    def search(self,search_query):
        # assert "(3) WhatsApp Business" in driver.title
        elem = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div')))
        self.action.click(elem).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).send_keys(search_query).send_keys(Keys.ENTER).perform()

    def func(self, path):
        elems = WebDriverWait(self.driver,20).until(EC.presence_of_element_located((By.XPATH, path)))
        return elems
    
    def find_num(self,xpath):
        elem = self.func(xpath)
        elem.click()

    def scroll_to_bottum(self , xpath):
        side_bar = self.func(xpath)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", side_bar)
        print(side_bar.is_displayed())
      
    def is_valid_number(self,text):
        return re.fullmatch(r'(\+91[\s\-]?)?\d{10}',text) is not None
    
    def extract_number(self):
        show_num_xpath = "//*[contains(text(), 'View all')]"
        div_scroll_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]'
    
        button = self.func(show_num_xpath)
        button.click()
        num_scroll_containar = self.func(div_scroll_xpath)

        all_number = set()
        previous_count = 0
        while True:
            self.driver.execute_script('arguments[0].scrollTop += 500',num_scroll_containar)
            sleep(4)

            number_container = self.driver.find_elements(By.CLASS_NAME, '_ak8o')
            # next_div_num = self.driver.find_elements(By.CLASS_NAME, '_ao3e')
             
            for elem in number_container:
                number = elem.text
                all_number.add(number)

            current_count = len(all_number)
            if current_count == previous_count:
               break
            previous_count = current_count
        return all_number
        sleep(2)
    
    def close_button(self):
        button_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/header/div/div[1]/div'
        button = self.func(button_xpath)
        button.click()
        sleep(2)

    def write_into_csv(self, all_number):
        with open("सरकारी रिजल्ट (SKResult.Com)  42.csv", "a", encoding='Utf-8') as file:
            for num in all_number:
               file.write(f"{num}\n")

        # self.driver.close()

url = "https://web.whatsapp.com/"
# number find xpath.
xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
# scroll to bottum xpath.
scroll_xpath = '//*[@id="app"]/div/div[3]/div/div[5]/span/div/span/div/div/div'
# Group list for search.
group_list = ["सरकारी रिजल्ट (SKResult.Com)  42"]

whatsapp_obj = WhatsappAutomation(url, group_list, xpath,scroll_xpath) 
# for group in group_list:
#     if group:
#         search_query = group
#         whatsapp_obj.search(search_query)
#         whatsapp_obj.find_num(xpath)
#         whatsapp_obj.scroll_to_bottum(scroll_xpath)
#         numbers = whatsapp_obj.extract_number()
#         whatsapp_obj.close_button()
#         whatsapp_obj.write_into_csv(numbers)

# whatsapp_obj.driver.quit()
