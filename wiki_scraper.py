import logging
import wikipediaapi
import pandas as pd
import time

# create a function to get the titles based on keyword
article_titles=[f'{e_year} United States presidential election' for e_year in range(1900,2020,4)]

def wiki_crawler():
    raw_wiki= wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    wiki_article_summary={}
    for article in article_titles:
        # if article[:4]=='1960':  # To avoid out repeated HTTP calls
        #     time.sleep(5)
        if raw_wiki.page(article).exists():
            article_desc = raw_wiki.page(article).summary
            wiki_article_summary[article] = article_desc
        else:
            logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
            continue
    df = pd.DataFrame(wiki_article_summary.items(), columns=['title','summary'])
    return df

# raw_wiki_data = wiki_crawler()
# raw_wiki_data.to_csv("wiki_data_20thCentury.csv")