from Robinhood import Robinhood

my_trader = Robinhood()

stock_instrument = my_trader.instruments("GEVO")[0]

my_trader.print_quote("AAPL")

my_trader.get_quote("AAPL")

my_trader.print_quotes(stocks=["FB", "MSFT"])

q = my_trader.get_historical_quotes(stock = "BTC", interval = "day", span = "year", bounds = "regular")
print(q)

quote_info = my_trader.quote_data("AAPL")
print(quote_info['previous_close'])
