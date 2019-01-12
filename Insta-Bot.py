from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chromedriver ="/Users/Lenovo/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

inputs = browser.find_element_by_xpath('//input[@name="username"]')
inputs.click()
inputs.send_keys('Username Or Email')

ayush = browser.find_element_by_xpath('//input[@name="password"]')
ayush.click()
ayush.send_keys('password')

a = browser.find_element_by_xpath('//button[@type="submit"]')
a.click()

sleep(5)
b = browser.find_element_by_xpath('//button[text()="Not Now"]')
b.click()
sleep(3)
c = browser.find_element_by_xpath('//span[@aria-label="Like"]')

while (True):
	c.click()
	c = browser.find_element_by_xpath('//span[@aria-label="Like"]')
	sleep(2)








