# -*- coding: utf-8 -*-

import datetime
import pytz
import re
# pour avoir la date en français
import locale
locale.setlocale(locale.LC_TIME,'')

class DateConv:
  def __init__(self):
    self.isoformat = '%Y-%m-%dT%H:%M:%S %Z'
    self.local_tz = pytz.timezone('Europe/Paris')
    return
    
  def now(self):
    return datetime.datetime.now()

  def nowStr(self):
    return(datetime.datetime.now().strftime("%A le %e %B %G"))

  def numSem(self):
    d = datetime.datetime.now()
    dd = d.isocalendar()
    return(dd[1])

  def jourSem(self):
    d = datetime.datetime.now()
    dd = d.isocalendar()
    return(dd[2])

  def dateJourApi(self):
    d = datetime.datetime.now()

    j = self.jourSem()

    if j > 5:    # afficher menu du lundi
      offset = 1 - j + 7
    elif d.hour > 12:
      offset = 1
    else:
      offset = 0
    
    d = d + datetime.timedelta(offset)
    return(d.strftime("%d-%m-%Y"))
    
  def heure(self):
    dt = datetime.datetime.now()
    ds = dt.strftime("%H:%M")
    return ds

  def nowLocalized(self):
    dt = datetime.datetime.now()
    return dt.replace(tzinfo=self.local_tz)

  def nowLocalizedTZ(self):
    dt = datetime.datetime.now()
    dt2 = dt.replace(tzinfo=self.local_tz)
    return dt2.astimezone(tz=self.local_tz)

  def nowUTC(self):
    return datetime.datetime.utcnow()
    
  def dateFromISO(self, dt):
    # remplacemnet du suffixe en UTC
    dtUTC = re.sub("(.*)Z$",r"\1 UTC", dt)
    return datetime.datetime.strptime(dtUTC, self.isoformat)
     
  def convLocal(self, dt):
    return dt.replace(tzinfo=pytz.utc)
