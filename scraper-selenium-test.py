#Given a myfonts URL, extract all the tags.

from bs4 import BeautifulSoup
import pandas
from requests import get
import re

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import time

i=0
list_of_fonts = []

list_names = []
list_creators = []
list_prices = []
list_styles = []


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# A randomizer for the delay
seconds = .5 + (random.random() * 2)
# create a new Chrome session
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(30)
# driver.maximize_window()



url = 'https://www.myfonts.com/search/release_date%3A%5B%2A+TO+2020-12-31T23%3A59%3A59.000Z%5D/fonts/'

# navigate to the application home page
driver.get(url)
time.sleep(seconds)

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight+1000);")

    # Wait to load page
    time.sleep(seconds)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


html = driver.page_source
html_soup = BeautifulSoup(html, 'html.parser')
type(html_soup)

df = pandas.DataFrame(data={"Font Name": list_names, "Foundry/Creator": list_creators, "Price": list_prices, "Styles": list_styles})
df.to_csv("./fonts.csv", sep=',',index=False)
