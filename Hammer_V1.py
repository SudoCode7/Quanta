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

startyear = 2020
startmonth = 12
startday = 3


# startyea = 2020
# startmont = 12
# startda = 8
# now = dt.datetime(startyea, startmont, startda)
start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()

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
historical_low = df['Low'][-26:length]
historical_High = df['High'][-26:length]
check_Low = round(df['Low'][length-2],2)
check_High = round(df['High'][length-2],2)
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
print(df.tail())

if Lowest_found==False:
    if (abs(close2-open2)*1.5)<abs(high2-low2): # Checking for hammer'''
            if low1<low3:
                Stoploss = low2
                Signal = "Buy"
            elif low1>low3:
                Signal = "none"
elif Highest_found==False:
    if (abs(close2-open2)*1.5)<abs(high2-low2): # Checking for hammer'''
        if high1>high3:
            Stoploss = high2
            Signal = "Sell"
        elif high1<high3:
            Signal = "none"

print('Signal: '+ str(Signal))
print('Stoploss: '+ str(StopLoss))


