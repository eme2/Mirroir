#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests
import json

# Gestion des donnees du site thingspeak
class Thing:
  def __init__(self, channel, nb=1):
    self.url = "https://api.thingspeak.com/channels/{}/feeds.json?results={}".format(channel, nb)
    self.data = None
    
  # Recuperation de la r�ponse
  def load(self):
    #print("log : load()")
    try:
        resp = requests.get(self.url, timeout=10)
    except:
        return
    monJsonUtf = resp.content 
    monJson = monJsonUtf.decode("utf-8") 
 
    self.data = json.loads(monJson)

  def getDesc(self):
    return(self.data['channel'])  

  def getSet(self, offset):
    return(self.data['feeds'][offset])
    
  def getField(self, offset, field):
    return(self.data['feeds'][offset][field])
    
  
    