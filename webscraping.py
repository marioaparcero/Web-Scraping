#!/usr/bin/python3
## crontab settings every 61 minutes
## */61 * * * * /usr/bin/python3 /home/mariotte/webscraping.py
from selenium import webdriver
import time
import random
import urllib.request
from bs4 import BeautifulSoup
import csv
while True:
 #### Open webpage
 driver = webdriver.Chrome()
 #url = "https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM"
 #driver.get(url)
 driver.get("https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM")
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
### Press bonus button
 # Todos los grupos VP4Iue wWlgrf span DPvwYc qn15kb
 bonusbutton = driver.find_element_by_xpath("//a[@href='./all-groups']")
 bonusbutton.click()
 time.sleep(10)
 # Cliqueando en los grupos div wWlgrf TE2Lw skrLqf u7GkXe
 bonusbutton1 = driver.find_element_by_xpath("//div[@class='u7GkXe']")
 bonusbutton1.click()
 time.sleep(10)
 # Cliqueando en los Miembros kWxq2b VP4Iue gn3Lk class 
 #bonusbutton2 = driver.find_element_by_xpath("//div[@class='VP4Iue']")
 # 83026; track:click; index:0;
 bonusbutton2 = driver.find_element_by_xpath("//a[@jslog='83026; track:click; index:0;']")
 bonusbutton2.click()
 ###Esperando para cargar
 time.sleep(10)
 print(driver.title);
 print(driver.current_url);
 #url = 'https://groups.google.com/all-groups/'
 #url = 'file:///home/debian/Escritorio/lista.html'
 url = (driver.current_url)
 print(url);
# Fetching the html
 #request = urllib.request.Request(url)
 #content = urllib.request.urlopen(request)
# Parsing the html 
 #parse = BeautifulSoup(content, 'html.parser')
# Provide html elements' attributes to extract the data 
 text1 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text2 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text3 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text4 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 #for value in text1:
 #       print(value.text)
 #for value in text2:
 #       print(value.text)
 #for value in text3:
 #       print(value.text)
 #for value in text4:
 #       print(value.text)
#text3 = 'test@email.com'
#print(text3.split("@"))
 print(text2)
 print(text1)
# Writing extracted data in a csv file
 with open('index.csv', 'a') as csv_file:
   writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  #First Name,Last Name,Position,Email
   writer.writerow(['First Name','Last Name','Position','Email'])
   for col1,col2,col3,col4 in zip(text1, text2, text3, text4):
     col2 = ""
     if col3.text.strip().find("alu") >= 0:
         col3 = ("Alumno");
     else:
         col3 = ("Profesor");
     writer.writerow([col1.text.split("@")[0],col2, col3 ,col4.text.strip()])
 #text5 = "email@alum.ies.com";
 #if text5.find("alum") >= 0:
 #	print ("Alumno");
 #else:
 #	print ("profesor");

 ### Close page
 driver.close()
 time.sleep(60*60) #Esperar 1h para cliclear de nuevo, sino estará en bucle analizando
