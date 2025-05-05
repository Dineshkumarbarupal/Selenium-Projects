from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('user-data-dir=C:\\Users\\NSG\\AppData\\Local\\Google\\Chrome\\User Data')
options.add_argument('--profile-directory=Profile 4') #e.g. Profile 3
options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

url = 'https://www.amazon.in'
search_query =  "green tee"
search_button_xpath = '//*[@id="twotabsearchtextbox"]'

def find_elem(url,search_button_xpath,send_key,options):
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        print(driver.title)
        assert "Amazon.in" in driver.title
        elem = driver.find_element(By.XPATH,search_button_xpath)
        # elem.clear()
        elem.send_keys(send_key)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

        print(driver.title)
        page_source = driver.page_source

        with open('amazon page source.html','w',encoding='utf=8') as file:
            file.write(page_source)
        driver.close()

    except Exception as e:
        print(e, "An error occurred")

find_elem(url,search_button_xpath,search_query,options)

