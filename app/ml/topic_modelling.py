import gensim

def get_topics(corpus, mapping, n=5, n_passes=10):
    dictionary = gensim.corpora.Dictionary(corpus)
    # dictionary.filter_extremes(no_below=n)

    bow_corpus = [dictionary.doc2bow(doc) for doc in corpus]
    tfidf = gensim.models.TfidfModel(bow_corpus)
    corpus_tfidf = tfidf[bow_corpus]

    if len(corpus_tfidf) == 0:
        return 
    
    lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=4, id2word=dictionary, passes=n_passes, workers=4)
    most_confident_topics = []
    for idx, topic in lda_model_tfidf.print_topics(-1):
        topics = topic.split('+')
        topics = [topics[i].split('*') for i in range(len(topics))]
        topics = [(mapping[topics[i][1].replace('"', '').strip()], float(topics[i][0])) for i in range(len(topics))]

        word = sorted(topics, key=lambda x: x[1], reverse=True)[0]
        if word not in most_confident_topics:
            most_confident_topics.append(word)

    return sorted(most_confident_topics, key=lambda x: x[1], reverse=True)
