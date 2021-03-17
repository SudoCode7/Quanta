
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

pd.options.display.max_rows

yf.pdr_override()

# ticker = 'icicibank' #input("Enter a stock ticker symbol: ")+'.NS'
# ticker = ticker+".NS"
# print(ticker)
#
# startyear = 2019
# startmonth = 1
# startday = 1
#
# start = dt.datetime(startyear, startmonth, startday)
# now = dt.datetime.now()
# df = pdr.get_data_yahoo(ticker, start, now)

#df['backward_ewm'] = df['Close'].ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()
def calc(df):
    df = df.sort_index()
    df['ewm26'] = df['Close'].ewm(span=26, min_periods=0, adjust=False, ignore_na=False).mean()
    df['ewm12'] = df['Close'].ewm(span=12, min_periods=0, adjust=False, ignore_na=False).mean()

    df['macd'] = df['ewm12'] - df['ewm26']
    df['ewm9/Signal_Line'] = df['macd'].ewm(span=9, min_periods=0, adjust=False, ignore_na=False).mean()
    signal = []
    c = 0
    # to append hold instead of repetative sell/ buy signal... 1 for buy, 2 for sell

    for i in range(len(df)):
        if df['macd'][i] > df['ewm9/Signal_Line'][i]:
            if c == 1:
                signal.append('hold')
            else:
                signal.append('buy')
                c = 1


        elif df['macd'][i] < df['ewm9/Signal_Line'][i]:
            if c == 2:
                signal.append('hold')
            else:
                signal.append('sell')
                c = 2


        else:
            signal.append('hold')

    df['signalMACD'] = signal
    return df

