#!/usr/bin/python3
## configuración de crontab cada 61 minutos
## */61 * * * * /usr/bin/python3 /home/mariotte/webscraping.py
from selenium import webdriver
import time
import random
import config
import os
import csv
#import urllib.request
#from bs4 import BeautifulSoup
## Librería para convertir una lista en un array
#import numpy as np
#while True:
while True:
 ## Abrir sitio web
 driver = webdriver.Chrome()
 #url = "https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM"
 #driver.get(url)
 driver.get("https://accounts.google.com/ServiceLogin?hl=es&passive=true&continue=https://groups.google.com&ec=GAZA0AM")
 ## Se pausa la pantalla durante 2 segundos para que tengamos tiempo de confirmar que llegó a la página correcta
 time.sleep(2)
 #print(driver.result)
 ## Añadir email
 Miemail = driver.find_element_by_id('identifierId')
 Miemail.clear()
 Miemail.send_keys(config.email)
 #time.sleep(10)
 ## Se añade la contraseña
 ## Se añade tiempo para que cargue
 time.sleep(2)
 button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
 button.click()
 time.sleep(3)
 Mipass = driver.find_element_by_xpath("//input[@name='password']")
 Mipass.clear()
 Mipass.send_keys(config.password)
 ## Presionar el botón de login
 ## Se añade tiempo para que cargue
 time.sleep(2)
 button = driver.find_element_by_xpath("//div[@class='VfPpkd-RLmnJb']")
 button.click()
 ## Se añade tiempo para que cargue
 time.sleep(9)
 ## Todos los grupos VP4Iue wWlgrf span DPvwYc qn15kb
 #enlacegrupos = driver.find_element_by_xpath("//a[@href='./all-groups']")
 #enlacegrupos.click()
 #time.sleep(5)
 ## Accediento a todos los grupos
 driver.get("https://groups.google.com/all-groups")
 ## Cliqueando en los grupos div > wWlgrf TE2Lw skrLqf, div > u7GkXe
 #clickgrupos = driver.find_elements_by_xpath("//div[@class='u7GkXe']")
 #clickgrupos.click()
 #print(clickgrupos)
 ## Obtener los emails de los departamentos
 #nododepartamentos = driver.find_elements_by_xpath("//div[@class='TE2Lw']")
 ## Obtener URL de a > href de los grupos; a > eRnJIb
 #print(nododepartamentos)
 ## Añadimos un break para que la ejecución del programa sea hasta aquí, esto nos servirá para pruebas
 ## Probamos que hasta aqui todo funcione correctamente, asi evitamos que se ejecute todo el programa
 #break
 ## BeautifulSoup y urllib
 ## Capturando el html
 #request = urllib.request.Request(url)
 #content = urllib.request.urlopen(request)
 ## Analizando el html 
 #parse = BeautifulSoup(content, 'html.parser')
 ## Para que los datos se guarden en un solo archivo csv primero se crean las cabeceras
 #with open('base_de_datos.csv', 'a') as csv_file:
   #writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
   ## First Name,Last Name,Position,Email, Departamento
   #writer.writerow(['First Name','Last Name','Position','Email', 'Departamento'])
 ## Obtener los nodos de las páginas
 nodospaginas = driver.find_elements_by_xpath("//div[@jsname='OCpkoe']")
 #print(len(nodopaginas))
 for i in nodospaginas:
  ## Obtener URL los grupos
  lista = []
  nodogrupos = driver.find_elements_by_xpath("//a[@class='eRnJIb']")
  #bucle=0
  #while bucle <= len(bonusbutton2):
  for x in nodogrupos:
   ## Aquí probe un manejo de excepciones para controlar un error de salida
   #try:
   lista = (x.get_attribute("href")+"/members")
   ## Se imprimen todos los titulos de los enlaces
   print ("Grupo: " + x.text.strip())
   ## Declaramos el nombre del archivo de cada grupo
   archivo = x.text.strip() + '.csv'
   ## Declaramos el nombre del archivo saneado para evitar errores
   #archivoSanitized = archivo.replace('/','-')
   #def processString(archivo):
   dictionary = {'<':'-', '>':'-', ':':'-', '"':'-', '|':'-', '?':'-', '*':'-', '/':'-'}
   transTable = archivo.maketrans(dictionary)
   archivoSanitized = archivo.translate(transTable)
   #print(archivoSanitized)
   ## Se imprimen todos las url de los grupos
   print ("Accediendo a " + lista)
   ## Convertir lista a un array
   #my_array = np.array(lista)
   #print(my_array)
   #print(my_array[1])
   #print(my_array[2])
   ## Guardamos la lista en un fichero temporal llamado lista.txt, esto lo use para pruebas
   #f = open("lista.txt", "a")
   #for i in lista:
   #    f.write(i)
   #f.close()
   ## Cambiar a una nueva ventana o pestaña
   #driver.switch_to.new_window('tab')
   driver.execute_script("window.open()")
   driver.switch_to.window(driver.window_handles[1])
   driver.get(lista)
   ## Se imprimen todos los enlaces
   #print (lista)
   ## Se pausa la pantalla durante 5 segundos para que tengamos tiempo de confirmar que llegó a la página correcta
   #time.sleep(5)
   ## Se proporcionan los atributos de los elementos html para extraer los datos.
   campo1 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
   campo2 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
   campo3 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
   campo4 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
   campo5 = driver.find_elements_by_xpath("//a[@class='p480bb Sq3iG']")
   campo6 = driver.find_elements_by_xpath("//h1[@class='KdPHLc']")
   #print(campo2)
   #print(campo1)
   #print(lista)
   ## Se escriben los datos extraídos en el archivo csv que antes creamos, no necesitaríamos controlar el contenido de los campos con el siguiente if
   #with open('base_de_datos.csv', 'a') as csv_file:
   ## Se controla que si no hay datos se cree o no se cree el archivo
   if len(campo1) == 0:
     print("El archivo " + archivoSanitized + " no se ha creado porque no contiene datos. \n")
   else:
     ## Se crea un directorio para guardar cada archivo archivo csv en una carpeta. Se usa la librería os
     directory = 'csv_files'
     path = os.path.join(directory)
     os.makedirs(path, exist_ok=True)
     ## Se escriben los datos extraídos en los archivos csv
     ## a Añade contenido progresivamente. Crea el archivo si no existe. Este lo usamos cuando necesitamos meter todo el contenido en un solo archivo.
     ## w+ Escritura y lectura. Sobrescribe el archivo si existe.
     with open("csv_files/" + archivoSanitized, 'w+') as csv_file:
      writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
      writer.writerow(['First Name','Last Name','Position','Email', 'Departamento'])
      ## First Name,Last Name,Position,Email,Departamento
      for col1,col2,col3,col4,col5 in zip(campo1, campo2, campo3, campo4, campo5):
        col2 = ""
        #if col3.text.strip().find("alu.") >= 0:
        if "alu.iesromerovargas" in col3.text.strip():
            col3 = ("Alumno");
        elif "fp.iesromerovargas" in col3.text.strip():
            col3 = ("Alumno");
        else:
            col3 = ("Profesor");
        col5 = campo6[0].text
        writer.writerow([col1.text.split("@")[0],col2, col3 ,col4.text.strip(), col5])
     print("El archivo " + archivoSanitized + " se ha creado. \n")
   ## Se cierra la ventana, en este caso la pestaña
   driver.close()
   ## Se cambia el controlador a la ventana o pestaña original
   driver.switch_to.window(driver.window_handles[0])
   time.sleep(1)
   #print(lista)
   ## Salimos de la excepción
   #except:
     #raise
     #pass
      #bucle +=1
   #driver.quit()
   #driver.execute_script("window.history.go(-1)")
   #driver.back()
   #driver.refresh()
   #time.sleep(10)
   ## Cliqueando en los Miembros kWxq2b VP4Iue gn3Lk class 
   #nodogrupos = driver.find_element_by_xpath("//a[@jslog='83026; track:click; index:0;']")
   #nodogrupos.click()
   ## Esperando para cargar
   #time.sleep(10)
   ## Se imprime el titulo del DOM y la URL en la que estamos navegando
   #print(driver.title);
   #print(driver.current_url);
  ## Presionar el botón siguiente
  botonpaginas = driver.find_element_by_xpath("//div[@jsname='OCpkoe']")
  botonpaginas.click()
  time.sleep(6)
 ## Se cierra la página
 driver.close()
 print("Todos los archivos han sido creados con éxito")
 ## Esperar 1h para analizar el bucle de nuevo
 time.sleep(60*60)
