from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

#element.click()
name = driver.find_element(By.NAME,value="fName")
name.send_keys("Python")

name2 = driver.find_element(By.NAME,value="lName")
name2.send_keys("second")

email = driver.find_element(By.NAME,value="email")
email.send_keys("Python@something",Keys.ENTER)

button = driver.find_element(By.CLASS_NAME,value="btn.btn-lg.btn-primary.btn-block")
button.click()
#driver.quit()