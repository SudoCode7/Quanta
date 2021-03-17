from py5paisa import FivePaisaClient
from py5paisa.order import Order, OrderType, Exchange#, ExchangeType

client = FivePaisaClient(email="jakshat101@gmail.com", passwd="$Ecurity@158", dob="20020714")
client.login()

def sell(script_code,close_price,quantity):
    order = Order(order_type=OrderType.SELL, scrip_code=script_code, quantity=quantity, price=close_price,
                       atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    client.place_order(order)

def buy(script_code,close_price,quantity):
    order = Order(order_type=OrderType.BUY, scrip_code=script_code, quantity=quantity, price=close_price,
                       atmarket=False)  # AHPlaced= 'AHPlaced.AFTER_MARKET_CLOSED')
    client.place_order(order)

def order_stats():
    info = client.positions()
    ticker_name1 = info[0]['ScripName']
    Script_Code1 = info[0]['ScripCode']
    BuyQuantity1 = info[0]['BuyQty']
    LTP1 = info[0]['LTP']
    print(ticker_name1+'\n'+Script_Code1+'\n'+BuyQuantity1+'\n'+LTP1+'\n')
