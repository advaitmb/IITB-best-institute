from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import pandas

#Link list
list_link = []

# A randomizer for the delay
seconds = 5 + (random.random() * 2)

#Initiate Chrome for Linkedin login
opts = webdriver.ChromeOptions()
opts.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = opts)
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#username
username = driver.find_element_by_id('username')
username.send_keys('rishabhisar@gmail.com')

#password
password = driver.find_element_by_id('password')
password.send_keys('puru@1997' + Keys.RETURN)

#Open linkedin for iitb links
driver.get('https://www.linkedin.com/school/indian-institute-of-technology-bombay/people/')
time.sleep(5)

#Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

#while True:
dang = 1
while dang < 5:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight+1000);")

    # Wait to load page
    time.sleep(seconds)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
    dang = dang + 1;

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

##Link Finder
items = soup.find_all('a')
for bla in items:
    link = bla['href']
    print(link)
    list_link.append(link)

##Pandas csv generator
df = pandas.DataFrame(data={"Profile link": list_link})
df.to_csv("alumni.csv")
