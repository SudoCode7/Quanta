import Many_In_one as calc
import yfinance as yf

def trend(ticker):
    ticker = ticker.upper() + ".BO"
    ticker = yf.Ticker(ticker)
    df = ticker.history(period="500d")
    print(df.tail())
    print(calc.SMA(df, 'Close', 'SMA_200', 200))

trend('itc')