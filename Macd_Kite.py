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

startyear = 2019
startmonth = 1
startday = 1

start = dt.datetime(startyear, startmonth, startday)
now = dt.datetime.now()
df = pdr.get_data_yahoo(ticker, start, now)

def macd(df):
    df['12_ema'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['26_ema'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['macd_line'] = df['12_ema'] - df['26_ema']  # MACD Line: (12-day EMA - 26-day EMA)
    df['single_line'] = df['macd_line'].ewm(span=9, adjust=False).mean()  # Signal Line: 9-day EMA of MACD Line
    df['macd_hist'] = df['macd_line'] - df['single_line']  # MACD Histogram: MACD Line - Signal Line
    return df
print( macd(df) )