#!/usr/local/bin/python3
#--*-- coding:utf8 --*--

import requests, json, datetime
import locale
locale.setlocale(locale.LC_TIME,'')

class OWM:
    def __init__(self, key):
        # http://api.openweathermap.org/data/2.5/forecast?q=Strasbourg,fr&lang=fr&units=metric&APPID=36e306cb2eda31ad3dec79db153557c2
        self.key = key
        # Temps courant
        self.url = "http://api.openweathermap.org/data/2.5/weather?q=Strasbourg,fr" + "&APPID=" + self.key
        # à 5 jours
        self.url = "http://api.openweathermap.org/data/2.5/forecast?q=Strasbourg,fr&lang=fr&units=metric" + "&APPID=" + self.key
        self.data = None
        self.t = None
        self.moment = {"matin":" 06:00:00", "midi":" 12:00:00", "soir":" 18:00:00", "znuit": " 21:00:00"}
        self.demo = None
        self.ret = None

    def load(self, mode):
        if mode == "demo":
            self.demo = True
            self.loadDemo()
            self.ret = 200
            return(self.ret)
        headers = { 'Accept':'text/html', 'Accept-Encoding': '', 'User-Agent': None } 
        try:
            resp = requests.get(self.url, headers=headers, timeout=10)
            self.ret = resp.status_code
            monJsonUtf = resp.content 
            monJson = monJsonUtf.decode("utf-8") 
    
            self.data = json.loads(monJson)
            return(int(self.data['cod']))
        except:
            self.ret = -1
            return(self.ret)

    def loadDemo(self):
        str = """
            {"cod":"200","message":0.0024,"cnt":40,"list":[{"dt":1538427600,"main":{"temp":8.74,"temp_min":7.65,"temp_max":8.74,"pressure":1006.74,"sea_level":1037.22,"grnd_level":1006.74,"humidity":75,"temp_kf":1.09},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10n"}],"clouds":{"all":12},"wind":{"speed":3.11,"deg":333.003},"rain":{"3h":0.125},"sys":{"pod":"n"},"dt_txt":"2018-10-01 21:00:00"},{"dt":1538438400,"main":{"temp":4.44,"temp_min":3.62,"temp_max":4.44,"pressure":1007.82,"sea_level":1038.57,"grnd_level":1007.82,"humidity":89,"temp_kf":0.82},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.59,"deg":290.51},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-02 00:00:00"},{"dt":1538449200,"main":{"temp":1.66,"temp_min":1.12,"temp_max":1.66,"pressure":1008.29,"sea_level":1039.14,"grnd_level":1008.29,"humidity":90,"temp_kf":0.55},"weather":[{"id":801,"main":"Clouds","description":"peu nuageux","icon":"02n"}],"clouds":{"all":20},"wind":{"speed":1.16,"deg":252.001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-02 03:00:00"},{"dt":1538460000,"main":{"temp":1.79,"temp_min":1.52,"temp_max":1.79,"pressure":1008.58,"sea_level":1039.5,"grnd_level":1008.58,"humidity":90,"temp_kf":0.27},"weather":[{"id":801,"main":"Clouds","description":"peu nuageux","icon":"02d"}],"clouds":{"all":12},"wind":{"speed":1.22,"deg":192.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-02 06:00:00"},{"dt":1538470800,"main":{"temp":9.85,"temp_min":9.85,"temp_max":9.85,"pressure":1009.29,"sea_level":1039.51,"grnd_level":1009.29,"humidity":82,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"peu nuageux","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":1.95,"deg":199.502},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-02 09:00:00"},{"dt":1538481600,"main":{"temp":11.92,"temp_min":11.92,"temp_max":11.92,"pressure":1008.22,"sea_level":1038.22,"grnd_level":1008.22,"humidity":71,"temp_kf":0},"weather":[{"id":802,"main":"Clouds","description":"partiellement nuageux","icon":"03d"}],"clouds":{"all":36},"wind":{"speed":3.57,"deg":235.501},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-02 12:00:00"},{"dt":1538492400,"main":{"temp":12.78,"temp_min":12.78,"temp_max":12.78,"pressure":1007.01,"sea_level":1036.92,"grnd_level":1007.01,"humidity":61,"temp_kf":0},"weather":[{"id":803,"main":"Clouds","description":"nuageux","icon":"04d"}],"clouds":{"all":64},"wind":{"speed":4.4,"deg":246.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-02 15:00:00"},{"dt":1538503200,"main":{"temp":11.22,"temp_min":11.22,"temp_max":11.22,"pressure":1007.27,"sea_level":1037.25,"grnd_level":1007.27,"humidity":67,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":3.56,"deg":242.504},"rain":{"3h":0.05},"sys":{"pod":"n"},"dt_txt":"2018-10-02 18:00:00"},{"dt":1538514000,"main":{"temp":11.14,"temp_min":11.14,"temp_max":11.14,"pressure":1007.58,"sea_level":1037.6,"grnd_level":1007.58,"humidity":75,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":3.72,"deg":224.002},"rain":{"3h":0.13},"sys":{"pod":"n"},"dt_txt":"2018-10-02 21:00:00"},{"dt":1538524800,"main":{"temp":10.68,"temp_min":10.68,"temp_max":10.68,"pressure":1007.3,"sea_level":1037.32,"grnd_level":1007.3,"humidity":85,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":4.23,"deg":208},"rain":{"3h":0.35},"sys":{"pod":"n"},"dt_txt":"2018-10-03 00:00:00"},{"dt":1538535600,"main":{"temp":9.8,"temp_min":9.8,"temp_max":9.8,"pressure":1006.98,"sea_level":1037.02,"grnd_level":1006.98,"humidity":94,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10n"}],"clouds":{"all":92},"wind":{"speed":4.31,"deg":204.002},"rain":{"3h":0.57},"sys":{"pod":"n"},"dt_txt":"2018-10-03 03:00:00"},{"dt":1538546400,"main":{"temp":9.83,"temp_min":9.83,"temp_max":9.83,"pressure":1007.69,"sea_level":1037.92,"grnd_level":1007.69,"humidity":95,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":3.53,"deg":206.507},"rain":{"3h":0.96},"sys":{"pod":"d"},"dt_txt":"2018-10-03 06:00:00"},{"dt":1538557200,"main":{"temp":11.62,"temp_min":11.62,"temp_max":11.62,"pressure":1009.62,"sea_level":1039.56,"grnd_level":1009.62,"humidity":99,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10d"}],"clouds":{"all":92},"wind":{"speed":1.78,"deg":230.504},"rain":{"3h":1.1},"sys":{"pod":"d"},"dt_txt":"2018-10-03 09:00:00"},{"dt":1538568000,"main":{"temp":14.34,"temp_min":14.34,"temp_max":14.34,"pressure":1010.17,"sea_level":1039.99,"grnd_level":1010.17,"humidity":96,"temp_kf":0},"weather":[{"id":500,"main":"Rain","description":"légère pluie","icon":"10d"}],"clouds":{"all":48},"wind":{"speed":1.61,"deg":251.002},"rain":{"3h":0.04},"sys":{"pod":"d"},"dt_txt":"2018-10-03 12:00:00"},{"dt":1538578800,"main":{"temp":15.26,"temp_min":15.26,"temp_max":15.26,"pressure":1010.12,"sea_level":1039.9,"grnd_level":1010.12,"humidity":80,"temp_kf":0},"weather":[{"id":801,"main":"Clouds","description":"peu nuageux","icon":"02d"}],"clouds":{"all":24},"wind":{"speed":1.86,"deg":307.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-03 15:00:00"},{"dt":1538589600,"main":{"temp":10.05,"temp_min":10.05,"temp_max":10.05,"pressure":1010.87,"sea_level":1040.95,"grnd_level":1010.87,"humidity":85,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.17,"deg":339.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-03 18:00:00"},{"dt":1538600400,"main":{"temp":6.17,"temp_min":6.17,"temp_max":6.17,"pressure":1011.67,"sea_level":1042.1,"grnd_level":1011.67,"humidity":85,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.15,"deg":7.50101},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-03 21:00:00"},{"dt":1538611200,"main":{"temp":4.43,"temp_min":4.43,"temp_max":4.43,"pressure":1012.03,"sea_level":1042.7,"grnd_level":1012.03,"humidity":85,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.27,"deg":15.0012},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-04 00:00:00"},{"dt":1538622000,"main":{"temp":3.03,"temp_min":3.03,"temp_max":3.03,"pressure":1011.57,"sea_level":1042.41,"grnd_level":1011.57,"humidity":85,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.17,"deg":14.5001},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-04 03:00:00"},{"dt":1538632800,"main":{"temp":2.21,"temp_min":2.21,"temp_max":2.21,"pressure":1011.44,"sea_level":1042.38,"grnd_level":1011.44,"humidity":83,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.16,"deg":13.504},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-04 06:00:00"},{"dt":1538643600,"main":{"temp":12.08,"temp_min":12.08,"temp_max":12.08,"pressure":1011.92,"sea_level":1042,"grnd_level":1011.92,"humidity":88,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.76,"deg":24},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-04 09:00:00"},{"dt":1538654400,"main":{"temp":16.2,"temp_min":16.2,"temp_max":16.2,"pressure":1010.94,"sea_level":1040.7,"grnd_level":1010.94,"humidity":76,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.23,"deg":49.0027},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-04 12:00:00"},{"dt":1538665200,"main":{"temp":16.97,"temp_min":16.97,"temp_max":16.97,"pressure":1009.68,"sea_level":1039.36,"grnd_level":1009.68,"humidity":65,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.46,"deg":51.0049},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-04 15:00:00"},{"dt":1538676000,"main":{"temp":10.86,"temp_min":10.86,"temp_max":10.86,"pressure":1009.18,"sea_level":1039.23,"grnd_level":1009.18,"humidity":77,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.06,"deg":35.0035},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-04 18:00:00"},{"dt":1538686800,"main":{"temp":6.47,"temp_min":6.47,"temp_max":6.47,"pressure":1008.83,"sea_level":1039.22,"grnd_level":1008.83,"humidity":85,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.62,"deg":37.0031},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-04 21:00:00"},{"dt":1538697600,"main":{"temp":4.02,"temp_min":4.02,"temp_max":4.02,"pressure":1008.01,"sea_level":1038.64,"grnd_level":1008.01,"humidity":83,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.01,"deg":53.5002},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-05 00:00:00"},{"dt":1538708400,"main":{"temp":2.54,"temp_min":2.54,"temp_max":2.54,"pressure":1006.95,"sea_level":1037.72,"grnd_level":1006.95,"humidity":83,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":0.93,"deg":59.0002},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-05 03:00:00"},{"dt":1538719200,"main":{"temp":1.9,"temp_min":1.9,"temp_max":1.9,"pressure":1006.6,"sea_level":1037.23,"grnd_level":1006.6,"humidity":80,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.11,"deg":106.009},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-05 06:00:00"},{"dt":1538730000,"main":{"temp":13.12,"temp_min":13.12,"temp_max":13.12,"pressure":1006.29,"sea_level":1036.12,"grnd_level":1006.29,"humidity":75,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.07,"deg":107.001},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-05 09:00:00"},{"dt":1538740800,"main":{"temp":17.72,"temp_min":17.72,"temp_max":17.72,"pressure":1004.76,"sea_level":1034.15,"grnd_level":1004.76,"humidity":73,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.11,"deg":140.504},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-05 12:00:00"},{"dt":1538751600,"main":{"temp":19.27,"temp_min":19.27,"temp_max":19.27,"pressure":1002.84,"sea_level":1032.34,"grnd_level":1002.84,"humidity":67,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":1.61,"deg":120.5},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-05 15:00:00"},{"dt":1538762400,"main":{"temp":12.42,"temp_min":12.42,"temp_max":12.42,"pressure":1001.99,"sea_level":1031.67,"grnd_level":1001.99,"humidity":89,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.17,"deg":64.503},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-05 18:00:00"},{"dt":1538773200,"main":{"temp":8.42,"temp_min":8.42,"temp_max":8.42,"pressure":1001.56,"sea_level":1031.57,"grnd_level":1001.56,"humidity":82,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.16,"deg":109.503},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-05 21:00:00"},{"dt":1538784000,"main":{"temp":6.94,"temp_min":6.94,"temp_max":6.94,"pressure":1001.04,"sea_level":1031.13,"grnd_level":1001.04,"humidity":80,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.16,"deg":156.004},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-06 00:00:00"},{"dt":1538794800,"main":{"temp":6.51,"temp_min":6.51,"temp_max":6.51,"pressure":1000.32,"sea_level":1030.55,"grnd_level":1000.32,"humidity":79,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":1.94,"deg":157.501},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-06 03:00:00"},{"dt":1538805600,"main":{"temp":7.33,"temp_min":7.33,"temp_max":7.33,"pressure":999.82,"sea_level":1030.03,"grnd_level":999.82,"humidity":81,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.38,"deg":157.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-06 06:00:00"},{"dt":1538816400,"main":{"temp":18.08,"temp_min":18.08,"temp_max":18.08,"pressure":999.54,"sea_level":1029.11,"grnd_level":999.54,"humidity":73,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":2.06,"deg":180.502},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-06 09:00:00"},{"dt":1538827200,"main":{"temp":22.78,"temp_min":22.78,"temp_max":22.78,"pressure":997.92,"sea_level":1027.09,"grnd_level":997.92,"humidity":65,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.06,"deg":198.003},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-06 12:00:00"},{"dt":1538838000,"main":{"temp":22.81,"temp_min":22.81,"temp_max":22.81,"pressure":996.08,"sea_level":1025.32,"grnd_level":996.08,"humidity":60,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01d"}],"clouds":{"all":0},"wind":{"speed":3.17,"deg":192.002},"rain":{},"sys":{"pod":"d"},"dt_txt":"2018-10-06 15:00:00"},{"dt":1538848800,"main":{"temp":16.52,"temp_min":16.52,"temp_max":16.52,"pressure":995.72,"sea_level":1025.16,"grnd_level":995.72,"humidity":65,"temp_kf":0},"weather":[{"id":800,"main":"Clear","description":"ciel dégagé","icon":"01n"}],"clouds":{"all":0},"wind":{"speed":2.97,"deg":180.5},"rain":{},"sys":{"pod":"n"},"dt_txt":"2018-10-06 18:00:00"}],"city":{"id":2973783,"name":"Strasbourg","coord":{"lat":48.5846,"lon":7.7507},"country":"FR","population":15000}}        """
        monJson = str.replace("\'", "\"")
        self.data = json.loads(monJson)
        return(int(self.data['cod']))

    def liste(self):
        if self.ret != 200:
            print("openWeather : erreur de chargement")
            return
        for l in range(self.data['cnt']):
            li = self.data['list'][l]
            print(li['dt_txt'], str(li['main']['temp'])+"°", li['weather'][0]['description'])

    # def jour(self):
    #     jour = "2018-10-00"
    #     d = {}
    #     for l in range(self.data['cnt']):
    #         li = self.data['list'][l]
    #         jour = li['dt_txt'][:10]
    #         if jour in d:
    #             d[jour].append(li['main']['temp'])
    #         else:
    #             d[jour] = [li['main']['temp']]
    #     return d

    def analyse(self):
        if self.ret != 200:
            return
        self.t = {}
        # Recup du temps dans le dico self.t indexe par la date et l'heure
        for l in range(self.data['cnt']):
            li = self.data['list'][l]
            #print(li['main']['temp'])
            self.t[li['dt_txt']] = "{} ({}°)".format(li['weather'][0]['description'],int(round(li['main']['temp'],0)))

    def duJour(self, offset):
        if self.t is None:
            print("None")
            return([])

        dt = datetime.datetime.now()
        dt = dt + datetime.timedelta(offset)
        dts = dt.strftime("%Y-%m-%d")

        if self.demo:
            if offset == 1:
                dts = "2018-10-03"         ####### a supprimer ensuite
            else:
                dts = "2018-10-02"
            print("mode demo : ", dts)
            ret = ["demo"]
        else:
            ret = []
        for periode, heure in self.moment.items():
            moment_heure = dts+heure
        
            if moment_heure in self.t:
                ret.append("{} : {}".format(periode,self.t[moment_heure]))
        return(sorted(ret))
        
    # def temps2J(self):
    #     self.t = {}
    #     dt = datetime.datetime.now()
    #     dt1s = dt.strftime("%Y-%m-%d")
    #     dt2 = dt + datetime.timedelta(1)
    #     dt2s = dt2.strftime("%Y-%m-%d")
    #     print("dates : ", dt1s, dt2s)
    #     for l in range(self.data['cnt']):
    #         li = self.data['list'][l]
    #         dat = datetime.datetime.fromtimestamp(li['dt'])
    #         self.t[li['dt_txt']] = "{} ({}°)".format(li['weather'][0]['description'],li['main']['temp'])
    #         #print(dat, joursem)
    #         #### récupérer le temps du matin , midi et soir
    #         #### ainsi que la pluie possible
    #     today = datetime.datetime.now()
    #     # afficher aujourd'hui et demain
    #     today_txt = today.strftime('%Y-%m-%d')
    #     #for key, value in self.t.items():
    #     #    print(key, value)
    #     ret = []
    #     dt1s = "2018-10-02"         ####### a supprimer ensuite
    #     matin = dt1s + " 06:00:00"
    #     if matin in self.t:
    #         ret.append(self.t[matin])
    #         print(ret)
    #     else:
    #         print(matin, "non trouvé")



