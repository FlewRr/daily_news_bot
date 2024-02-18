import json
from app.ml.parse_data import get_articles, get_pandas_dataframe
from app.ml.clustering import get_clusters
from app.ml.preprocessing import preprocess_corpus
from app.ml.topic_modelling import get_topics
from sentence_transformers import   SentenceTransformer
from app.ml.database.db import News, add_news_to_storage
from sqlalchemy.orm import Session
import time

def generate_dataset(db: Session, n_news: int, API_KEY=None):
    if not API_KEY:
        raise AttributeError
    st = time.time()
    df = get_pandas_dataframe(get_articles(n_news, API_KEY))
    fn = time.time()
    print(f"PARSING HAS ENDED {fn-st}")
    embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')
    st = time.time()
    clustered_data = get_clusters(embedder=embedder, data=df.texts, num_clusters=5)
    fn = time.time()
    print(f"CLUSTERING HAS ENDED {fn-st}")
    st = time.time()
    new_data, mapping = preprocess_corpus(clustered_data)
    fn = time.time()
    print(f"PREPROCESSING HAS ENDED {fn-st}")
    labeled_data = {}

    st = time.time()
    for column in new_data.keys():
        topics = [topic[0] for topic in get_topics(new_data[column], mapping, n=5)]
        if topics is not None:
            labeled_data[' '.join(topics)] = clustered_data[column]
    fn = time.time()
    print(f"TOPIC MODELLING HAS ENDED {fn-st}")
    topics = labeled_data.keys()
    mapping = {y: x+1 for x, y in enumerate(topics)}
    reversed_mapping = {x+1: y for x, y in enumerate(topics)}
    # with open('data.json', 'w') as f:
    #     json.dump(reversed_mapping, f)

    st = time.time()
    for column, data in labeled_data.items():
        for element in data:
            if element != '':
                add_news_to_storage(db, element, mapping[column])
    fn = time.time()
    print(f"ADDING TO THE STORAGE HAS ENDED {fn-st}")

    return reversed_mapping
