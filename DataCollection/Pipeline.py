import database, getData, time
#stocks = ['TWTR', 'YAHOY', 'YIPI', 'YOOIF', 'MOMO', 'GDDY', 'BBBY', 'INTC', 'PCAR', 'INTU', 'MDLZ', 'BIDU', 'LLTC', 'KLAC', 'GOOGL', 'PCLN', 'AMGN', 'CSCO', 'ISRG', 'AAPL', 'F']
stocks = ['FB', 'NFLX', 'YUM', 'BTCUSDT', 'ETHUSDT', 'XRPUSDT', 'ORCL', 'CMCSA', 'PEP', 'GE', 'SBUX', 'FOXA', 'TSLA', 'SNAP']


for stock in stocks:
    try:
        getData.getData(stock)
        database.insertCSV(stock)
    except:
        print("unlucky")
