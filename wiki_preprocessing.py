import pandas as pd
import nltk
#from wiki_scraper import wiki_crawler
from pyspark.sql import SparkSession
#raw_wiki_data = wiki_crawler()
from google.cloud import bigquery,storage


def upload_to_bucket(bucket_name, blob_path, local_path):
    bucket = storage.Client().bucket(bucket_name)
    blob = bucket.blob(blob_path)
    blob.upload_from_filename(local_path)
    return blob.public_url

# method call
bucket_name = 'wiki-us-elections-data' 
blob_path = 'path/'
local_path = r'D:\Study Materials\My git projects\USA-election-analysis\USA-election-analysis\src\Usa_elections\pipeline'


upload_to_bucket(bucket_name, blob_path, local_path)
