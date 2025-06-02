from bs4 import BeautifulSoup
import requests
response = requests.get("https://appbrewery.github.io/instant_pot/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
price = soup.find(name="span", class_= "aok-offscreen").getText().split("$")
prince_numer = float(price[1])
print(prince_numer)