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
