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

# now = dt.datetime.now()
# d = dt.timedelta(days = 300)
# start = now - d
# df = pdr.get_data_yahoo(ticker, start, now)

ticker = yf.Ticker(ticker)
df = ticker.history(period="300d")
df = df.sort_index()
print(df)

client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
client.login()

# # Fetches holdings
# client.holdings()
#
# # Fetches the order book of the client
# client.order_book()
# data = yf.download(ticker,start,now)
# print(data)

signal = pd.DataFrame(index=df.index)
signal = indi.MACD(df)
# df = pd.merge(df,signal)#df.append(signal)
df = pd.concat([df, signal], axis=1)
signal = indi.RSI(df)
signal = indi.BBand(df)
signal = indi.SuperTrend(df,10,7)
signal = indi.HA(df)
signal = indi.EMA(df,'Close','ema_200',200)
#print(signal)
#df = pd.concat([df, signal], axis=1)
close_price = df['Close'][-1]
if df['signalMACD'][-1]=='sell':
    test_order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1, price=close_price,
                       atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    client.place_order(test_order)
    print('sell')

elif df['signalMACD'][-1]=='buy':
    test_order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1, price=close_price,
                       atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    client.place_order(test_order)
    print('buy')

# else :
#     continue
    # test_order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1, price=close_price,
    #                    atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    # client.place_order(test_order)

print(df)


