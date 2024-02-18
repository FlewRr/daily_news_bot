import gensim
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import numpy as np
np.random.seed(2018)
import nltk
nltk.download('wordnet')

stemmer = SnowballStemmer('english')

def lemmatize_stemming(text, mapping):
    stemmed_word = stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
    mapping[stemmed_word] = text
    return stemmed_word

def preprocess(text, mapping={}):
  result = []
  for token in gensim.utils.simple_preprocess(text):
      if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
          result.append(lemmatize_stemming(token, mapping))
  return result

def preprocess_corpus(corpus):
    return_tokens_mapping = {}
    columns = corpus.keys()
    new_data = {}
    
    for column in columns:
        new_data[column] = [preprocess(text, return_tokens_mapping) for text in corpus[column]]

    return new_data, return_tokens_mapping