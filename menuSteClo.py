import requests
import dateConv, datetime
from io import open as iopen
from PIL import Image
from PIL import ImageFile
import PIL.ImageOps

class MenuSteClo:
    def __init__(self):
        self.sem = "45"
        self.jourSem = 0
        self.ret = -1
        self.resp = None
        self.jours = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
        
    def load(self):
        dt = dateConv.DateConv()
        self.jourSem = dt.jourSem()
        print("Jour de la semaine : ", self.jourSem)
        if self.jourSem > 5:         # le WE on affiche le menu du lundi
            self.sem = str(dt.numSem()+1)
            self.jourSem = 1
        else:
            d = datetime.datetime.now()
            if d.hour > 12:
                self.jourSem += 1
            self.sem = str(dt.numSem())

        self.sem= "0"+self.sem
        self.sem = self.sem[-2:]
        url = "http://www.macantineetmoi.com/images/menu/sainte-clotilde/sainte-clotilde_S"+self.sem+".jpg"
        file_name = "menu.jpg"
        print("Recuperation de ", url)
        headers = { 'Accept':'text/html', 'Accept-Encoding': '', 'User-Agent': None } 
        try:
            self.resp = requests.get(url, headers= headers, timeout=10)
        except:
            self.ret = -1
            return
        self.ret = self.resp.status_code
        print("Apres requests ", self.ret)
        j=0
        if self.ret == requests.codes.ok:
            with iopen(file_name, 'wb') as file:
                for chunk in self.resp.iter_content(1024):
                    #print("> ", j)
                    j = j+1
                    file.write(chunk)
                file.close()
        print("Terminé ")

    def lstMenu(self):
        pass

    def dateMenu(self):
        return "{} semaine {}".format(self.jours[self.jourSem - 1], self.sem)

    def crop(self):
        ImageFile.LOAD_TRUNCATED_IMAGES = True

        im = Image.open("menu.jpg")
        im_size = im.size

        print("Size : ", im_size)

        left = 40
        top = 275
        width = 200
        height = 560
        hmarge = 30

        print("Recup du jour : ", self.jourSem)
        coin = left + (self.jourSem - 1)*(width+hmarge)
        box = (coin, top, coin+width, top+height)
        area = im.crop(box)

        area.save("jour.gif", "GIF")
        reduc = area.resize((140,400), Image.ANTIALIAS)
        inv = PIL.ImageOps.invert(reduc)
        reduc.save("reduc.gif", "GIF")
        inv.save("invert.gif", "GIF")

