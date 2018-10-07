# TODO(developer): Uncomment the lines below and replace with your values.
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField
import os, csv, requests, datetime

project_id = 'autotrader-test-1'
dataset_id = 'PriceData'
userdata_id = 'UserData'
userdata_table = 'Data'

def addUserData(data):
    client = bigquery.Client(project_id)
    table_id = userdata_table  # replace with your table ID
    table_ref = client.dataset(userdata_id).table(table_id)
    table = client.get_table(table_ref)  # API request

    errors = client.insert_rows(table, data)

    assert errors == []

def queryUser(username):
    client = bigquery.Client(project_id)

    QUERY = ('SELECT * FROM `%s.%s.%s` WHERE Username=\'%s\' LIMIT 1000' % (project_id, userdata_id, userdata_table, username))

    query_job = client.query(QUERY)
    rows = query_job.result()

    return [[r[1], r[2], r[2], r[3]] for r in rows]


def updateQuantity(User, Stock, newQuantity):
    client = bigquery.Client(project_id)

    QUERY = ('UPDATE `%s.%s.%s` SET Quantity=%s WHERE Username=%s AND Stock=%s' % (project_id, userdata_id, userdata_table, newQuantity, User, Stock))

    query_job = client.query(QUERY)
    rows = query_job.result()

    print(rows)


def updateMoney(User, Stock, newMoney):
    client = bigquery.Client(project_id)

    QUERY = ('UPDATE `%s.%s.%s` SET Quantity=%s WHERE Username=%s AND Stock=%s' % (project_id, userdata_id, userdata_table, newMoney, User, Stock))

    query_job = client.query(QUERY)
    rows = query_job.result()

    print(rows)

def query(stock):
    client = bigquery.Client(project_id)

    QUERY = ('SELECT * FROM `%s.%s.%s` LIMIT 1000' % (project_id, dataset_id, stock))

    query_job = client.query(QUERY)
    rows = query_job.result()

    '''
    for row in rows:
        print(row.symbol)
    '''
    return(rows.to_dataframe())

#gets most recent price of all stocks
def getPrices(DATE):
    client = bigquery.Client(project_id)
    # DATE = datetime.date(int(DATE[0:4]), int(DATE[4:6]), int(DATE[6:8]))

    QUERY = ("SELECT * FROM `%s.%s.*` WHERE date=\'%s\'" % (project_id, dataset_id, DATE))

    query_job = client.query(QUERY)
    rows = query_job.result()
    out = {}
    for r in rows:
        out.update({r[0]:r[2]})

    return out

def insertCSV(stock):

    client = bigquery.Client(project_id)

    SCHEMA = [
        SchemaField('symbol', 'STRING', mode='required'),
        SchemaField('date', 'DATE', mode='required'),
        SchemaField('close', 'FLOAT', mode='required'),
        SchemaField('high', 'FLOAT', mode='required'),
        SchemaField('low', 'FLOAT', mode='required'),
        SchemaField('open', 'FLOAT', mode='required'),
        SchemaField('volume', 'INTEGER', mode='required'),
    ]

    table_ref = client.dataset(dataset_id).table(stock)

    load_config = LoadJobConfig()
    load_config.skip_leading_rows = 1
    load_config.schema = SCHEMA

    with open('Data/%s.csv' % stock, 'rb') as readable:
        r = csv.reader(readable, delimiter=',')
        client.load_table_from_file(
            readable, table_ref, job_config=load_config)

def insertRow(stock, data):
    client = bigquery.Client(project_id)
    table_id = stock  # replace with your table ID
    table_ref = client.dataset(dataset_id).table(table_id)
    table = client.get_table(table_ref)  # API request

    errors = client.insert_rows(table, data)

    assert errors == []


def getAllStocks():
    client = bigquery.Client(project_id)

    QUERY = ('SELECT * FROM `%s.__TABLES__`' % (dataset_id))

    query_job = client.query(QUERY)
    rows = query_job.result()

    return [r['table_id'] for r in rows]

if __name__ == "__main__":
    #insertCSV("GOOG")
    # rows = query("TWTR")
    # for r in rows:
    #     print(r)
    # insertCSV("NKE")
    # stocks = getAllStocks()
    # for s in stocks:
    #     print(s)
    # print(getPrices('2018-10-05'))

    addUserData([(u'jayd0104@gmail.com', u'COF', 16, 12.70)])

    # updateQuantity("jayd0104@gmail.com", "AAPL", 6)

    # print(queryUser("jayd0104@gmail.com"))
