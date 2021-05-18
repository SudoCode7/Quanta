#*** If intraday order is placed it will fail to recognize in positions
# ADD gtt slide too
# quantity could be or could not me met exactly
# modifying order
# cancel the order if not executed by getting order id

from py5paisa import FivePaisaClient
import datetime
from py5paisa.order import Order, OrderType, AHPlaced, OrderForStatus, Exchange, RequestList, ExchangeSegment
import time

date = str(datetime.datetime.now())
date = date.split(' ')[0]

# login to network via api
try:
    client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
    client.login()
    log = True
except:
    print('Login Failed')
    log = False


# placing order
def place(script_code, close_price, quantity, stoploss, Signal, intraday, signal_type ):
    if log == True:
        if Signal == 'sell':
            check = sell(script_code, close_price, quantity, stoploss, intraday, signal_type)

        elif Signal == 'buy':
            check = buy(script_code, close_price, quantity, stoploss, intraday, signal_type)

        elif Signal == 'check':
            order_stats(script_code,Signal, intraday, signal_type, quantity)

        else:
            check = ''
            print('No Signal has been received in Order Script')

    else:
        check = ''

    return check


# Sell Stock
def sell(script_code, close_price, quantity, stoploss, intraday, signal_type):
    signal='sell'
    if signal_type == 'first':
        if intraday == True:
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
                          price=close_price, is_intraday=True, stoploss_price=stoploss, atmarket=False) # ahplaced=AHPlaced.AFTER_MARKET_CLOSED - for offline order or AMO
            client.place_order(order)
        else:
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
                          price=close_price, stoploss_price=stoploss, is_intraday=False, atmarket=False, is_vtd=True)
            client.place_order(order)

    # entre GTT args here
    elif signal=='second':
        if intraday == True:
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
                          price=close_price, is_intraday=True,stoploss_price=stoploss, atmarket=False)
            client.place_order(order)
        else:
            order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity,
                          price=close_price,stoploss_price=stoploss,is_intraday=False, atmarket=False, is_vtd=True)
            client.place_order(order)

    time.sleep(60)
    if order_stats(script_code,signal, intraday, signal_type, quantity)==True:
        return signal
    else:
        return ''


# Buy Stock
def buy(script_code, close_price, quantity, stoploss, intraday, signal_type):
    signal='buy'
    if signal_type == 'first':
        if intraday == True:
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=quantity,
                          price=close_price, is_intraday=True, stoploss_price=stoploss, atmarket=False)
            client.place_order(order)
        else:
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=quantity,
                          price=close_price, stoploss_price=stoploss,is_intraday=False, atmarket=False, is_vtd=True)
            client.place_order(order)

    # entre GTT args here
    elif signal == 'second':
        if intraday == True:
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=quantity,
                          price=close_price, is_intraday=True, stoploss_price=stoploss, atmarket=False)
            client.place_order(order)
        else:
            order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=quantity,
                          price=close_price,is_intraday=False, atmarket=False, stoploss_price=stoploss, is_vtd=True)
            client.place_order(order)

    time.sleep(60)
    if order_stats(script_code,signal, intraday, signal_type, quantity)==True:
        return signal
    else:
        return ''


# Check for order if executed or exists
def order_stats(sc, signal, intraday, signal_type, quantity):
    val2 = False
    flag = True
    i = 0

    if signal == 'buy'or signal == 'sell' and signal_type=='first':
        while i != 5 and flag == True:
            # hold = client.holdings()
            # for j in range(len(hold)):
            #     dictonay = hold[j]
            #     for values, keys in dictonay.items():
            #         if keys == sc and (values == 'BseCode' or values == 'NseCode'):
            #             flag = False
            #             val1 = True
            #             break

            pos = client.positions()
            for j in range(len(pos)):
                dictonary = pos[j]
                for values, keys in dictonary.items():
                    if (keys == sc and values == 'ScripCode') and (values == 'BuyQty' and keys != 0):
                        flag = False
                        val2 = True
                        break

            i = i + 1
            if intraday == False and flag == True:
                time.sleep(60 * 30)
            elif flag == True and intraday == True:
                time.sleep(60)

        if val2 == True:
            # write_data(sc, Signal_type)
            return True
        else:
            # cancel the order by getting order id
            client.cancel_order(exch_order_id="order id", traded_qty=quantity, scrip_code=sc)
            return False

    if signal == 'check':
        # test_order_status = OrderForStatus(exchange=Exchange.BSE, exchange_segment=ExchangeSegment.CASH,
        #                                    scrip_code=500875, order_id=0)
        # req_list = RequestList()
        pos = client.positions()
        return pos


# Write data for executed orders
def write_data(sc,Signal_type):
    sc = str(sc)
    if Signal_type == 'make':
        write = open('Order_book.txt','a')
        data = '\n'+ sc
        write.write(data)

    elif Signal_type == 'clear':
        write = open('Order_book.txt', 'r')
        lines = write.readlines()
        write.close()
        #print(lines)

        write = open('Order_book.txt', 'w')
        for line in lines:
            if line.strip("\n") != sc:
                write.write(line)
        write.close()
