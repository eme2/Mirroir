# -*- coding: utf-8 -*-

import datetime
import pytz
import re

isoformat = '%Y-%m-%dT%H:%M:%S %Z'
local_tz = pytz.timezone('Europe/Paris')

dt = datetime.datetime.now()

print("Now : ", dt)

local_tz = pytz.timezone('Europe/Paris')
dtl = dt.replace(tzinfo=local_tz)
print("Localisee : ",dtl)