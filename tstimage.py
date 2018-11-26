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
s = menuOscar.dateMenu()

canvas = Canvas(root, width=140, height=450, background='black', highlightthickness=1)
photo1 = PhotoImage(file='invert.gif')
photo2 = PhotoImage(file='reduc.gif')

i=1
id_image = canvas.create_image(0,20,anchor=NW, image=photo1)
txt = canvas.create_text(60,10, text=s, font="Arial 12 italic", fill="white")

#r = canvas.create_image(0,20,image=photo)

#canvas.grid(row=0, sticky='e')
offset = larg - 150
canvas.place(x=offset, y=30)

root.title('Mirroir oh mon beau mirroir')
if sys.platform.startswith("darwin"):		# sur mac
	root.geometry("1280x1024+100+80")
else:
	root.attributes("-fullscreen", True)
def clic(t):
	pass
root.bind("<1>", clic)
root.bind("<Escape>", exit)

def changeImage():
    global i, photo1, photo2, canvas, larg, id_image, txt
    if i == 1:
        i=2
        r = canvas.itemconfigure(id_image, image=photo2)
        canvas.itemconfigure(txt, text="la deuxieme")
    else:
        i=1
        r = canvas.itemconfigure(id_image, image=photo1)
        canvas.itemconfigure(txt, text="la premiere")
    offset = larg - 150
    #canvas.place(x=offset, y=30)
    #canvas.pack()
    root.after(10000, changeImage)

root.configure(background="black")

root.after(10000, changeImage)

root.mainloop()

def exit():
	root.quit()