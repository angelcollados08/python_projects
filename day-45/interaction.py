from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

element = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#element.click()
bar = driver.find_element(By.NAME,value="search")
bar.send_keys("Python",Keys.ENTER)
driver.quit()