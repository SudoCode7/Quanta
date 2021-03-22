from py5paisa import FivePaisaClient
import pandas as pd
import datetime
from datetime import date
from py5paisa.order import Order, OrderType, AHPlaced
import time

# now = datetime.datetime.now()
# now = now.split('')
# print(now[0])
# current_time = now.strftime("%H:%M:%S")
# current = current_time.split(':')
# hr = int(current[0])
# min=int(current[1])
# week_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
# week_num=datetime.date(now[0]).weekday()
# print(week_days[week_num])

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

client = FivePaisaClient(email="@gmail.com", passwd="Password", dob="yyyymmdd")
client.login()

def sell(script_code,close_price,quantity,ticker,stoploss):
    data = {'Ticker': [ticker], "Script_code": [script_code], 'Signal': ["sell"],
            'Buy Price': [close_price], 'Quantity': [quantity],
            "Date Bought": [str(date.today())],'Stoploss':[stoploss]}
    if order_stats(data) == True:
        # order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
        #                atmarket=True)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED',price=close_price,)

        # order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1,
        #                    ahplaced=AHPlaced.AFTER_MARKET_CLOSED,price=close_price)
        # client.place_order(order)
        if (weekday != 'Saturday' and weekday != 'Sunday'):
            if ((9 <= hr <= 15) or (hr == 15 and min <= 25)) and (day != 'Saturday' or day != 'Sunday'):
                #print('ho')  # checker
                order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1, atmarket=True,
                              price=close_price, stoploss_price=stoploss)#,
                              #stoploss_price=stoploss)  # ahplaced=AHPlaced.AFTER_MARKET_CLOSED,is_stoploss=True
                client.place_order(order)

        else:
            #print('ha') #checker
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1,
                          ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price, atmarket=False, stoploss_price=stoploss)
            client.place_order(order)

        write_data(data,'clear')

        return 'sell'

    elif  order_stats(data) == False:
        # order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
        #                atmarket=False,price=close_price)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED',price=close_price,)
        # order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1,
        #               ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price)
        # client.place_order(order)
        if (weekday !='Saturday' and weekday !='Sunday'):
            if ((9 <= hr <= 15) or (hr == 15 and min <= 25)):
                #print('ho')  # checker
                order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1,
                              price=close_price, atmarket=True, stoploss_price=stoploss)
                client.place_order(order)
        else:
            #print('ha') #checker
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=1,
                          ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price, atmarket=False, stoploss_price=stoploss)
            client.place_order(order)
        write_data(data,'make')
        return 'sell'


def buy(script_code,close_price,quantity,ticker,stoploss):
    data = {'Ticker': [ticker], "Script_code": [script_code], 'Signal': ["buy"],
            'Buy Price': [close_price], 'Quantity': [quantity],
            "Date Bought": [str(date.today())],'Stoploss':[stoploss]}
    if order_stats(data) == False:
        # order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
        #                atmarket=True)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED',price=close_price,)
        # order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
        #               ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price)
        # client.place_order(order)
        if (weekday != 'Saturday' and weekday != 'Sunday'):
            if (hr >= 9 and hr <= 15) or (hr == 15 and min <= 25) and (day!='Saturday'or day!='Sunday'):
                #print('ho') #checker
                order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
                               price=close_price,atmarket=True, stoploss_price=stoploss)#ahplaced=AHPlaced.AFTER_MARKET_CLOSED,is_stoploss=True
                #client.place_order(order)
        else:
            #print('ho')
            #print('ha') #checker
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
                          ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price, atmarket=False, stoploss_price=stoploss)
            #client.place_order(order)
        write_data(data, 'make')
        return 'buy'

    elif order_stats(data) == True:
        # order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
        #                atmarket=True)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED',price=close_price,)
        # order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
        #               ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price)
        # client.place_order(order,'clear')
        if (weekday != 'Saturday' and weekday != 'Sunday'):
            if (hr >= 9 and hr <= 3) or (hr == 3 and min <= 25) and (day != 'Saturday' or day != 'Sunday'):
                order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
                              ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price)
                #client.place_order(order)
        else:
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=1,
                          ahplaced=AHPlaced.AFTER_MARKET_CLOSED, price=close_price, atmarket=False)
            #client.place_order(order)
        write_data(data,'clear')
        return 'buy'

# data = {'Ticker': 'ICICIBANK',"Script_code": 532174, 'Signal': "sell",
#                           'Buy Price': 581.29998779296, 'Quantity': 1,
#                           "Date Bought": str('2021-03-18'),"Stoploss":578.0}
def order_stats(data):
    df = pd.DataFrame(data= data,index=[0])
    sc = df['Script_code'][0]
    read = pd.read_excel('Order_book.xlsx', index_col=0)
    lis= []
    for i in read['Script_code']:
         lis.append(i)
    if sc in lis:
        return True
    else:
        return False


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
    #print(CheckTime)
    execution = client.positions()

    #print(execution)
    length = len(execution)
    trueLen = len(execution)
    if length == 0:
        length = 1
    time.sleep(2)
    boolean = True
    while boolean == True:
        for i in range(length):
            #print(str(trueLen))
            if trueLen >= 1:
                if execution[i]['ScripCode'] == tic[0]:
                    boolean = False
                    #print(boolean)
                    break

            else:
                if CheckTime == 'now':
                    #print(boolean)
                    time.sleep(60)

                elif CheckTime == 'later':
                    if hr > 15:
                        diff = (24 - hr) + 9

                    else:
                        diff = 9 - hr
                    time.sleep((diff * 60 * 60) + (60 * 15))

    #print('hi')
    if signal=='make':
        read = pd.read_excel('Order_book.xlsx', index_col='Ticker')
        #temp=pd.DataFrame.from_dict(data)
        #temp.set_index('Ticker')
        temp = [data["Script_code"],data['Signal'],data['Buy Price'],data['Quantity'],data["Date Bought"],data["Stoploss"]]
        df = pd.DataFrame(data=read)
        df.loc[data['Ticker'][0]] = temp[data["Script_code"],data['Signal'],data['Buy Price'],data['Quantity'],data["Date Bought"],data["Stoploss"]]
        df.to_excel('Order_book.xlsx')
        print('hi')

    elif signal=='clear':
        read = pd.read_excel('Order_book.xlsx', index_col='Ticker')
        read.drop(data['Ticker'], inplace=True)
        df = pd.DataFrame(data=read)
        df.to_excel('Order_book.xlsx')


