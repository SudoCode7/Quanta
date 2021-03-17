from matplotlib import pyplot as plt
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

startyear = 2020
startmonth = 1
startday = 1

start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()
df = pdr.get_data_yahoo(ticker, start, now)

def rsi(df, period):
    df['pnl'] = df['Close'].diff()
    df.loc[df['pnl'] >= 0, 'gain'] = df['pnl']
    df['gain'].fillna(value=0, inplace=True)
    df.loc[df['pnl'] < 0, 'loss'] = df['pnl'].abs()
    df['loss'].fillna(value=0, inplace=True)
    df['average_gain'] = df['gain'].ewm(com=period - 1, min_periods=period).mean()
    df['average_loss'] = df['loss'].ewm(com=period - 1, min_periods=period).mean()
    df['rs'] = df['average_gain'] / df['average_loss']
    df['rsi'] = 100 - (100 / (1 + df['rs']))
    Signal = []

    for i in df['rsi']:
        if i>70.0:
            Signal.append("buy")

        elif i<30.0:
            Signal.append("sell")

        else:
            Signal.append("hold")

    df['Signal']= Signal
    return df

print( rsi(df, 14) )