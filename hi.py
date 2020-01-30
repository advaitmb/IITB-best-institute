print("Starting stuff")
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import numpy
import pandas

##Link list
list_link = []

seconds = 3 + (random.random() * 2)

##Initiate Chrome for Linkedin login
opts = webdriver.ChromeOptions()
opts.binary_location = "D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
##prefs = {"profile.managed_default_content_settings.images": 2}
##opts.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options = opts)

driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

##username
username = driver.find_element_by_id('username')
username.send_keys('iitbestinstitute@gmail.com')

##password
password = driver.find_element_by_id('password')
password.send_keys('iloveiit' + Keys.RETURN)

## submit = driver.find_elements_by_class_name('btn__primary--large from__button--floating')
##submit = driver.find_elements_by_tag_name('button')
##submit.click()
driver.get('https://www.linkedin.com/school/indian-institute-of-technology-bombay/people/')
time.sleep(5)

##======================THIS IS THE SCROLLING FUNCTION=========================================

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

##while True:
for i in range(1,10):
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight+1000);")

    # Wait to load page
    time.sleep(seconds)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height



##============THIS PART PARSES THE PAGE AND PRINTS OT THE LINKS===============================

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
##print(soup.prettify())

##linkedin_urls = driver.find_elements_by_id('ember297')
##linkedin_urls = [url.text for url in linkedin_urls]
##print(linkedin_urls[0])

##print(soup.find_all('a')[19].attrs)
items = soup.find_all('a')
print(len(items))
print(items[19]['href'])
print('=====================================================')
print(items[20]['href'])
print('=====================================================')
for link in items:
    bla = link['href']
    print(bla)
    list_link.append(bla)


##================TILL HERE ==========================================================
##Pandas csv generator
df = pandas.DataFrame(data={"Profile link": list_link})
df.to_csv("alumni.csv")

