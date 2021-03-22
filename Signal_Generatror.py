import yfinance as yf
import Many_In_one as indi
import pandas as pd
import datetime
from mailjet_rest import Client

def stratergy1(ticker):
    ticker = ticker.upper() + ".NS"
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

    if hr < 15 and hr>9:
        close_price = df['Close'][-2]
    else:
        close_price = df['Close'][-1]

     #staregy one
    boolean = True
    i=2
    if df['STX_12_3'][-1] == df['STX_10_1'][-1] == df['STX_11_2'][-1] == 'sell':
        while boolean == True:
            if df['STX_12_3'][-i] == df['STX_10_1'][-i] == df['STX_11_2'][-i] == 'sell':
                i+=1
            else:
                boolean= False
        return (i-2,'sell',close_price)

    elif df['STX_12_3'][-1] == df['STX_10_1'][-1] == df['STX_11_2'][-1] == 'buy':
        while boolean == True:
            if df['STX_12_3'][-i] == df['STX_10_1'][-i] == df['STX_11_2'][-i] == 'sell':
                i+=1
            else:
                boolean= False
        return (i-2,'buy',close_price)

    else:
        return (0,'NONE',0.0)

def stock():
    ticker = ['ICICIBANK','RELIANCE','tcs','infy','HINDUNILVR','JSWSTEEL','TATASTEEL','DIVISLAB','M&M','HDFCLIFE','CIPLA','TATAPOWER',
              'ITC','BHARTIARTL','HCLTECH','LT','PIDILITIND','KOTAKBANK']

    # df['Ticker'] = df.apply(lambda _: '', axis=0)
    # df['Signal'] = df.apply(lambda _: '', axis=0)
    # df['Signal Type'] = df.apply(lambda _: '', axis=0)
    k=[]
    signal=[]
    price = []
    TypeSignal = []
    for i in ticker:
        j,si,pr=stratergy1(i)
        k.append(j)
        signal.append(si)
        price.append(pr)
    for i in range(len(ticker)):
        if k[i]<=2:
            TypeSignal.append('Fresh')
        else:
            TypeSignal.append('Old')
    df = pd.DataFrame({'Ticker':ticker,'Signal':signal,'Signal Type':TypeSignal,'Price':price}, columns=['Ticker','Signal','Signal Type','Price'])
    df.to_excel('Signal.xlsx')
    #df = df.applymap(str)
    df = df.astype(str)
    d = pd.DataFrame(df)
    s = d.to_string
    #email(str(s))

def email(df):
    api_key = '0ed285bf226264e3b52d36a920c9c82d'  # Enter your api key here
    api_secret = '49c5467504f4e8849d172aae971dfd6d'  # Enter your api secret here
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    EMAIL_ADDRESS = 'jakshat70@gmail.com'
    message = df#'Your Stocks list'
    subject = message
    # title1 = tic.encode('utf-8')
    mailtext = message
    data = {
        'Messages': [
            {
                "From": {
                    "Email": EMAIL_ADDRESS,
                    "Name": "Sudo"
                },
                "To": [
                    {
                        "Email": EMAIL_ADDRESS,
                        "Name": "Sudo"
                    }
                ],
                "Subject": subject,
                "HTMLPart": mailtext,
                "CustomID": "Order Stat",
                #"Attachments" : [{"Content-type": "text\plain","Filename": "check.txt","Base64Content": "VGhpcyBpcyB5b3VyIGF0dGFjaGVkIGZpbGUhISEK"}]
            }
        ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())
    print('Email Sent!\n\n')
    pass



stock()


