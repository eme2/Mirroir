# -*- coding: utf-8 -*-
import requests
from io import open as iopen

url = "http://www.macantineetmoi.com/images/menu/sainte-clotilde/sainte-clotilde_S37.jpg"
file_name = "menu.jpg"
print("Récupération de ", url)
i = requests.get(url)
print("Après requests ", i.status_code)
if i.status_code == requests.codes.ok:
    with iopen(file_name, 'wb') as file:
        file.write(i.content)
