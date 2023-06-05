import pandas as pd
import nltk
from wiki_scraper import wiki_crawler

#raw_wiki_data = wiki_crawler()

raw_wiki_data= pd.read_csv("wiki_data.csv")
print(raw_wiki_data.head())

