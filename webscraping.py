#!/usr/bin/python3
## crontab settings every 61 minutes
## */61 * * * * /usr/bin/python3 /home/mariotte/webscraping_release.py
from selenium import webdriver
import time
import random
while True:
 #### Open webpage
 driver = webdriver.Chrome()
 driver.get ("https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM")
 # wait to load
 time.sleep(3)
 #print(driver.result)
 ### Add email
 #Myname = driver.find_element_by_id('InputEmail')
 Myname = driver.find_element_by_id('identifierId')
 Myname.clear()
 Myname.send_keys(config.email)
 #time.sleep(10)
 ### Add password
 # Add random times
 n = random.randint(0,10)
 time.sleep(n)
 #mypass = driver.find_element_by_id('InputPass')
 button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
 button.click()
 time.sleep(3)
 #mypass = driver.find_element_by_class('whsOnd zHQkBf')
 mypass = driver.find_element_by_xpath("//input[@name='password']")
 mypass.clear()
 mypass.send_keys(config.password)
 ### Press login button
 # Add random times
 n = random.randint(0,10)
 time.sleep(n)
 #button = driver.find_element_by_xpath("//button[@class='btn btn-base mt-4']")
 button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
 button.click()
 ### go to bonuses page
 #wait to load
 time.sleep(10)
 driver.get("https://groups.google.com/all-groups")
 ###Wait to load
 time.sleep(10)
 ### Press bonus button
 bonusbutton = driver.find_element_by_id('get-bonus')
 bonusbutton.click()
 bonusbutton1 = driver.find_element_by_id('bonus-timer')
 bonusbutton1.click()
 #button2 = driver.find_element_by_xpath("//button[@class='btn btn-base text-uppercase mt-4']")
 #button2.click()
 ###Wait to load
 time.sleep(10)
 print("Cliqueamos una vez más")
 ### Close page
 driver.close()
 time.sleep(60*60) #wait one hour before clicking again
