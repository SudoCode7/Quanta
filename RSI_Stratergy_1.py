import yfinance as yf
import Many_In_one as indi
from pandas_datareader import data as pdr
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

ticker = 'ICICIBANK' #(input("Enter a stock ticker symbol: ")).strip()
script_code = 532174 #int(input("Enter the stock script code: "))#  scode[1].strip()
quantity = 1 #int(input("Enter the no. of quantity to be bought: "))
ticker = ticker.upper()+".BO"
print(ticker+'  '+str(script_code))
ticker = yf.Ticker(ticker)

# get historical market data and intitialize same index to signal
df = ticker.history(period="400d")
signal = pd.DataFrame(index=df.index)
df = pd.concat([df, signal], axis=1)

#get necessary date
signal = indi.SuperTrend(df,12,3)
signal = indi.SuperTrend(df,10,1)
signal = indi.SuperTrend(df,11,2)
signal = indi.EMA(df,'Close','ema_200',200)
print(df.tail(3))

#staregy one
import Order_placement
close_price = df['Close'][-1]
if df['STX_12_3'][-1]==df['STX_10_1'][-1]==df['STX_11_2'][-1]=='sell':
    Order_placement.sell(script_code,close_price, quantity=quantity)
    print('\n'+'sell')

elif df['STX_12_3'][-1]==df['STX_10_1'][-1]==df['STX_11_2'][-1]=='buy':
    Order_placement.sell(script_code, close_price, quantity=quantity)
    print('\n'+'buy')

else :
    print('\n'+'hold')

