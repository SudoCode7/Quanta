from py5paisa.order import Order, OrderType, Exchange
import yfinance as yf
import Many_In_one as indi
from pandas_datareader import data as pdr
import pandas as pd
from py5paisa import FivePaisaClient
import time
from py5paisa.order import OrderForStatus, Exchange, RequestList

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

ticker = 'ICICIBANK'#(input("Enter a stock ticker symbol: ")).strip()
script_code = 539437#int(input("Enter the stock script code: "))#  scode[1].strip()
ticker = ticker.upper()+".BO"
print(ticker+'  '+str(script_code))
ticker = yf.Ticker(ticker)

client = FivePaisaClient(email="")
client.login()

# get historical market data and intitialize same index to signal
signal = pd.DataFrame()
df = ticker.history(period="400d")
df = pd.concat([df, signal], axis=1)
#print(df)

#get necessary date
# signal = indi.MACD(df)
# signal = indi.RSI(df)
# signal = indi.BBand(df)
signal = indi.SuperTrend(df,12,3)
signal = indi.SuperTrend(df,10,1)
signal = indi.SuperTrend(df,11,2)
signal = indi.SuperTrend(df,10,3)
# signal = indi.HA(df)
signal = indi.EMA(df,'Close','ema_200',200)
#print(df.tail(50))

#staregy one
# close_price = df['Close'][-1]
# if df['STX_12_3'][-1]==df['STX_10_1'][-1]==df['STX_11_2'][-1]=='sell':
#     test_order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1, price=close_price,
#                        atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
#     client.place_order(test_order)
#     print('sell')
#
# elif df['STX_12_3'][-1]==df['STX_10_1'][-1]==df['STX_11_2'][-1]=='buy':
#     test_order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1, price=close_price,
#                        atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
#     client.place_order(test_order)
#     print('buy')
#
# else :
#     print('holding')

#srategy 2
close_price = df['Close'][-1]
if close_price > df['ema_200'][-1] and df['STX_10_3'][-1]=='sell':
    test_order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1, price=close_price,
                       atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    client.place_order(test_order)
    print('sell')

elif df['STX_10_3'][-1]=='buy' and close_price < df['ema_200'][-1]:
    test_order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1, price=close_price,
                       atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    client.place_order(test_order)
    print('buy')

else :
    print('holding')


info = client.positions()
ticker_name1 = info[0]['ScripName']
Script_Code1 = info[0]['ScripCode']
BuyQuantity1 = info[0]['BuyQty']
LTP1 = info[0]['LTP']
#print(info[0][''NetQty'']

# test_order_status = OrderForStatus(exchange=Exchange.BSE, exchange_type=ExchangeType.CASH, scrip_code=script_code, order_id=0)
#
# req_list = RequestList()
# # Add multiple orders to the RequestList to know status of multiple orders at once.
# req_list.add_order(test_order_status)
#
# # Fetches the trade details
# client.fetch_trade_info(req_list)
#
# # Fetches the order status
# client.fetch_order_status(req_list)
