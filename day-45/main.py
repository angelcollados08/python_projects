from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")
elements = driver.find_elements(By.CSS_SELECTOR, value=".event-widget.last time")
names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget.last li a")
#price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

for e in elements:
    print(e.text)
for a in names:
    print(a.text)

events = {}

for n in range(len(names)):
    events[n] = {
        "time": elements[n].text,
        "event": names[n].text,
    }

print(events)
driver.quit()
