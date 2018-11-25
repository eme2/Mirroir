#!/usr/bin/env python 
# -*- coding: utf-8 -*-

# TODO
# ajouter la date du menu SteClo, l'indcateur mail et portail.
# 25/11 : pb d'affichage du menu steClo : comment modifier l'image ?
# 	elle n'est pas prise en compte dans la fonction... manque un pack ?

import thing, dateConv, openWeather, menuCantine, cts, menuSteClo
import tkinter, time, sys
from tkinter import *
from keys import *


# Temps initial en secondes
tick = time.time()
tick10 = tick
tick6h = tick

if len(sys.argv) > 1:
	mode = "prod"
else:
	mode = "demo"
print("Mode : ", mode)
# Initialisation des sources
menuPhil = menuCantine.MenuCantine()
menuOscar = menuSteClo.MenuSteClo()
tempExt = thing.Thing(keyPiscine,1)
portail = thing.Thing(keyPortail,1)
meteo = openWeather.OWM(meteoKey)
bus = cts.Cts(idCts, pwdCts, arretCts)
dt = dateConv.DateConv()



root = Tk()
#larg = root.winfo_screenwidth()
#haut = root.winfo_screenheight()
larg = 1280		# Dimensions de l'écran 19''
haut = 1024

#----------test 
menuOscar.load()
#s = menuOscar.dateMenu()
canvas = Canvas(root, width=140, height=450, background='black', highlightthickness=1)
photo = PhotoImage(file='invert.gif')
print(photo)
r = canvas.create_image(0,20,anchor=NW, image=photo)
#r = canvas.create_image(0,20,image=photo)
print("retour : ", r)
#canvas.grid(row=0, sticky='e')
offset = larg - 150
canvas.place(x=offset, y=30)
#print("Menu Oscar : ", s)
#dtMenu.set(menuOscar.dateMenu())
#menuOscar.crop()
time.sleep(3)
#----------test 

# Variables tkinter
dtJour = StringVar()
hJour = StringVar()
extTemp = StringVar()
piscTemp = StringVar()
sMeteoAuj = StringVar()
sMeteoDem = StringVar()
dtMenu = StringVar()




#import tkFont
myRow = 0
font=("Helvetica", 40,"bold")
labelD = Label(root, textvariable=dtJour, fg="white", bg="black", font="Arial 20 bold")
labelD.grid(row=myRow, sticky='w')

labelMo = Label(root, textvariable=dtMenu, fg="white", bg="black")
#labelMo.grid(row=myRow, column=1, sticky='e')
labelMo.grid(row=myRow,  sticky='w')


myRow += 1
labelH = Label(root, textvariable=hJour, fg="white", bg="black")
labelH.grid(row=myRow, sticky='w')
myRow += 1
labelTE = Label(root, textvariable=extTemp, fg="white", bg="black")
labelTE.grid(row=myRow, sticky='w')
myRow += 1
labelTP = Label(root, textvariable=piscTemp, fg="white", bg="black")
labelTP.grid(row=myRow, sticky='w')
myRow += 1
labelA = Label(root, text="Météo du jour", fg="white", bg="black", font="Arial 14")
labelA.grid(row=myRow, pady=20, sticky='w')
myRow += 1
textMetAuj = Text(root, fg="white", bg="black", height=4, borderwidth=0, highlightthickness=0)
textMetAuj.grid(row=myRow, sticky='w')
myRow += 1
labelA = Label(root, text="Demain", fg="white", bg="black")
labelA.grid(row=myRow, sticky='w')
myRow += 1
textMetDem = Text(root, fg="white", bg="black", height=4, bd=0, highlightthickness=0)
textMetDem.grid(row=myRow, sticky='w')
myRow += 2
labelM = Label(root, text="Menu Phil", fg="white", bg="black", font="Arial 14")
labelM.grid(row=myRow, pady=20, sticky='w')
myRow += 1
textApi = Text(root, fg="white", bg="black", height=6, borderwidth=0, highlightthickness=0)
textApi.grid(row=myRow, sticky='w')
myRow += 1
labelB = Label(root, text="Bus", fg="white", bg="black", font="Arial 14")
labelB.grid(row=myRow, pady=20, sticky='w')
myRow += 1
textBus = Text(root, fg="white", bg="black", height=10, bd=0, highlightthickness=0)
textBus.grid(row=myRow, sticky='w')

# Fonctions de mise à jour des infos
def majMin():
	dtJour.set(dt.nowStr())
	hJour.set(dt.heure())
	tempExt.load()
	derMesure =  tempExt.getField(0, "created_at")
	if derMesure != -1:
		dtIso = dt.dateFromISO(derMesure)
		diff = dt.nowUTC() - dtIso
		extTemp.set("il fait {}° (il y a {} min)".format(float(tempExt.getField(0, "field2")), int(diff.total_seconds())//60))
		piscTemp.set("cabane à {}°".format(float(tempExt.getField(0, "field1"))))
	else:
		diff = -1
		extTemp.set("Pb de lecture de la température")
		piscTemp.set("------")
	
	bus.load()
	textBus.delete(1.0, 7.40)
	textBus.insert(1.0, '\n'.join(bus.horaires()))

def maj10min():
	global textMetAuj, textMetDem, mode
	menuPhil.load()
	meteo.load(mode)
	meteo.analyse()
	textMetAuj.delete(1.0, 5.0)
	textMetAuj.insert(1.0, '\n'.join(meteo.duJour(0)))
	textMetDem.delete(1.0, 5.0)
	textMetDem.insert(1.0, '\n'.join(meteo.duJour(1)))
	textApi.delete(1.0, 6.20)
	textApi.insert(1.0, '\n'.join(menuPhil.lstMenu()))
	
def maj6h():
	global root, larg, dtMenu, canvas
	#menuOscar.load()
	s = menuOscar.dateMenu()
	#menuOscar.crop()
	# highlightthinkness=0 pour éviter la bordure
	txt1 = canvas.create_text(60,10, text=s, font="Arial 12 italic", fill="white")
	photo = PhotoImage(file='jour.gif')
	print(photo)
#	r = canvas.create_image(0,20,anchor=NW, image=photo)
	r = canvas.create_image(0,20,image=photo)
	print("retour : ", r)
	#canvas.grid(row=0, sticky='e')
	offset = larg - 150
	canvas.place(x=offset, y=30)

# Fonction de mise à jour des infos
majMin()
maj10min()
maj6h()


root.title('Mirroir oh mon beau mirroir')
if sys.platform.startswith("darwin"):		# sur mac
	root.geometry("1280x1024+100+80")
else:
	root.attributes("-fullscreen", True)
def clic(t):
	pass
root.bind("<1>", clic)
root.bind("<Escape>", exit)

root.configure(background="black")
#fnt = Font(family="Helvetica", size=128, weight='bold')
#Label(root, text="22 °C")

def readsensor():
	global tick10, tick6h				# un tick par seconde
	tick = time.time()
	if tick - 36000 > tick6h:
		tick6h = tick
	if tick - 600 > tick10:
		tick10 = tick
		maj10min()
	majMin()

	root.after(60000, readsensor)		# une minute

root.after(2000, readsensor)

root.mainloop()

	
def exit():
	root.quit()

