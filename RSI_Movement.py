import Many_In_one as indi
from py5paisa import FivePaisaClient
import time
from matplotlib import pyplot as plt
import yfinance as yf
import datetime as dt
from py5paisa.order import Order, OrderType, Exchange#, ExchangeType
from pandas_datareader import data as pdr
import pandas as pd
import Get_ScriptCode as sc
import time
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

pd.options.display.max_rows
ticker = 'idfcfirstb'#(input("Enter a stock ticker symbol: ")).strip()
# scode = sc.code(ticker)
# scode = scode.split('|')
script_code = 539437#int(input("Enter the stock script code: "))#  scode[1].strip()
ticker = ticker.upper()+".BO"
#print(scode[0][1:]+"  "+script_code)
print(ticker+'  '+str(script_code))

# startyear = 2019
# startmonth = 1
# startday = 1
# start = dt.datetime(startyear, startmonth, startday)

now = dt.datetime.now()
d = dt.timedelta(days = 300)
start = now - d
df = pdr.get_data_yahoo(ticker, start, now)
#print(df)
df = df.sort_index()

client = FivePaisaClient(email="")
client.login()

signal_EMA_200 = indi.EMA(df,'Close','ema_200',200)


