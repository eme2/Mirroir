#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests
import json

# Gestion des donnees du site thingspeak
class Meteo:
  def __init__(self, key):
    self.key = key
    # Temps courant
    self.url = "http://api.openweathermap.org/data/2.5/weather?q=Strasbourg,fr" + "&APPID=" + self.key
    # � 5 jours
    self.url = "http://api.openweathermap.org/data/2.5/forecast?q=Strasbourg,fr" + "&APPID=" + self.key
    self.data = None
    
  # Recuperation de la r�ponse
  def load(self):
    print("log : load({})".format(self.url))
    resp = requests.get(self.url)
    
    monJsonUtf = resp.content 
    monJson = monJsonUtf.decode("utf-8") 
 
    self.data = json.loads(monJson)
    print(self.data)
     
  def getSet(self, offset):
    #print("log : Ext�rieur ", self.data['feeds'][0]['field1']) 
    #print("log : Piscine ", self.data['feeds'][0]['field2']) 
    #print("log : Mise � jour ", self.data['feeds'][0]['created_at'])

    return(self.data['feeds'][offset])
    
  def getField(self, offset, field):
    return(self.data['feeds'][offset][field])
    
  
    