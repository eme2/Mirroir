#!/usr/local/bin/python3
#--*-- coding:utf8 --*--

import requests, dateConv
from bs4 import BeautifulSoup

class MenuCantine:
  def __init__(self):
    self.url = "http://eurometropole.apimobile.fr/LesMenus/Index/caf9f5a9-2f0c-4617-bca9-3ea37af1d54a?date="
    self.soup = None
    self.menus = []
    
  def load(self):
    d = dateConv.DateConv()
 
    requete = requests.get(self.url+d.dateJourApi())
    page = requete.content
    self.soup = BeautifulSoup(page, 'html.parser')
  

  def lstMenu(self):
    dateMenu = self.soup.find('span', attrs={"class":"subtitle"})
    self.menus.append("menu du {}".format(dateMenu.text))
    d = self.soup.find(class_="dish-name")
    f = self.soup.findAll('ul', attrs={"class":"dishes-list"})

    for i in range(len(f)):
      transition = f[i].findAll('a')
    
      for j in range(len(transition)):
        menu = transition[j].find('span', attrs={"class":"intitule"})
        prix = transition[j].find('span', attrs={"class":"dish-price"})
        self.menus.append("{} - {}".format(menu.text, prix.text))
    return self.menus
