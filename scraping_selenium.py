#!/usr/bin/python
import selenium
import time
from selenium import webdriver
import selenium.webdriver.chrome.service as service
service = service.Service('X:/Drive/Software/chromedriver_win32/chromedriver.exe')
service.start()
capabilities = {'chrome.binary': 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'}
driver = webdriver.Remote(service.service_url, capabilities)

#driver = webdriver.Chrome('X:/Drive/Software/chromedriver_win32/chromedriver.exe')
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import selenium.webdriver.common.alert


# go to the home page
driver.get("http://jhu.eblib.com/patron/SearchResults.aspx?ca=1&t=category&r=15&fl=1&p=1")
driver.maximize_window()
#this is where chrome stores the default profile
#C:\Users\Nicolae\AppData\Local\Google\Chrome\User Data\Default

#sign into JHU system
inputElement = driver.find_element_by_name("USER")
inputElement.send_keys("ndone1")
inputElement = driver.find_element_by_name("PASSWORD")
inputElement.send_keys("Balar!!007")
inputElement = driver.find_element_by_name("submit1")
driver.find_element_by_id("submit1").click()

#wait to load Elib page
WebDriverWait(driver, 5).until(EC.title_contains("EBL Patron"))
print driver.title

#a good link looks like this: http://jhu.eblib.com/patron/SearchResults.aspx?ca=1&t=category&r=15&fl=1&p=1
#ca=1 means first category (agriculture); r=15 means show 15 books per page; fl=1 means books written in English
#p=1 means first page; if I want to show too many books on the page, Chrome will give me an error; so better to show 100 and then move to next page
#categories to take first: 3;4;6;28;29;34;47;48
#all categories:
#1Agriculture
#2Architecture
#3Business / Management
#4Computer Science / IT
#5Education
#6Engineering
#7Engineering: Chemical
#8Engineering: Civil
#9Engineering: Construction
#10Engineering: Electrical
#12Engineering: Environmental
#13Engineering: Manufacturing
#14Engineering: Mechanical
#15Engineering: Mining
#16Environmental Studies
#51Fiction
#17Fine Arts
#18General Works / Reference
#19Geography / Travel
#20Health
#21History
#22Home Economics
#23Journalism
#24Language / Linguistics
#25Law
#26Library Science
#27Literature
#28Mathematics
#29Medicine
#30Military Science
#31Museums
#32Nursing
#50Pharmacy
#33Philosophy
#34Political Science
#35Psychology
#36Publishing
#37Religion
#38Science
#39Science: Anatomy / Physiology
#40Science: Astronomy
#41Science: Biology / Natural History
#42Science: Botany
#43Science: Chemistry
#44Science: Geology
#45Science: Physics
#46Science: Zoology
#47Social Science
#48Sport & Recreation

#booktitles = driver.find_elements_by_id("rel")
#print booktitles

bookids = ['4471535']

for book in bookids:
	address = 'http://jhu.eblib.com/patron/Read.aspx?p=' + book
	driver.get(address)
	print address
	download = driver.find_element_by_css_selector('a.left-rotate-text.left-tab-download-padding')
	download.click()
	pdf = driver.find_element_by_css_selector('input.ebook-format-rb')
	pdf.click()
	takeit=driver.find_element_by_css_selector('input.ebook-format-btn')
	takeit.click()
	#driver.find_element_by_xpath('//*[@id="left-content-holder"]/form/input[3]').click()
print "done"

#driver.quit()

#driver.find_element_by_xpath('//*[@id="tab-download"]/a').click()

#left-content-holder > form > input.ebook-format-btn