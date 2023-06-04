import logging
import wikipediaapi

# create a function to get the titles based on keyword
article_titles=['2020 United States presidential election',
   '2016 United States presidential election',
   '2012 United States presidential election',
   '2008 United States presidential election',
   '2004 United States presidential election',
   '2014 United States presidential election',
   '2000 United States presidential election'
   ]

def wiki_crawler():
    raw_wiki= wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )
    wiki_article_summary={}
    for article in article_titles:
        if raw_wiki.page(article).exists():
            article_desc = raw_wiki.page(article).summary
            wiki_article_summary[article] = article_desc
        else:
            logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
            continue
