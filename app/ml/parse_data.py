import requests
import time
import pandas as pd

def get_articles(n=1, API_KEY=None):
    if not API_KEY:
        return
    articles = []

    for i in range(n):
        url='https://api.nytimes.com/svc/search/v2/articlesearch.json?q='+'&api-key='+API_KEY+'&page='+str(i)
        response = requests.get(url).json()
        docs = response['response']['docs']
        for doc in docs:
            filteredDoc = {}
            filteredDoc['title'] = doc['headline']['main']
            filteredDoc['abstract'] = doc['abstract']
            filteredDoc['paragraph'] = doc['lead_paragraph']
            articles.append(filteredDoc)

        time.sleep(12)
    return articles


def get_pandas_dataframe(articles):
    df = pd.DataFrame(articles)
    df['texts'] = 'Title: ' + df.title + '\nAbstract: ' + df.abstract + '\nParagraph:' + df.paragraph
    df = df.drop(columns=['title', 'abstract', 'paragraph'])

    return df



