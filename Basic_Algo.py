import logging
from kiteconnect import KiteConnect


logging.basicConfig(level=logging.DEBUG)
kite = KiteConnect(api_key="your_api_key")
data = kite.generate_session("request_token_here", api_secret="your_secret")
kite.set_access_token(data["access_token"])
print('initialized')

Ticker = (input("Enter ticker:  ")).upper()
Enter_Price = float(input("\nEnter 'enter price':  "))
type_order = 1
#put_Order(Ticker, Enter_Price,type_order) #type= buy = 1 and sell = 0



def put_Order(Ticker, Enter_price, type_order): #type= buy = 1 and sell = 0
    if type==1:
        try:
            order_id = kite.place_order(tradingsymbol=Ticker,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))

    else :
        try:
            order_id = kite.place_order(tradingsymbol=Ticker,
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML)

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))
    print('order placed')
    Check_Price_and_Order(Ticker)


def Check_Price_and_Order(Ticker):
    print('order to be placed at: ')

