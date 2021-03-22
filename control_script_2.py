import RSI_Stratergy_2
import yfinance as yf
import time
from mailjet_rest import Client
import datetime

amt = 600.0 #float(input("Enter a stock ticker symbol: "))
tic = 'itc'#(input("Enter a stock ticker symbol: ")).strip()#YESBANK' #
script_code = 500875#int(input("Enter the stock script code: "))#  scode[1].strip()532648 #
quantity = 1 #int(input("Enter the no. of quantity to be bought: "))
EMAIL_ADDRESS = 'jakshat70@gmail.com'#input("Enter your gmail address ")  # ENTER YOUR EMAIL ADDRESS
ticker = tic.upper()+".BO"
ticker = yf.Ticker(ticker)
df = ticker.history(period="5d")
api_key = '0ed285bf226264e3b52d36a920c9c82d' #Enter your api key here
api_secret = '49c5467504f4e8849d172aae971dfd6d' #Enter your api secret here
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
i=0

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
current = current_time.split(':')
hr = int(current[0])
min=int(current[1])

def email(message):
    subject = message
    #title1 = tic.encode('utf-8')
    mailtext = message+' '+tic +' '+  +'  for quantity of ' + str(quantity)
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
                # "TextPart": mailtext,
                "HTMLPart": mailtext,
                "CustomID": "Order Stat"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())
    print('Email Sent!\n\n')
    pass


if amt>quantity*df['Close'][-1]:
    signal = RSI_Stratergy_2.sratergy2(tic,script_code,quantity)
    f = open("RSI_Stratergy_1.txt",'r')
    i=0
    boolean = True

    while boolean==True and i !=2:
        if f.readline() == 'buy' or f.readline() == 'sell':
            # flag=False
            # print('ho')
            # email(' order executed')
            boolean = False
            break
        else:
            time.sleep(3*60*60)
        i+=1
    i=2
    if boolean == True:
        email(' order not executed')

    elif boolean == False:
        while boolean == False:
            if signal == 'buy':
                if i == 2:
                    email(' order executed')
                if hr > 15:
                    diff = (24 - hr) + 9
                else:
                    diff = 9 - hr
                time.sleep((abs(diff) * 60 * 60) + (60 * 20))
                signal = RSI_Stratergy_2.sratergy2(tic, script_code, quantity)


            elif signal == '':
                boolean = True
                message = ' Authorize TPIN of CDSL and Position will be squared off'
                email(message)
                print(message)
            i += 1

elif amt<quantity*df['Close'][-1]:
    print('NOT ENOUGH BALANCE')

else:
    email(' not executed')
    print('ORDER NOT EXECUTED')

