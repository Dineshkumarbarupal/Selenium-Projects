# import webdriver 
from selenium import webdriver 
from time import sleep
# create webdriver object 
driver = webdriver.Chrome() 

# get geeksforgeeks.org 
driver.get("https://www.geeksforgeeks.org/") 

# write script 
script = "alert('Alert via selenium')"

# generate a alert via javascript 
driver.execute_script(script) 
sleep(20)
driver.quit()