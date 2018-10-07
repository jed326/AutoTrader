import database, getDataFiveYear, time
stocks = ['TWTR', 'YAHOY', 'YIPI', 'YOOIF', 'MOMO', 'GDDY', 'BBBY', 'INTC', 'PCAR', 'INTU', 'MDLZ', 'BIDU', 'LLTC', 'KLAC', 'GOOGL', 'PCLN', 'AMGN', 'CSCO', 'ISRG', 'AAPL', 'F']

for stock in stocks:
    try:
        getDataFiveYear.getData(stock)
        database.insertCSV(stock)
    except:
        print("unlucky")
