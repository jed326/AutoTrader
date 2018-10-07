# TODO(developer): Uncomment the lines below and replace with your values.
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField
import os, csv, requests

project_id = 'autotrader-test-1'
dataset_id = 'PriceData'

def query(stock):
    client = bigquery.Client(project_id)

    QUERY = ('SELECT * FROM `%s.%s.%s` LIMIT 1000' % (project_id, dataset_id, stock))

    query_job = client.query(QUERY)
    rows = query_job.result()

    return rows

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

def insertRow(stock):
    pass

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
    insertCSV("AAPL")

    stocks = getAllStocks()
    for s in stocks:
        print(s)
