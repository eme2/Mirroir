#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

#sudo apt-get install python-lxml
import xml.etree.ElementTree as ET
import dateConv

import re, datetime

class Cts:
    def __init__(self, id, pwd, arret):
        self.url = "http://opendata.cts-strasbourg.fr/webservice_v4/Service.asmx"
        self.dt = dateConv.DateConv()
        # xpath : //*[@id="bi-bloc-08TCR4BC0001"]/div[2]/header/div[1]/div/h2
        self.headers = {'content-type': 'text/xml'}
        self.body1 ="""<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:cts="http://www.cts-strasbourg.fr/">
            <soap:Header>
                <cts:CredentialHeader>
                    <!--Optional:-->
                    <cts:ID>"""
        + id + """</cts:ID>
                    <!--Optional:-->
                    <cts:MDP>"""
        + pwd + """</cts:MDP>
                </cts:CredentialHeader>
            </soap:Header>
            <soap:Body>
                <cts:rechercheProchainesArriveesWeb>
                    <!--Optional:-->
                    <cts:CodeArret>"""
        + arret + """</cts:CodeArret>
                    <cts:Mode>2</cts:Mode>
                    <!--Optional:-->
                    <cts:Heure>"""
        self.body2 = """</cts:Heure>
                <cts:NbHoraires>3</cts:NbHoraires>
            </cts:rechercheProchainesArriveesWeb>
        </soap:Body>
        </soap:Envelope>""" 
        self.tree = None

    def load(self):
        print("Horaires de ", self.dt.heure())
        body = self.body1 + str(self.dt.heure()) + self.body2
        response = requests.post(self.url,data=body,headers=self.headers)
        monXml = str(response.content)
        deb = monXml.find("<ListeArrivee>")
        fin = monXml.find("</ListeArrivee>")
        coeurXml = monXml[deb:fin+15]

        self.tree = ET.fromstring(coeurXml)
        #print(etree.tostring(etree.getroot()))
        #tree.xpath("/ListeArrivee/Arrivee[Destination='L6 Pont phario']"))
        #print(tree.xpath("/ListeArrivee/Arrivee[Destination='L6 Pont phario']"))
        #arrivees = tree.getroot()

    def horaires(self):
        ret = []
        for node in self.tree.findall("Arrivee"):
            h = node.find("Horaire").text
            jour = datetime.datetime.now().strftime("%d-%m-%Y ")
            d = datetime.datetime.strptime(jour+h, "%d-%m-%Y %H:%M:%S")
            d_now = datetime.datetime.now()
            delta = d - d_now
            ret.append("Destination {} {} ({} min)".format(node.find("Destination").text, node.find("Horaire").text, delta.seconds // 60))
            
        return(sorted(ret))
