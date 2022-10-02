import countdown
from easygui import *

msg = "Fill in the amount of days your counter needs to have"
title = "Days"
fieldNames = ["Days"]
fieldValues = int()
fieldValues = multenterbox(msg,title, fieldNames)
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(fieldValues)
days = ""
for m in fieldValues:
    if m.isdigit():
        days = days + m
days = int(days)
msg = "Fill in the amount of hours your counter needs to have"
title = "Hours"
fieldNames = ["Hours"]
fieldValues = int()
fieldValues = multenterbox(msg,title, fieldNames)
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break
    fieldValues = multenterbox(fieldValues)
hours = ""
for m in fieldValues:
    if m.isdigit():
        hours = hours + m
hours = int(hours)
msg = "Fill in the amount of minutes your counter needs to have"
title = "minutes"
fieldNames = ["minutes"]
fieldValues = int()
fieldValues = multenterbox(msg,title, fieldNames)
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break
    fieldValues = multenterbox(fieldValues)
minutes = ""
for m in fieldValues:
    if m.isdigit():
        minutes = minutes + m
minutes = int(minutes)
msg = "Fill in the amount of seconds your counter needs to have"
title = "seconds"
fieldNames = ["seconds"]
fieldValues = int()
fieldValues = multenterbox(msg,title, fieldNames)
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break
    fieldValues = multenterbox(fieldValues)
seconds = ""
for m in fieldValues:
    if m.isdigit():
        seconds = seconds + m
seconds = int(seconds)
countdown.countdown(days, hours, minutes, seconds)