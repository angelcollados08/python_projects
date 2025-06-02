from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Speed:
    def __init__(self) -> None:
        self.download = 0
        self.upload = 0
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
    
    def get_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(5)
        cookie_button = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        cookie_button.click()

        speed_button = self.driver.find_element(By.CLASS_NAME,value="start-text")
        speed_button.click()
        sleep(60)
        self.download = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.upload = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text
        print(self.download)
        print(self.upload)


speed = Speed()
#speed.get_speed()


#button_notification = driver.find_element(By.CLASS_NAME, value="notification-dismiss.close-btn")
#button_notification.click()


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "/Users/angel"
TWITTER_EMAIL = "angelsasuke1@hotmail.es"
TWITTER_PASSWORD = "narutol123"

speed.driver.get("https://x.com/i/flow/login")
sleep(5)


button_log = speed.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
#button_log.click()
button_log.send_keys(TWITTER_EMAIL)
button_log.send_keys(Keys.ENTER)

button_pass = speed.driver.find_element(By.XPATH,value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
button_pass.send_keys(TWITTER_PASSWORD)
button_pass.send_keys(Keys.ENTER)