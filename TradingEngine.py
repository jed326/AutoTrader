from DataCollection import database
from DataCollection import getData

#Run every MWF at market open

#insert yesterday's closing data into database

    #get all stocks from dataset
    #update all data

stocks = database.getAllStocks()
for stock in stocks:
    #get latest stock PriceData
    newDay = getData.lastDay(stock)
    database.insertRow(stock, newDay)

    #insert function
    print(stock)

#run model based on update dataset
