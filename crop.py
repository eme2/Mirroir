# -*- coding: utf-8 -*-
#
from PIL import Image
from PIL import ImageFile
import PIL.ImageOps

ImageFile.LOAD_TRUNCATED_IMAGES = True

im = Image.open("menu.jpg")
im_size = im.size

print("Size : ", im_size)

left = 40
top = 275
width = 200
height = 560
hmarge = 30

jour = 5
coin = left + (jour - 1)*(width+hmarge)
box = (coin, top, coin+width, top+height)
print("box : ", box)
area = im.crop(box)

print("crop : ", area.size)


area.save("jour.gif", "GIF")
reduc = area.resize((140,400), Image.ANTIALIAS)
inv = PIL.ImageOps.invert(reduc)
print("resize ", reduc.size)
reduc.save("reduc.gif", "GIF")
inv.save("invert.gif", "GIF")
