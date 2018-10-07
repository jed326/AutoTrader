import requests, csv

def getData(stock):
    with open("./Data/%s.csv" % stock, 'w') as c:
        URL = "https://api.iextrading.com/1.0/stock/" + stock.lower() + "/chart/5y"
        res = requests.get(url = URL)
        data = res.json()
        writer = csv.writer(c, delimiter=',')
        writer.writerow(["symbol", "date", "close", "high", "low", "open", "volume"])
        for d in data:
            writer.writerow([stock, d["date"], d["close"], d["high"], d["low"], d["open"], d["volume"]])

def lastDay(stock):
    URL = "https://api.iextrading.com/1.0/stock/" + stock.lower() + "/batch?types=quote,news,chart&range=1m&last=10"
    res = requests.get(url = URL)
    data = res.json()
    dataQ = data['quote']

    newData = [dataQ['symbol'], data['chart'][20]['date'], dataQ['close'], dataQ['high'], dataQ['low'], dataQ['open'], dataQ['latestVolume']]

    return newData
    # SchemaField('symbol', 'STRING', mode='required'),
    # SchemaField('date', 'DATE', mode='required'),
    # SchemaField('close', 'FLOAT', mode='required'),
    # SchemaField('high', 'FLOAT', mode='required'),
    # SchemaField('low', 'FLOAT', mode='required'),
    # SchemaField('open', 'FLOAT', mode='required'),
    # SchemaField('volume', 'INTEGER', mode='required'),

if __name__ == "__main__":
    print(lastDay("AAPL"))
