from pandas_datareader import data as pdr
import pandas as pd
from datetime import date
import datetime as dt
import matplotlib
import yfinance as yf
yf.pdr_override()
start_date = '2020-01-01'
end_date = dt.datetime.now()
ticker = 'ITC' #input("Enter ticker")
ticker = ticker+".NS"
# User pandas_reader.data.DataReader to load the desired data. As simple as that.
df = pdr.get_data_yahoo(ticker, start_date, end_date)
ma = 100
sma = 'Sma_'+str(ma)
df[sma] = df.iloc[: ,4].rolling(windows=ma).mean()
'''close = panel_data['Close']
sumHundred = 0.0
avgHundred = []
sumTwoHundred = 0.0
avgTwoHundred = []
length = len(close)
i = 0
while (length == i):
    cnt = 0
    for cnt in range(200):
        if cnt <= 100:
            sumHundred += close[cnt]
        sumTwoHundred += close[cnt]
        cnt += 1
    avgHundred.append((sumHundred / 100))
    avgTwoHundred.append((sumTwoHundred / 200))
    i += 1
print(sumTwoHundred/200)'''
print(df)