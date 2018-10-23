#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import thing, dateConv, openWeather, menuCantine, cts
import time
from keys import *

deb = time.time()
menuPhil = menuCantine.MenuCantine()
menuPhil.load()

tempExt = thing.Thing(keyPiscine,1)
portail = thing.Thing(keyPortail,1)
tempExt.load()
portail.load()
m = openWeather.OWM(meteoKey)
m.load("demo")
m.analyse()
dt = dateConv.DateConv()

bus = cts.Cts(idCts, pwdCts, arretCts)
bus.load()

print("------------------")


print(dt.nowStr())
print(dt.heure())

derMesure =  tempExt.getField(0, "created_at")
dtIso = dt.dateFromISO(derMesure)
diff = dt.nowUTC() - dtIso
print("il fait {}° (il y a {} min)".format(float(tempExt.getField(0, "field1")), int(diff.total_seconds())//60))
print("piscine à {}°".format(float(tempExt.getField(0, "field2"))))
print("------------------")
print("\nAUJOURD'HUI")
print('\n'.join(m.duJour(0)))
print("\nDEMAIN")
print('\n'.join(m.duJour(1)))
print("------------------")
for li in menuPhil.lstMenu():
    print(li)
print("------------------")

print('\n'.join(bus.horaires()))

print("------------------")


print("Courrier :", portail.getField(0, "field5"))
print("Contact :", portail.getField(0, "field1"))
print("Ouverture :", portail.getField(0, "field2"))
print("TempPortail :", portail.getField(0,"field3"))
portailUpdate = portail.getField(0, "created_at")
derMesure =  tempExt.getField(0, "created_at")
print("le : ", derMesure)

dtIso = dt.dateFromISO(derMesure)

diff = dt.nowUTC() - dtIso
diffPortail = dt.nowUTC() - dt.dateFromISO(portailUpdate)
print("derniere mesure il y a (min) : ", int(diff.total_seconds())//60)
print("Update Portail (min) : ", int(diffPortail.total_seconds())//60 )




print("retour ", m.loadDemo())
d = m.jour()

print(type(d))
print("Terminé en ", time.time() - deb)
exit()
for cle, valeur in d.items():
    print(cle, round(min(valeur),1), round(max(valeur),1))


#m.temps()