"""Un script simple para extraer datos de una página web
Este script permite al usuario extraer datos de una página web y luego exportar los datos a un archivo csv con columna (s).
"""
# libraries
import urllib.request
from bs4 import BeautifulSoup
import csv
# Put your URL here
url = 'https://groups.google.com/a/iesromerovargas.com/g/3a-profesorado/members'
#url = 'file:///home/usuario/Escritorio/lista.html'
# Fetching the html
request = urllib.request.Request(url)
content = urllib.request.urlopen(request)
# Parsing the html 
parse = BeautifulSoup(content, 'html.parser')
# Provide html elements' attributes to extract the data 
text1 = parse.find_all('a', attrs={'class': 'p480bb Sq3iG'})
text2 = parse.find_all('a', attrs={'class': 'p480bb Sq3iG'})
text3 = parse.find_all('a', attrs={'class': 'p480bb Sq3iG'})
text4 = parse.find_all('a', attrs={'class': 'p480bb Sq3iG'})
#text3 = 'test@email.com'
#print(text3.split("@"))
print(text2)
# Writing extracted data in a csv file
with open('index.csv', 'a') as csv_file:
  writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
  #First Name,Last Name,Position,Email
  writer.writerow(['First Name','Last Name','Position','Email'])
  for col1,col2,col3,col4 in zip(text1, text2, text3, text4):
    col2 = ""
    if col3.get_text().strip().find("alum") >= 0:
        col3 = ("Alumno");
    else:
        col3 = ("Profesor");
    writer.writerow([col1.get_text().split("@")[0],col2, col3 ,col4.get_text().strip()])
#text5 = "test2@email.com";
#if text5.find("alum") >= 0:
#	print ("Alumno");
#else:
#	print ("profesor");
