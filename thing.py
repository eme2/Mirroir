#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import requests
import json

# Gestion des donnees du site thingspeak
class Thing:
  def __init__(self, channel, nb=1):
    
    self.url = "https://api.thingspeak.com/channels/{}/feeds.json?results={}".format(channel, nb)
    self.data = None
    self.ret = None
    
  # Recuperation de la r�ponse
  def load(self):
    #print("log : load()")
    headers = { 'Accept':'text/html', 'Accept-Encoding': '', 'User-Agent': None } 
    try:
        resp = requests.get(self.url, headers= headers, timeout=10)
    except:
        self.ret = resp.status_code
        return
    self.ret = resp.status_code
    monJsonUtf = resp.content 
    monJson = monJsonUtf.decode("utf-8") 
 
    self.data = json.loads(monJson)

  def getDesc(self):
    if self.ret == 200:
      return(self.data['channel'])  
    else:
      return("")

  def getSet(self, offset):
    if self.ret == 200:
      return(self.data['feeds'][offset])
    else:
      return({})
    
  def getField(self, offset, field):
    if self.ret == 200:
      return(self.data['feeds'][offset][field])
    else:
      return("")
    
  
    