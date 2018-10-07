# TODO(developer): Uncomment the lines below and replace with your values.
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField
import os, csv

def query():
    client = bigquery.Client('autotrader-test-1')

    QUERY = ('SELECT begins_at FROM `autotrader-test-1.HistoricalPrices.F` '
             'LIMIT 1000')

    query_job = client.query(QUERY)
    rows = query_job.result()

    for row in rows:
        print(row.begins_at)

"""
symbol
"""
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

if __name__ == "__main__":
    insertCSV("GOOG")

# dataset_id = 'autotrader-test-1:HistoricalPrices'  # replace with your dataset ID
# # For this sample, the table must already exist and have a defined schema
# table_id = 'autotrader-test-1:HistoricalPrices.F'  # replace with your table ID
# # IN A LOOP
# table_ref = client.dataset(dataset_id).table(table_id)
# table = client.get_table(table_ref)  # API request
#
# rows_to_insert = [
#     (u'Phred Phlyntstone', 32),
#     (u'Wylma Phlyntstone', 29),
# ]
#
# errors = client.insert_rows(table, rows_to_insert)  # API request
#
# assert errors == []
