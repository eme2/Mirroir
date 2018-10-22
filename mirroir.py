#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import thing, dateConv, openWeather, menuCantine, cts
import tkinter, time
from tkinter import *
import keys


# Temps initial en secondes
tick = time.time()
print("Tick : ", tick)


# Initialisation des sources
menuPhil = menuCantine.MenuCantine()
tempExt = thing.Thing(keyPiscine,1)
portail = thing.Thing(keyPortail,1)
meteo = openWeather.OWM()
bus = cts.Cts()
dt = dateConv.DateConv()

def majMin():
	print("Màj")
	dtJour.set(dt.nowStr())
	hJour.set(dt.heure())
	print("Màj tempExt")
	tempExt.load()
	print("Màj Retour")
	derMesure =  tempExt.getField(0, "created_at")
	dtIso = dt.dateFromISO(derMesure)
	diff = dt.nowUTC() - dtIso
	extTemp.set("il fait {}° (il y a {} min)".format(float(tempExt.getField(0, "field1")), int(diff.total_seconds())//60))
	piscTemp.set("piscine à {}°".format(float(tempExt.getField(0, "field2"))))
	print("màj Fin")

def maj10min():
	print("Maj menu")
	menuPhil.load()
	print("Maj temp")
	tempExt.load()
	int("Maj portail")
	portail.load()
	print("Maj meteo")
	meteo.load("demo")
	meteo.analyse()
	print("Maj bus")
	bus.load()

root = Tk()
canvas = Canvas(root, width=140, height=400, background='black')
#txt1 = canvas.create_text(75,75, text="Cible", font="Arial 16 italic", fill="blue")
photo = PhotoImage(file="invert.png")
canvas.create_image(0,0,anchor=NW, image=photo)
#canvas.grid(row=0, sticky='e')
canvas.place(x=600, y=0)

# Variables tkinter
dtJour = StringVar()
hJour = StringVar()
extTemp = StringVar()
piscTemp = StringVar()

# Fonction de mise à jour des infos
majMin()
#maj10min()

#import tkFont
font=("Helvetica", 40,"bold")
labelD = Label(root, textvariable=dtJour, fg="white", bg="black", font="Arial 20 bold")
labelD.grid(row=0, sticky='w')
labelH = Label(root, textvariable=hJour, fg="white", bg="black")
labelH.grid(row=1, sticky='w')
labelTE = Label(root, textvariable=extTemp, fg="white", bg="black")
labelTE.grid(row=2)
labelTP = Label(root, textvariable=piscTemp, fg="white", bg="black")
labelTP.grid(row=3)

root.title('Mirroir oh mon beau mirroir')
root.attributes("-fullscreen", True)
def clic(t):
	pass
root.bind("<1>", clic)
root.bind("<Escape>", exit)

root.configure(background="black")
#fnt = Font(family="Helvetica", size=128, weight='bold')
#Label(root, text="22 °C")

def readsensor():
	global tick
	print("dans readsensor, tick : ", tick)
	if time.time() - 600 > tick:
		tick = time.time()
		maj10min()
	majMin()
	root.after(60000, readsensor)		# une minute

root.after(2000, readsensor)

root.mainloop()

	
def exit():
	root.quit()

