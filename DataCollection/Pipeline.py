import database, getDataFiveYear
stocks = ['TWTR', 'YAHOY', 'YIPI', 'YOOIF', 'MOMO', 'GDDY', 'BBBY', 'INTC', 'PCAR', 'INTU', 'MDLZ', 'BIDU', 'LLTC', 'KLAC', 'GOOGL', 'PCLN', 'AMGN', 'CSCO', 'ISRG']

for stock in stocks:
    try:
        getDataFiveYear.getData(stock)
        insert.insertCSV(stock)
    except:
        print("unlucky")
