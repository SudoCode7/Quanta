# from py5paisa import FivePaisaClient
# from py5paisa.order import OrderForStatus, Exchange, RequestList, ExchangeSegment
# import pandas as pd
import datetime
# from py5paisa.order import Order, OrderType, AHPlaced
# import time
#
#
# client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
# client.login()
# test_order_status = OrderForStatus(exchange=Exchange.BSE,exchange_segment=ExchangeSegment.CASH, scrip_code=500875, order_id=0)
#
# req_list = RequestList()
# #print(req_list)
# #test_order_status = OrderForStatus(exchange=Exchange.NSE, scrip_code=11915, order_id=0, exchange_type=ExchangeType.CASH)
# print(client.fetch_order_status(req_list))
# #print(client.fetch_order_status({11915}))

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

if weekday == "Saturdayi":
    diff = (24 - hr) + 9 + 24
    print(diff)


elif weekday == "Saturday":

    diff = (24 - hr) + 9
    print(diff)
    print((diff) + 0.25 )
    sec = (diff + 0.25 )
    print(sec )

