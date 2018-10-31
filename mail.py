#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime, os


import thing, dateConv, openWeather, menuCantine, cts
import time, sys
from keys import *

def sendMail(frm, to, msg, title):
    sendmail_location = "/usr/sbin/sendmail" # sendmail location
    p = os.popen("%s -t" % sendmail_location, "w")
    p.write("From: %s\n" % frm)
    p.write("To: %s\n" % to)
    p.write("Subject: %s\n" % title)
    p.write("\n") # blank line separating headers from body
    p.write(msg)
    p.write("...")    
    status = p.close()
    if status != 0:
           print("Sendmail exit status", status)

def addMsg(s):
  global msg
  msg = msg + s + "\n"


msg = ""
deb = time.time()
menuPhil = menuCantine.MenuCantine()
menuPhil.load()

tempExt = thing.Thing(keyPiscine,1)
portail = thing.Thing(keyPortail,1)
tempExt.load()
portail.load()
m = openWeather.OWM(meteoKey)
m.load("real")    # pas en mode demo
m.analyse()
dt = dateConv.DateConv()

bus = cts.Cts(idCts, pwdCts, arretCts)
bus.load()

addMsg(dt.nowStr())
addMsg(dt.heure())

derMesure =  tempExt.getField(0, "created_at")
dtIso = dt.dateFromISO(derMesure)
diff = dt.nowUTC() - dtIso
addMsg("il fait {}Â° (il y a {} min)".format(float(tempExt.getField(0, "field1")), int(diff.total_seconds())//60))
addMsg("piscine Ã  {}Â°".format(float(tempExt.getField(0, "field2"))))
addMsg("------------------")
addMsg("\nAUJOURD'HUI")
addMsg('\n'.join(m.duJour(0)))
addMsg("\nDEMAIN")
addMsg('\n'.join(m.duJour(1)))
addMsg("------------------")
for li in menuPhil.lstMenu():
    addMsg(li)
addMsg("------------------")
#print("##############################################")
#print(msg)
#print("##############################################")

sendMail(keyFrom, keyTo, msg, "Infos du jour") 
