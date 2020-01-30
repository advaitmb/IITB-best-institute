print(2+2)
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

opts = webdriver.ChromeOptions()
opts.binary_location = "D:\Program Files (x86)\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(chrome_options = opts)

##Items of Interest
##DIV with class "result-card__contents experience-item__contents"
##DIV with class "result-card experience-item"  ##Explore this structure in detail
            ## DIV class "result-card__contents experience-item__contents"
                ## H3 class "result-card__title experience-item__title"  take html text of that
                ##h4 class "result-card__subtitle experience-item__subtitle" >> take html text of the a tg inside it
                
##DIV with class "experience-group experience-item" ##This is the big group
