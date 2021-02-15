import yfinance as yf
import pandas as pandas

pandas.set_option('display.max_rows', 1000)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

# msft = yf.Ticker("MSFT")
# tesla = yf.Ticker("TSLA")
apple = yf.Ticker("AAPL")
ba = yf.Ticker("BA")
osur = yf.Ticker("OSUR")
gspc = yf.Ticker("^GSPC")       # s&p500

# print (msft.info)

# print (msft.actions)

# print(type(msft.dividends))     # class 'pandas.core.series.Series'

# print(apple.splits)

# print("major holders: ")
# print(apple.major_holders)
# print("institutional holders: ")
# print(apple.institutional_holders)

# print(ba.sustainability)

print(osur.history(
        period="2d",
        interval="1m",
        prepost=True
    ))

# print(type(osur.history()))     # pandas.core.frame.DataFrame

