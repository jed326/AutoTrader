# TODO(developer): Uncomment the lines below and replace with your values.
from google.cloud import bigquery
from google.cloud.bigquery import LoadJobConfig
from google.cloud.bigquery import SchemaField
import os

def query():
    client = bigquery.Client('autotrader-test-1')

    QUERY = ('SELECT begins_at FROM `autotrader-test-1.HistoricalPrices.F` '
             'LIMIT 1000')

    query_job = client.query(QUERY)
    rows = query_job.result()

    for row in rows:
        print(row.begins_at)

def insertCSV():
    

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
