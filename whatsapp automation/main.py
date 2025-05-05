from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

class WhatsappAutomation:
    def __init__(self,url):
        self.url = url 
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=C:/Users/NSG/AppData/Local/Google/Chrome/User Data') 
        options.add_argument('--profile-directory=Profile 3')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
        self.action = ActionChains(self.driver)
        self.driver.get(self.url)
        
    def search(self,search_query):
        sleep(10)
        # assert "(3) WhatsApp Business" in driver.title
        elem = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[2]/div')))
        self.action.click(elem).send_keys(search_query).send_keys(Keys.ENTER).perform()

        sleep(20)

    def func(self, path):
        elems = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, path)))
        return elems
    
    def find_num(self,xpath):
        elem = self.func(xpath)
        elem.click()

    def scroll_to_bottum(self , xpath):
        side_bar = self.func(xpath)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", side_bar)
        print(side_bar.is_displayed())
        sleep(15)

    def extract_number(self):
        show_num_xpath = '//*[@id="app"]/div/div[3]/div/div[5]/span/div/span/div/div/div/section/div[10]/div[2]/div[2]/div/div[2]/div/div'
        div_scroll_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]'
        number_xpath = '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div/div[2]/div/div/div/div[9]/div/div/div[2]/div[1]/div/div/div/span'

        button = self.func(show_num_xpath)
        button.click()
        sleep(2)
        num_scroll_containar = self.func(div_scroll_xpath)

        number_container = num_scroll_containar.find_element(By.CLASS_NAME, '_ak8q')

        all_number = set()
        for _ in range(200):
            self.driver.execute_script('arguments[0].scrollTop += 300',num_scroll_containar)
            sleep(2)

            for elem in number_container:
                number = elem.text.strip()
                if number:
                    all_number.add(number)

        print(all_number)


        self.driver.close()


url = "https://web.whatsapp.com/"
# number find xpath
xpath = '//*[@id="main"]/header/div[2]/div[2]/span'
# scroll to bottum xpath
scroll_xpath = '//*[@id="app"]/div/div[3]/div/div[5]/span/div/span/div/div/div'

search_query = "Team Guruvandna"
whatsapp_obj = WhatsappAutomation(url)
whatsapp_obj.search(search_query)
whatsapp_obj.find_num(xpath)
whatsapp_obj.scroll_to_bottum(scroll_xpath)
whatsapp_obj.extract_number()


