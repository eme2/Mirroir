import requests
import dateConv
from io import open as iopen

dt = dateConv.DateConv()
jourSem = dt.jourSem()
print("Jour de la semaine : ", jourSem)
if jourSem > 5:
    sem = str(dt.numSem()+1)
else:
    sem = str(dt.numSem())

url = "http://www.macantineetmoi.com/images/menu/sainte-clotilde/sainte-clotilde_S"+sem+".jpg"
file_name = "menu.jpg"
print("Recuperation de ", url)
i = requests.get(url, stream=True)
print("Apres requests ", i.status_code)
j=0
if i.status_code == requests.codes.ok:
    with iopen(file_name, 'wb') as file:
        for chunk in i.iter_content(1024):
            #print("> ", j)
            j = j+1
            file.write(chunk)
print("Terminé ")