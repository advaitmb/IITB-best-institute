print(2+2)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
opts = webdriver.ChromeOptions()
opts.binary_location = "D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(chrome_options = opts)