import requests, csv

stocks = ["AAPL", "F", "GOOG"]
for stock in stocks:
    with open("%s.csv" % stock, 'w') as c:
        URL = "https://api.iextrading.com/1.0/stock/" + stock.lower() + "/chart/5y"
        res = requests.get(url = URL)
        data = res.json()
        writer = csv.writer(c, delimiter=',')
        writer.writerow(["symbol", "begins_at", "close_price", "high_price", "low_price", "open_price", "volume"])
        for d in data:
            writer.writerow([stock, d["date"], d["close"], d["high"], d["low"], d["open"], d["volume"]])
