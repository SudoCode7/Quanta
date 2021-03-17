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
#
# #df['backward_ewm'] = df['Close'].ewm(span=20,min_periods=0,adjust=False,ignore_na=False).mean()
# df = df.sort_index()
def calc(df):
    df['ewm26'] = df['Close'].ewm(span=26, min_periods=0, adjust=False, ignore_na=False).mean()
    df['ewm12'] = df['Close'].ewm(span=12, min_periods=0, adjust=False, ignore_na=False).mean()

    df['macd'] = df['ewm12'] - df['ewm26']
    df['ewm9/Signal_Line'] = df['macd'].ewm(span=9, min_periods=0, adjust=False, ignore_na=False).mean()
    signal = []
    for i in range(len(df)):
        if df['macd'][i] > df['ewm9/Signal_Line'][i]:
            signal.append('buy')


        elif df['macd'][i] < df['ewm9/Signal_Line'][i]:
            signal.append('sell')


        else:
            signal.append('hold')
    df['signalMACD'] = signal
    return df
# exp1 = df.ewm(span=12, adjust=False).mean()
# exp2 = df.ewm(span=26, adjust=False).mean()  #15.223581    22.290528  -7.066948
# macd = exp1 - exp2
# exp3 = macd.ewm(span=9, adjust=False).mean()
#
# macd.plot(label=ticker+' MACD', color='g')
# ax = exp3.plot(label='Signal Line', color='r')
# df.plot(ax=ax, secondary_y=True, label=ticker)
#
# ax.set_ylabel('MACD')
# ax.right_ax.set_ylabel('Price Rs')
# ax.set_xlabel('Date')
# lines = ax.get_lines() + ax.right_ax.get_lines()
# ax.legend(lines, [l.get_label() for l in lines], loc='upper left')
# plt.show()
