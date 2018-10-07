from flask import Flask, render_template, redirect, url_for, request
from Robinhood import Robinhood
import sys
sys.path.append("../")
from DataCollection import database

app = Flask(__name__)

my_trader = Robinhood()

@app.route('/')
def hello():
    return "Hello World!"

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        test1(request.form['username'], request.form['password'])
        return redirect(url_for('yeet'))
    return render_template('login.html')

@app.route('/yeet')
def yeet():
    stocks = database.getAllStocks()
    print(stocks)
    return render_template('stockchooser.html', stocks = stocks)


def test1(u, p):
    my_trader.login(username=u, password=p)