from flask import Flask, render_template, redirect, url_for, request
from Robinhood import Robinhood
import sys, datetime
sys.path.append("../")
from DataCollection import database

#Global Fields
app = Flask(__name__)
my_trader = Robinhood()
username = ""

@app.route('/')
def hello():
    #landing page, redirect to login
    return redirect(url_for('login'))

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        login(request.form['username'], request.form['password'])
        return redirect(url_for('home'))
    return render_template('login.html')

def login(un, pw):
    my_trader.login(username = un, password = pw)

@app.route('/home')
def home():
    # if request.method == 'POST':
    #     nextPage = request.form['nav']
    #     if nextPage == 'pick':
    #         return redirect(url_for('pick')) #Stock Chooser page
    #     if nextPage == 'portfolio':
    #         return redirect(url_for('portfolio')) #Portfolio page
    #     if nextPage == 'stats':
    #         return redirect(url_for('stats')) #Stats page
        #Cases for navigating to 3 sub pages
    return render_template('home.html')

@app.route('/stocks')
def pick():
    now = datetime.datetime.now()

    date = str(now.year) + '-' + str(now.month) + '-'  + str(now.day)
    date = '2018-10-05'
    print(date)
    stocks = database.getPrices(date)
    print(stocks)
    return render_template('stockchooser.html', stocks = stocks)

@app.route('/portfolio')
def portfolio():
    #get all rows by user
    username = "jayd0104@gmail.com"
    print("port", username)
    portfolio = database.queryUser(username)
    for r in portfolio:
        r[2] = int(r[2])*float(my_trader.quote_data("AAPL")['previous_close'])
    print(portfolio)
    return render_template('portfolio.html', results=portfolio)

@app.route('/stats')
def graphs():
    return render_template('graphs.html')

if __name__ == "__main__":
    print(username)
    rows = database.queryUser(username)
    print(rows)
    for r in rows:
        print(r)
