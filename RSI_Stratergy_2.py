import yfinance as yf
import Many_In_one as indi
import datetime
import pandas as pd
import Order_placement1

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# ticker = 'ICICIBANK'#(input("Enter a stock ticker symbol: ")).strip()
# script_code = 532174 #int(input("Enter the stock script code: "))#  scode[1].strip()
# ticker = ticker.upper()+".BO"
# quantity = 1 #int(input("Enter the no. of quantity to be bought: "))
def sratergy2(ticker, script_code, quantity):
    tic = ticker
    ticker = ticker.upper() + ".BO"
    print(ticker + '  ' + str(script_code))
    ticker = yf.Ticker(ticker)

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current = current_time.split(':')
    hr = int(current[0])

    # get historical market data and intitialize same index to signal
    df = ticker.history(period="3500d")
    signal = pd.DataFrame(index=df.index)
    df = pd.concat([df, signal], axis=1)

    # get necessary date
    signal = indi.SuperTrend(df, 10, 3)
    signal = indi.EMA(df, 'Close', 'ema_200', 200)
    print(df.tail(3))

    # srategy 2
    if hr < 15 and hr > 9:
        close_price = df['Close'][-2]
        stoploss = df['Close'][-3]
        j=-2
    else:
        close_price = df['Close'][-1]
        stoploss = df['Close'][-2]
        j=-1

    f = open("RSI_Stratergy_2.txt", "r")
    import Order_placement
    if f.readline() == 'buy':
        #f = open("RSI_Stratergy_2.txt", "r+")
        # if f.readline() == 'sell':
        #     print('money is growing')
        #     f.close()
        if close_price < df['ema_200'][j] and df['STX_10_3'][j] == 'sell':
            f.close()
            f = open("RSI_Stratergy_2.txt", "w")
            f.write('')

            Order_placement1.sell(script_code, close_price, quantity=quantity, ticker=ticker,stoploss=stoploss)
            print('\n' + 'sell')
            return 'sell'
        # else:
        #     f = open("RSI_Stratergy_1.txt", "w")
        #     f.write('sell')
        #     import Order_placement
        #     Order_placement.sell(script_code, close_price, quantity=quantity, ticker=ticker)
        #     print('\n' + 'sell')

    elif f.readline() == '':
        #print('ha')
        # f = open("RSI_Stratergy_1.txt", "r+")
        #
        #     print('money is growing')

        # elif f.readline() == 'sell':
        #     f.close()
        #     f = open("RSI_Stratergy_1.txt", "w")
        #     f.write('buy')
        #     import Order_placement
        #     Order_placement.sell(script_code, close_price, quantity=quantity, ticker=tic)
        #     print('\n' + 'buy')
        if df['STX_10_3'][j] == 'buy' and close_price > df['ema_200'][j]:
            f.close()
            f = open("RSI_Stratergy_2.txt", "w")
            f.write('buy')
            Order_placement1.buy(script_code, close_price, quantity=quantity, ticker=tic,stoploss=stoploss)
            print('\n' + 'buy')
            return "buy"


    else:
        print('\n' + 'no particular signal generated.-  HOLDING')

