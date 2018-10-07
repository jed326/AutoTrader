# TODO(developer): Uncomment the lines below and replace with your values.
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField
import os, csv

def query(stock):
    client = bigquery.Client('autotrader-test-1')

    QUERY = ('SELECT * FROM `autotrader-test-1.HistoricalPrices.%s` LIMIT 1000' % stock)

    query_job = client.query(QUERY)
    rows = query_job.result()

    # for row in rows:
    #     print(row['high'])

    return rows

def insertCSV(stock):

    client = bigquery.Client('autotrader-test-1')

    SCHEMA = [
        SchemaField('symbol', 'STRING', mode='required'),
        SchemaField('date', 'DATE', mode='required'),
        SchemaField('close', 'FLOAT', mode='required'),
        SchemaField('high', 'FLOAT', mode='required'),
        SchemaField('low', 'FLOAT', mode='required'),
        SchemaField('open', 'FLOAT', mode='required'),
        SchemaField('volume', 'INTEGER', mode='required'),
    ]

    table_ref = client.dataset('HistoricalPrices').table(stock)

    load_config = LoadJobConfig()
    load_config.skip_leading_rows = 1
    load_config.schema = SCHEMA

    with open('%s.csv' % stock, 'rb') as readable:
        r = csv.reader(readable, delimiter=',')
        # for row in r:
        #     print(r)
        client.load_table_from_file(
            readable, table_ref, job_config=load_config)

def insertRow(stock):
    pass

if __name__ == "__main__":
    #insertCSV("GOOG")
    r = query("TWTR")
    for x in r:
        print(x['close'])
