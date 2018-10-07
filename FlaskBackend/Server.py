from flask import Flask, render_template, redirect, url_for, request
from Robinhood import Robinhood

#Global Fields
app = Flask(__name__)
my_trader = Robinhood()

@app.route('/')
def hello():
    #landing page, redirect to login
    return redirect(url_for('login'))

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login(request.form['username'], request.form['password'])
        return redirect(url_for('home'))
    return render_template('login.html')

def login(un, pw):
    my_trader.login(username = un, password = pw)

@app.route('/home')
def home():
    if request.method == 'POST':
        nextPage = request.form['nav']
        if nextPage == 'pick':
            return redirect(url_for('pick')) #Stock Chooser page
        if nextPage == 'portfolio':
            return redirect(url_for('portfolio')) #Portfolio page
        if nextPage == 'stats':
            return redirect(url_for('stats')) #Stats page
        #Cases for navigating to 3 sub pages
    return render_template('home.html')

@app.route('/')
def pick():
    return render_template('pick.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/stats')
def stats():
    return render_template('stats.html')
