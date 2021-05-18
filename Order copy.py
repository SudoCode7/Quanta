from py5paisa import FivePaisaClient
import pandas as pd
import datetime
from datetime import date
from py5paisa.order import Order, OrderType, AHPlaced
import time

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
current = current_time.split(':')
hr = int(current[0])
min=int(current[1])
now = str(now)
now = now.split(' ')
now = (now[0]).split('-')
day,mon,yr = now[0],now[1],now[2]
week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
week_num=datetime.date(int(day),int(mon),int(yr)).weekday()
weekday = week_days[week_num]



# login to network via api
client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
try:
    client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
    client.login()
    log = True
except:
    print('Login Failed')
    log = False
def place(script_code, close_price, quantity, ticker, stoploss, Signal):
    if log == True:
        if Signal == 'sell':
            check=sell(script_code, close_price, quantity, ticker, stoploss)

        elif Signal == 'buy':
            check=buy(script_code, close_price, quantity, ticker, stoploss)

        else:
            check=''
            print('No Signal has been received in Order Script')
    return check


# Sell Stock
def sell(script_code, close_price, quantity, ticker, stoploss):
    data = {'Ticker': [ticker], "Script_code": [script_code], 'Signal': ["sell"],
            'Buy Price': [close_price], 'Quantity': [quantity],
            "Date Bought": [str(date.today())], 'Stoploss': [stoploss]}
    signal='sell'
    if order_stats(script_code) == False:

        if (weekday != 'Saturday' and weekday != 'Sunday') :
            if ((9 <= hr <= 15) or (hr == 15 and min <= 25)):
                # print('ho')  # checker
                order = Order(order_type=OrderType.sell, scrip_code=script_code, quantity=1, atmarket=True,
                          price=close_price, stoploss_price=stoploss)
                # st+oploss_price=stoploss)  # ahplaced=ahplaced.after_market_closed,is_stoploss=true
                client.place_order(order)

            else:
                order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1, atmarket=True,
                              price=close_price, stoploss_price=stoploss,ahplaced=AHPlaced.AFTER_MARKET_CLOSED)
                # st+oploss_price=stoploss)  # ahplaced=AHPlaced.AFTER_MARKET_CLOSED,is_stoploss=True
                client.place_order(order)

        else:
            # print('ha') #checker
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1,
                          ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price, atmarket=False,
                          stoploss_price=stoploss)
            client.place_order(order)

        write_data(data, 'sell')

        return 'sell'

    elif order_stats(script_code) == True:
        return 'exists'


# Buy Stock
def buy(script_code, close_price, quantity, ticker, stoploss):
    data = {'Ticker': [ticker], "Script_code": [script_code], 'Signal': ["buy"],
            'Buy Price': [close_price], 'Quantity': [quantity],
            "Date Bought": [str(date.today())], 'Stoploss': [stoploss]}
    signal='buy'
    if order_stats(script_code) == True:
        return 'exists'

    elif order_stats(script_code) == False:

        if (weekday != 'Saturday' and weekday != 'Sunday'):
            if (hr >= 9 and hr <= 3) or (hr == 3 and min <= 25):
                order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
                              ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price)
                client.place_order(order)
            else:
                order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1, atmarket=True,
                              price=close_price, stoploss_price=stoploss,ahplaced=AHPlaced.AFTER_MARKET_CLOSED)
                # st+oploss_price=stoploss)  # ahplaced=AHPlaced.AFTER_MARKET_CLOSED,is_stoploss=True
                client.place_order(order)

        else:
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
                          ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price, atmarket=False)
            client.place_order(order)
        write_data(data, 'buy')
        return 'buy'


# Check for order if executed or exists
def order_stats(sc):
    pos=client.positions()
    hold=client.holdings()
    val1=False
    val2= False
    for i in range(len(hold)):
        dictonay = hold[i]
        for values,keys in dictonay.items():
            if keys==sc and (values=='BseCode' or values=='NseCode'):
                val1=True
                break

    for i in range(len(pos)):
        dictonay = pos[i]
        for values,keys in dictonay.items():
            if keys==sc and (values=='BseCode' or values=='NseCode'):
                val1=True
                break

    if val1==True or val2==True:
        return True
    else:
        return False


# Write data for executed orders
def write_data(data, signal):
    # if (9 <= hr <= 15) or (hr == 15 and min <= 25):
    #     CheckTime = 'now'
    # else:
    #     CheckTime = 'later'
    # tic = data["Ticker"]
    # execution = client.positions()
    # boolean = True
    # while boolean == True:
    #     for i in range(len(execution)):
    #         if execution[0]['Symbol'] == tic:
    #             boolean = False
    #             break
    #
    #         else:
    #             time.sleep(60)
    tic = data["Script_code"]
    ticker = data['Ticker']
    if (9 <= hr <= 15) or (hr == 15 and min <= 25):
        CheckTime = 'now'

    else:
        CheckTime = 'later'
    # print(CheckTime)
    execution = client.positions()

    # print(execution)
    length = len(execution)
    trueLen = len(execution)
    if length == 0:
        length = 1
    time.sleep(2)
    boolean = True
    while boolean == True:
        for i in range(length):
            # print(str(trueLen))
            if trueLen >= 1:
                if execution[i]['ScripCode'] == tic[0]:
                    boolean = False
                    # print(boolean)
                    break

            else:
                if CheckTime == 'now':
                    # print(boolean)
                    time.sleep(60)

                elif CheckTime == 'later':
                    if hr > 15:
                        diff = (24 - hr) + 9

                    else:
                        diff = 9 - hr
                    time.sleep((diff * 60 * 60) + (60 * 15))

    # print('hi')
    if signal == 'make':
        read = pd.read_excel('Order_book.txt.xls', index_col='Ticker')
        # temp=pd.DataFrame.from_dict(data)
        # temp.set_index('Ticker')
        temp = [data["Script_code"], data['Signal'], data['Buy Price'], data['Quantity'], data["Date Bought"],
                data["Stoploss"]]
        df = pd.DataFrame(data=read)
        df.loc[data['Ticker'][0]] = temp[
            data["Script_code"], data['Signal'], data['Buy Price'], data['Quantity'], data["Date Bought"], data[
                "Stoploss"]]
        df.to_excel('Order_book.txt.xls')
        print('hi')

    elif signal == 'clear':
        read = pd.read_excel('Order_book.txt.xls', index_col='Ticker')
        read.drop(data['Ticker'], inplace=True)
        df = pd.DataFrame(data=read)
        df.to_excel('Order_book.txt.xls')

    # data = {'Ticker': 'ICICIBANK',"Script_code": 532174, 'Signal': "sell",
    #                           'Buy Price': 581.29998779296, 'Quantity': 1,
    #                           "Date Bought": str('2021-03-18'),"Stoploss":578.0}
#print(order_stats(500845))


