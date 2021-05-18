#modifying order in stoploss once some milestone is hit

import Order
import time
import datetime

# tic = 'itc'#(input("Enter a stock ticker symbol: ")).strip()#YESBANK' #
# script_code = 500875#int(input("Enter the stock script code: "))#  scode[1].strip()532648 #
# quantity = 1 #int(input("Enter the no. of quantity to be bought: "))


def execution(script_code, close_price, quantity, stoploss, Signal, intraday ):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current = current_time.split(':')
    hr = int(current[0])
    min = int(current[1])
    now = str(now)
    now = now.split(' ')
    now = (now[0]).split('-')
    day, mon, yr = now[0], now[1], now[2]
    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    week_num = datetime.date(int(day), int(mon), int(yr)).weekday()
    weekday = week_days[week_num]

    if weekday == "Saturday":
        diff = (24 - hr) + 9 +24
        time.sleep(diff *60 *60)

    elif weekday == "Sunday":
        diff = (24 - hr) + 9
        time.sleep(diff * 60*60)

    else:
        if hr > 14:
            diff = (24 - hr) + 9
            time.sleep((diff * 60 * 60) + (60 * 15))
        else:
            pass

    signal = Order.place(script_code, close_price, quantity, stoploss, Signal, intraday,'first')

    if signal == 'buy' or signal == 'sell':
        #send order for gtt for next 45 days
        if signal=='buy':
            Signal='sell'
        elif signal=='sell':
            Signal='buy'

        # place gtt order for 45 days
        Order.place(script_code, close_price, quantity, stoploss, Signal, intraday, 'second')

        # return appropriate signal if the order is executed successfully
        return True


    elif signal == '':
        return False




        # while boolean == True and i != 2:
        #     if f.readline() == 'buy' or f.readline() == 'sell':
        #         # flag=False
        #         # print('ho')
        #         # email(' order executed')
        #         boolean = False
        #         break
        #     else:
        #         time.sleep(3 * 60 * 60)
        #     i += 1
        # i = 2
        # if boolean == True:
        #     email(' order not executed')
        #
        # elif boolean == False:
        #     while boolean == False:
        #         if signal == 'buy':
        #             if i == 2:
        #                 email(' order executed')
        #             if hr > 15:
        #                 diff = (24 - hr) + 9
        #             else:
        #                 diff = 9 - hr
        #             time.sleep((abs(diff) * 60 * 60) + (60 * 20))
        #             signal = RSI_Stratergy_1.stratergy1(tic, script_code, quantity)
        #
        #
        #         elif signal == '':
        #             boolean = True
        #             message = ' Authorize TPIN of CDSL and Position will be squared off'
        #             email(message)
        #             print(message)
        #         i += 1

