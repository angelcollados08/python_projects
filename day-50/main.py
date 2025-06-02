from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

sleep(5)
#element_init = driver.find_element(By.CLASS_NAME,value="lxn9zzn")
login_button = driver.find_element(By.XPATH, value='//*[@id="c1323653706"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
login_button.click()

login_session = driver.find_element(By.XPATH, value='//*[@id="c1323653706"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[2]/div[2]/div[2]/div')
login_session.click()

sleep(5)
fb_login_window = driver.window_handles[0]
driver.switch_to.window(fb_login_window)
print(driver.title)
#element_init.click()