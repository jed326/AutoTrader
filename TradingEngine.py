from DataCollection import database

#Run every MWF at market open

#insert yesterday's closing data into database

    #get all stocks from dataset
    #update all data
stocks = database.getAllStocks()
for stock in stocks:
    print(stock)

#run model based on update dataset
