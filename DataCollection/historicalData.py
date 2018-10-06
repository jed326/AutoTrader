import numpy as np
import pandas as pd
import pandas_datareader.data as web
import pmysql

#from pandas_datareader.robinhood import RobinhoodQuoteReader, \
#    RobinhoodHistoricalReader

symbols = ["GOOG", "AMZN"]

for i in symbols:
    data = web.DataReader(i, 'lextrading')
    data.to_csv(i+".csv", sep = ',')
'''
'''
f = web.DataReader('F', 'robinhood')
Google = web.DataReader("GOOG", 'robinhood')
Amazon = web.DataReader("AMZN", 'robinhood')
