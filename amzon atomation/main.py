from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


li_class  = '_sv4'
driver = webdriver.Chrome()
driver.get('https://facebook.com')

def get_ui_list(li_class,driver):
    try:
        list = driver.find_element(By.CLASS_NAME,li_class)
        print(list.text)
     
        # for elem in list:
        #     with open('all_list.text','w',encoding='utf-8') as file:
        #         file.write(elem.text)
       

    except Exception as e:
        print(e,'An error occerred')          

get_ui_list(li_class,driver)