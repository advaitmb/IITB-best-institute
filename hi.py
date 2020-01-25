print(2+2)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
opts = webdriver.ChromeOptions()
opts.binary_location = "D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(chrome_options = opts)
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
username = driver.find_element_by_id('username')
username.send_keys('rishabhisar@gmail.com')
password = driver.find_element_by_id('password')
password.send_keys('puru@1997' + Keys.RETURN)
## submit = driver.find_elements_by_class_name('btn__primary--large from__button--floating')
##submit = driver.find_elements_by_tag_name('button')
##submit.click()
driver.get('https://www.linkedin.com/school/indian-institute-of-technology-bombay/people/')
time.sleep(5)



html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))
##print(soup.prettify())

##linkedin_urls = driver.find_elements_by_id('ember297')
##linkedin_urls = [url.text for url in linkedin_urls]
##print(linkedin_urls[0])

##print(soup.find_all('a')[19].attrs)

print(soup.find_all('a')[19]['href'])
print('=====================================================')
print(link['href'] for link in soup.find_all('a'))



