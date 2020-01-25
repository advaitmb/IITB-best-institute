print(2+2)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

#lists
list_names = []
list_position = []
list_batch = []
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
## submit = driver.find_elements_by_class_name('btn__primary--large from__button--floating')
##submit = driver.find_elements_by_tag_name('button')
##submit.click()

#Open linkedin for iitb links
driver.get('https://www.linkedin.com/school/indian-institute-of-technology-bombay/people/')
time.sleep(5)

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
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
##print(soup.prettify())

##linkedin_urls = driver.find_elements_by_id('ember297')
##linkedin_urls = [url.text for url in linkedin_urls]
##print(linkedin_urls[0])

##print(soup.find_all('a')[19].attrs)

##Rishabh's link finder
#print(soup.find_all('a')[19]['href'])
#print('=====================================================')
#print(link['href'] for link in soup.find_all('a'))

##Pandas csv generator
df = pandas.DataFrame(data={"Name": list_names, "Current Position": list_position, "Graduation Batch": list_batch, "Profile link": list_link})
df.to_csv("./alumlinks.csv", sep=',',index=False)
