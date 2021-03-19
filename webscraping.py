#!/usr/bin/python3
## crontab settings every 61 minutes
## */61 * * * * /usr/bin/python3 /home/mariotte/webscraping.py
from selenium import webdriver
import time
import random
import urllib.request
from bs4 import BeautifulSoup
import csv
#while True:
 # Abrir sitio web
driver = webdriver.Chrome()
 #url = "https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM"
 #driver.get(url)
driver.get("https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM")
 # Se añade tiempo para que cargue
time.sleep(2)
 #print(driver.result)
 # Añadir email
Myname = driver.find_element_by_id('identifierId')
Myname.clear()
Myname.send_keys(config.email)
 #time.sleep(10)
 # Añadir contraseña
 # Se añade tiempo para que cargue
time.sleep(2)
button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
button.click()
time.sleep(3)
mypass = driver.find_element_by_xpath("//input[@name='password']")
mypass.clear()
mypass.send_keys(config.password)
 # Presionar el boton de login
 # Se añade tiempo para que cargue
time.sleep(2)
button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
button.click()
 ### go to bonuses page
 # Se añade tiempo para que cargue
time.sleep(9)
### Press bonus button
 # Todos los grupos VP4Iue wWlgrf span DPvwYc qn15kb
bonusbutton = driver.find_element_by_xpath("//a[@href='./all-groups']")
bonusbutton.click()
time.sleep(5)
 # Cliqueando en los grupos div > wWlgrf TE2Lw skrLqf, div > u7GkXe
bonusbutton1 = driver.find_elements_by_xpath("//div[@class='u7GkXe']")
 #bonusbutton1.click()
 #print(bonusbutton1)
 # Obtener URL de los emails de los departamentos div > TE2Lw
 # bonusbutton1 = driver.find_elements_by_xpath("//div[@class='TE2Lw']")
 # Obtener URL de a > href de los grupos; a > eRnJIb
bonusbutton2 = driver.find_elements_by_xpath("//a[@class='eRnJIb']")
 #break
 #print(bonusbutton1)
with open('base_de_datos.csv', 'a') as csv_file:
  writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  #First Name,Last Name,Position,Email
  writer.writerow(['First Name','Last Name','Position','Email', 'Departamento'])
lista = []
for x in bonusbutton2:
 lista = (x.get_attribute("href")+"/members")
 print ("Accediendo a " + lista)
 #Se imprimen todos los titulos de los enlaces
 print ("Departamento: " + x.text.strip())
 time.sleep(2)
 #driver.switch_to.new_window('tab')
 driver.execute_script("window.open()")
 driver.switch_to.window(driver.window_handles[1])
 driver.get(lista)
 # Se imprimen todos los enlaces
 #print (lista)
 # Se pausa la pantalla durante 5 segundos para que tengamos tiempo de confirmar que llegó a la página correcta
 time.sleep(2)
 # Se proporcionan los atributos de los elementos html para extraer los datos.
 text1 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text2 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text3 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text4 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text5 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
 text6 = driver.find_elements_by_xpath("//h1[@class='KdPHLc']")
 #print(text2)
 #print(text1)
 #print(lista)
# Se escriben los datos extraídos en un archivo csv
 with open('base_de_datos.csv', 'a') as csv_file:
   writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  #First Name,Last Name,Position,Email
   for col1,col2,col3,col4,col5 in zip(text1, text2, text3, text4, text5):
     col2 = ""
     if col3.text.strip().find("alu") >= 0:
         col3 = ("Alumno");
     else:
         col3 = ("Profesor");
     col5 = text6[0].text
     writer.writerow([col1.text.split("@")[0],col2, col3 ,col4.text.strip(), col5])
 #driver.execute_script("window.history.go(-1)")
 #Se cierra una ventana o pestaña
 driver.close()
 #Se cambia el controlador a la ventana o pestaña original
 driver.switch_to.window(driver.window_handles[0])
 time.sleep(10)
 print(lista)
 #driver.quit()
 #driver.back()
 #driver.refresh()
 #time.sleep(10)
 #break
 # Cliqueando en los Miembros kWxq2b VP4Iue gn3Lk class 
 #bonusbutton2 = driver.find_element_by_xpath("//a[@jslog='83026; track:click; index:0;']")
 #bonusbutton2.click()
 ###Esperando para cargar
 #time.sleep(10)
 #print(driver.title);
 #print(driver.current_url);
 ### Se cierra la página
#driver.close()
time.sleep(60*60) #Esperar 1h para cliclear de nuevo, sino estará en bucle analizando
