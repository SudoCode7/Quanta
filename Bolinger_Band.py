import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

pd.options.display.max_rows


yf.pdr_override()

ticker = 'icicibank' #input("Enter a stock ticker symbol: ")+'.NS'
ticker = ticker+".NS"
print(ticker)

startyear = 2019
startmonth = 1
startday = 1

start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()
df = pdr.get_data_yahoo(ticker, start, now)

df['mean'] = df['Close'].rolling(20).mean()
df['std'] = df['Close'].rolling(20).std()
df['upperband'] = df['mean'] + (df['std'] * 2)
df['lowerband'] = df['mean'] - (df['std'] * 2)
df = df.drop(['mean', 'std'], axis=1)
print(df)