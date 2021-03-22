from py5paisa import FivePaisaClient
import pandas as pd
import datetime
from datetime import date
from py5paisa.order import Order, OrderType, AHPlaced
import time

client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
client.login()

try:
    client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
    client.login()
except TypeError:
    client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
    client.login()
except:
    print("Something ha gone wrong")