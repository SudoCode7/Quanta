from py5paisa import FivePaisaClient
import pandas as pd
import datetime
from datetime import date
from py5paisa.order import Order, OrderType, AHPlaced
import time
from datetime import date
from py5paisa.order import Order, OrderType, AHPlaced

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
now = current_time.split(':')
hr = int(now[0])
min=int(now[1])


client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
client.login()
tic='IDFCFIRSTB'

#print(client.positions())
if (9<= hr <= 15) or (hr == 15 and min <= 25):
    CheckTime = 'now'

else:
    CheckTime = 'later'

execution = client.positions()
length = len(execution)
trueLen = len(execution)
if length==0:
    length=1

boolean = True
while boolean == True:
    for i in range(length):
        if trueLen==1:
            if execution[i]['Symbol'] == tic:
                boolean = False
                break

        else:
            if CheckTime == 'now':
                time.sleep(60)

            elif CheckTime == 'later':
                if hr > 15:
                    diff = (24 - hr) + 9

                else:
                    diff = 9 - hr
                time.sleep((diff*60)+(60*15))

