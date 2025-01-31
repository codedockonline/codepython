


#######################################################################
#       Apple Stock Trend with Yahoo Finance in Python
#######################################################################

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


stock = yf.Ticker("AAPL")
df = stock.history(period="5y")


plt.figure(figsize=(10,5))
plt.plot(df['Close'], label='Closing Price')
plt.title('Apple Stock price trend')
plt.legend()
plt.show()
