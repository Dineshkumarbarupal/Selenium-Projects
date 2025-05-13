from selenium import webdriver
from selenium.webdriver import ChromeOptions
from time import sleep

options = ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/NSG/AppData/Local/Google/Chrome/User Data/profile for selenium')
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)
sleep(1)
driver.get("https://web.whatsapp.com")

sleep(20)




















