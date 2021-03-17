"""
***Remember we are only taking last 3 candles into consideration

Lowest_found and Highest_found are to check for 25 days lowest and highest

Try to code your logic after line 83 and print the  signal in the last
"""

import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

yf.pdr_override()

stock = 'emmbi'  # input("Enter a stock ticker symbol: ")+'.NS'
stock = stock + ".NS"
print(stock)

startyear = 2016
startmonth = 3
startday = 1

start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()

# now = dt.datetime.now()
#
# d = dt.timedelta(days = 300)
# start = now - d

df = pdr.get_data_yahoo(stock, start, now)
length = len(df)

close1 = df['Close'][length - 1]
open1 = df['Open'][length - 1]
high1 = df['High'][length - 1]
low1 = df['Low'][length - 1]

close2 = df['Close'][length - 2]
open2 = df['Open'][length - 2]
high2 = df['High'][length - 2]
low2 = df['Low'][length - 2]

close3 = df['Close'][length - 3]
open3 = df['Open'][length - 3]
high3 = df['High'][length - 3]
low3 = df['Low'][length - 3]

Comment = ''
Signal = ''
StopLoss = 0.0
#
# Lowest_found = False
# Highest_found = False
# historical_low = df['Low'][-26:length]
# historical_High = df['High'][-26:length]
# check_Low = round(df['Low'][length - 2], 2)
# check_High = round(df['High'][length - 2], 2)

# for i in historical_low:
#
#     if i < check_Low:
#         temp = i
#         check_Low = temp
#         Lowest_found = True
#
# for j in historical_High:
#     # if j<check_High:
#     #     Highest_found = False
#
#     if j > check_High:
#         temp1 = j
#         check_High = temp1
#         Highest_found = True


if (high2 - max(open2, close2)) >= (abs(close2 - open2) * 1.5) and max(open2, close2) >= open1 :
    # since it doesnt make a difference in shooting star if candle stick is red or green,
    # so abs and max as open or close can be greater than other

    StopLoss = low2
    Signal = "buy (see comment)"
    Comment = "buy at " + str(high3)
    print("Inverted Hammer Candlestick, indication of bullish trend")

else:
    Signal = "none"

print('Signal: ' + Signal)
print('Comment: ' + Comment)
print('Stoploss: ' + str(StopLoss))