#!/usr/bin/python3
## configuración de crontab cada 61 minutos
## */61 * * * * /usr/bin/python3 /home/mariotte/webscraping.py
from selenium import webdriver
import time
import random
import csv
import config
while True:
 ## Abrir sitio web
 driver = webdriver.Chrome()
 driver.get("https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM")
 ## Se pausa la pantalla durante 2 segundos para que tengamos tiempo de confirmar que llegó a la página correcta
 time.sleep(2)
 ## Se añade el email
 Miemail = driver.find_element_by_id('identifierId')
 Miemail.clear()
 Miemail.send_keys(config.email)
 ## Presionar el botón siguiente
 button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
 button.click()
 time.sleep(3)
 ## Se añade la contraseña
 Mipass = driver.find_element_by_xpath("//input[@name='password']")
 Mipass.clear()
 Mipass.send_keys(config.password)
 ## Presionar el botón siguiente para iniciar sesión
 button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
 button.click()
 time.sleep(9)
 ## Accediento a todos los grupos
 driver.get("https://groups.google.com/all-groups")
 ## Obtener URL de los emails de los departamentos
 #nododepartamentos = driver.find_elements_by_xpath("//div[@class='TE2Lw']")
 ## Obtener URL los grupos
 nodogrupos = driver.find_elements_by_xpath("//a[@class='eRnJIb']")
 lista = []
 for x in nodogrupos:
  lista = (x.get_attribute("href")+"/members")
  ## Se imprimen todos los titulos de los enlaces
  print ("Departamento: " + x.text.strip())
  archivo = x.text.strip() + '.csv'
  print ("Creando el archivo..." + archivo)
  with open(archivo, 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(['First Name','Last Name','Position','Email', 'Departamento'])
  ## Se imprimen todos las url de los grupos
  print ("Accediendo a " + lista)
  driver.execute_script("window.open()")
  driver.switch_to.window(driver.window_handles[1])
  driver.get(lista)
  ## Se proporcionan los atributos de los elementos html para extraer los datos.
  campo1 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
  campo2 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
  campo3 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
  campo4 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
  campo5 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
  campo6 = driver.find_elements_by_xpath("//h1[@class='KdPHLc']")
  ## Se escriben los datos extraídos en un archivo csv
  with open(archivo, 'a') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for col1,col2,col3,col4,col5 in zip(campo1, campo2, campo3, campo4, campo5):
      col2 = ""
      if "alu.iesromerovargas" in col3.text.strip():
          col3 = ("Alumno");
      elif "fp.iesromerovargas" in col3.text.strip():
          col3 = ("Alumno");
      else:
          col3 = ("Profesor");
      col5 = campo6[0].text
      writer.writerow([col1.text.split("@")[0],col2, col3 ,col4.text.strip(), col5])
  ## Se cierra la ventana, en este caso la pestaña
  driver.close()
  ## Se cambia el controlador a la ventana o pestaña original
  driver.switch_to.window(driver.window_handles[0])
  time.sleep(1)
 ## Se cierra la página
 driver.close()
 ## Esperar 1h para analizar el bucle de nuevo
 time.sleep(60*60)
