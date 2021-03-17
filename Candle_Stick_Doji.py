'''
close3 and similar variables indicate left candle
close2 and similar variables indicate middle candle
close1 and similar variables indicate right candle

***Remember we are only taking last 3 candles into consideration

Lowest_found and Highest_found are to check for 25 days lowest and highest

Try to code your logic after line 83 and print the  signal in the last
'''
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

yf.pdr_override()

stock = 'itc' #input("Enter a stock ticker symbol: ")+'.NS'
stock = stock+".NS"
print(stock)

now = dt.datetime.now()

d = dt.timedelta(days = 5)
start = now - d

df = pdr.get_data_yahoo(stock, start, now)
length = len(df)
close2 = df['Close'][length-2]
open2 = df['Open'][length-2]
high2 = df['High'][length-2]
low2 = df['Low'][length-2]

close3 = df['Close'][length-3]
open3 = df['Open'][length-3]
high3 = df['High'][length-3]
low3 = df['Low'][length-3]

close1 = df['Close'][length-1]
open1 = df['Open'][length-1]
high1 = df['High'][length-1]
low1 = df['Low'][length-1]
Signal = ''
StopLoss = 0.0

Lowest_found= False
Highest_found= False
historical_low = round(df['Low'][-26:length],1)
historical_High = df['High'][-26:length]
check_Low = round(df['Low'][length-2],1)
check_High = round(df['High'][length-2],1)
temp1 = temp = 0

for i in historical_low:
    if i<check_Low:
        temp = i
        check_Low = temp
        Lowest_found = True

    else:
        continue


for j in historical_High:
    # if j<check_High:
    #     Highest_found = False

    if j>check_High:
        temp1 = j
        check_High = temp1
        Highest_found = True

    else:
        continue


if Lowest_found==False:
    if open2 == close2 == low2 or open2 == close2 and close2>(low2-(high2-low2)/2) :
        if low3 < low1:
            print("Gravestone Doji, sell signal, Trend reversal to bearish ")
            StopLoss = high2
            Signal = ["sell"]

elif Highest_found==False:
    if open2 == close2 == high2 or open2 == close2 and open2<(high2-(high2-low2)/2):
        if high1 < high3:
            print("Dragonfly Doji, buy signal, Trend reversal to bearish ")
            StopLoss = low2
            Signal = ["Buy"]


elif open2 == close2 == low2 == high2:
        print("Four Price Doji, not important")
        Signal = ["none"]


elif open2 == close2:
        print("Long Legged Doji,Trend Uncertain, hold money")
        Signal = ["trend uncertain"]


else:
    Signal = "none"

print('Stoploss: '+ str(StopLoss))
print('Signal: '+ Signal)



