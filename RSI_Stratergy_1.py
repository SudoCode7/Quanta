import yfinance as yf
import Many_In_one as indi
import pandas as pd
import datetime
#import Order_placement1


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

# ticker = 'ICICIBANK' #(input("Enter a stock ticker symbol: ")).strip()
# script_code = 532174 #int(input("Enter the stock script code: "))#  scode[1].strip()
# quantity = 1 #int(input("Enter the no. of quantity to be bought: "))
def stratergy1(ticker, script_code, quantity):
    tic = ticker
    ticker = ticker.upper() + ".BO"
    print(ticker + '  ' + str(script_code))
    ticker = yf.Ticker(ticker)

    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current = current_time.split(':')
    hr = int(current[0])

    # get historical market data and intitialize same index to signal
    df = ticker.history(period="400d")
    signal = pd.DataFrame(index=df.index)
    df = pd.concat([df, signal], axis=1)

    # get necessary date
    signal = indi.SuperTrend(df, 12, 3)
    signal = indi.SuperTrend(df, 10, 1)
    signal = indi.SuperTrend(df, 11, 2)
    signal = indi.EMA(df, 'Close', 'ema_200', 200)
    print(df.tail(3))

    # staregy one
    if hr < 15 and hr>9:
        close_price = df['Close'][-2]
        j=-2
    else:
        close_price = df['Close'][-1]
        j=-1

    import Order_placement1
    f = open("RSI_Stratergy_1.txt", "r+")
    stoploss = df['Close'][-2] + ((df['Close'][-2] / 100) * 5)
    if f.readline() == '':
        # if df['STX_12_3'][-1] == df['STX_10_1'][-1] == df['STX_11_2'][-1] == 'sell':
        #     f.close()
        #     f = open("RSI_Stratergy_1.txt", "w")
        #     val=Order_placement.sell(script_code, close_price, quantity=quantity, ticker=tic, stoploss=stoploss)
        #     f.write(val)
        #     print('\n' + 'sell')
        #     return 'sell'

        if df['STX_12_3'][j] == df['STX_10_1'][j] == df['STX_11_2'][j] == 'buy':
            f.close()
            f = open("RSI_Stratergy_1.txt", "w")
            val = Order_placement1.buy(script_code, close_price, quantity=quantity, ticker=tic, stoploss=stoploss)
            f.write(val)
            print('\n' + 'buy')
            return 'buy'

    elif f.readline() == 'buy' and (df['STX_12_3'][j] != 'buy'or df['STX_10_1'][j] != 'buy'or df['STX_11_2'][j] != 'buy'):#or f.readline() == 'sell':
        #if  f.readline() == 'buy' and df['STX_12_3'][-1] == df['STX_10_1'][-1] == df['STX_11_2'][-1] != 'buy':
        f = open("RSI_Stratergy_1.txt", "w")
        f.write('')
        Order_placement1.sell(script_code, close_price, quantity=quantity, ticker=tic, stoploss=stoploss)
        print('\n' + 'sell')
        return 'sell'

        # elif f.readline() == 'sell' and df['STX_12_3'][-1] == df['STX_10_1'][-1] == df['STX_11_2'][-1] != 'sell':
        #     f = open("RSI_Stratergy_1.txt", "w")
        #     f.write('')
        #     Order_placement.buy(script_code, close_price, quantity=quantity, ticker=tic, stoploss=stoploss)
        #     print('\n' + 'buy')
        #     return 'buy'

    else:
        print('\n' + 'no particular signal generated.-  HOLDING')

    '''if df['STX_12_3'][-1]==df['STX_10_1'][-1]==df['STX_11_2'][-1]=='sell':
        f = open("RSI_Stratergy_1.txt", "r+")
        if f.readline() == 'sell':
            print('money is growing')
            f.close()
        elif f.readline() == 'buy':
            f.close()
            f = open("RSI_Stratergy_1.txt", "w")
            f.write('sell')
            import Order_placement
            Order_placement.sell(script_code,close_price, quantity=quantity, ticker=tic)
            print('\n'+'sell')
        else:
            f = open("RSI_Stratergy_1.txt", "w")
            f.write('sell')
            import Order_placement
            Order_placement.sell(script_code, close_price, quantity=quantity, ticker=tic)
            print('\n' + 'sell')

    elif df['STX_12_3'][-1]==df['STX_10_1'][-1]==df['STX_11_2'][-1]=='buy':
        f = open("RSI_Stratergy_1.txt", "r+")
        if f.readline() == 'buy':
            print('money is growing')
            f.close()
        elif f.readline() == 'sell' :
            f.close()
            f = open("RSI_Stratergy_1.txt", "w")
            f.write('buy')
            import Order_placement
            Order_placement.sell(script_code, close_price, quantity=quantity, ticker=tic)
            print('\n'+'buy')

        else:
            f.close()
            f = open("RSI_Stratergy_1.txt", "w")
            f.write('buy')
            import Order_placement
            Order_placement.sell(script_code, close_price, quantity=quantity, ticker=tic)
            print('\n' + 'buy')

    else :
        print('\n'+'hold')'''

