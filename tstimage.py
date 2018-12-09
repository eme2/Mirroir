#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import dateConv, menuSteClo
import tkinter, time, sys
from tkinter import *
from keys import *

i = 1

root = Tk()
#larg = root.winfo_screenwidth()
#haut = root.winfo_screenheight()
larg = 1280		# Dimensions de l'écran 19''
haut = 1024

#----------test 
menuOscar = menuSteClo.MenuSteClo() 
menuOscar.load()
s = menuOscar.dateMenu()            #

canvas = Canvas(root, width=140, height=450, background='black', highlightthickness=1)
canvas2 = Canvas(root, width=220, height=60, background='black', highlightthickness=0)
photo1 = PhotoImage(file='invert.gif')
photo2 = PhotoImage(file='mail.gif')
ouvert = PhotoImage(file='ouvert.gif')
ferme = PhotoImage(file='ferme.gif')


i=1
id_image = canvas.create_image(0,20,anchor=NW, image=photo1)
txt = canvas.create_text(60,10, text=s, font="Arial 12 italic", fill="white")

canvas2.create_image(0,0, anchor=NW, image=photo2)
canvas2.create_image(140,0, anchor=NW, image=ouvert)


#r = canvas.create_image(0,20,image=photo)

#canvas.grid(row=0, sticky='e')
offset = larg - 150
canvas.place(x=offset, y=30)
canvas2.place(x=500, y=700)

root.title('Mirroir oh mon beau mirroir')
if sys.platform.startswith("darwin"):		# sur mac
	root.geometry("1280x1024+100+80")
else:
	root.attributes("-fullscreen", True)
def clic(t):
	pass

def callback(t):
    global canvas, id_image
    print("Callback !!")
    img2 = PhotoImage(file="reduc.gif")
    canvas.itemconfigure(id_image, image=img2)
    #canvas.configure(image=img2)
    canvas.image = img2
root.bind("<1>", clic)
root.bind("<Return>", callback)
root.bind("<Escape>", exit)

def changeImage():
    global i, photo1, photo2, canvas, larg, id_image, txt
    if i == 1:
        photo_2 = PhotoImage(file='noImage.gif')
        r = canvas.itemconfigure(id_image, image=photo2)
        canvas.itemconfigure(txt, text="la deuxieme")
    elif i == 2:
        r = canvas.itemconfigure(id_image, image=photo1)
        canvas.itemconfigure(txt, text="la premiere")
    elif i == 3:
        r = canvas.itemconfigure(id_image, image=ouvert)
        canvas.itemconfigure(txt, text="Ouvert")
    else:
        r = canvas.itemconfigure(id_image, image=ferme)
        canvas.itemconfigure(txt, text="Fermé")
        i = 0
    i+=1

    offset = larg - 150
    #canvas.place(x=offset, y=30)
    #canvas.pack()
    root.after(5000, changeImage)

root.configure(background="black")

root.after(10000, changeImage)

root.mainloop()

def exit():
	root.quit()