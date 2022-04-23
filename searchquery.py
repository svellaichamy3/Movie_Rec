import pandas as pd
import matplotlib.pyplot as plt
import string
from gensim import corpora,models, similarities
import numpy as np
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
import time
import pickle
from gensim.models import CoherenceModel
class search_query:
    
    def __init__(self, model_path, dictionary_path, corpus_path, nn_file_path, all_posters):
        self.model_path = model_path
        self.dictionary_path = dictionary_path
        self.corpus_path = corpus_path
        self.nn_file_path = nn_file_path
        self.all_posters = all_posters
        self.punctuation = set(string.punctuation)
        self.stoplist = set(stopwords.words('english'))
        self.lemma = WordNetLemmatizer()
        
    def load_info(self):
        self.model = models.LdaModel.load(self.model_path)
        self.posters = pd.read_csv(self.all_posters)
        self.dictionary = corpora.Dictionary.load(self.dictionary_path)
        self.movie_data = pd.read_csv(self.nn_file_path)
        
        texts = self.movie_data['Plot'].to_list()
        texts = [text.split(" ") for text in texts]
        
        with open(self.corpus_path, "rb") as fp:   
            self.corpus = pickle.load(fp)
            
    def remove_punctuation(self, text):
        return ''.join([char for char in text if char not in self.punctuation])


    def remove_numbers(self, text):
        return ''.join([char for char in text if not char.isdigit()])


    def remove_stopwords_lowercase(self, text):
        return ' '.join([word.lower() for word in text.split() if word not in self.stoplist])


    def lemmatize(self, text):
        return ' '.join([self.lemma.lemmatize(word) for word in text.split()])


    def clean_text(self, text):
        text = self.remove_punctuation(text)
        text = self.remove_numbers(text)
        text = self.remove_stopwords_lowercase(text)
        text = self.lemmatize(text)
        return text
        
    def get_similarity(self, query):
        index = similarities.MatrixSimilarity(self.model[self.corpus])
        sims = index[query]
        return sims
    
    def search(self, search_input):
        search_input = self.dictionary.doc2bow(self.clean_text(search_input).split())
        query_vector = self.model[search_input]
        sims = self.get_similarity(query_vector)
        sims = sorted(enumerate(sims), key=lambda item: -item[1])[0:3]
        movie_names = []
        poster_urls = []
        for s in sims:
            movie_1 = self.movie_data['Title'][s[0]] 
            movie_names.append(movie_1)
            movie_2 = self.movie_data['nn'][s[0]].split(", ")[0]
            movie_names.append(movie_2)
            poster_urls.append(self.movie_data['Poster'].tolist()[s[0]])
            poster_urls.append(self.posters[self.posters['Title'] == movie_2]['Poster'].tolist()[0])
        #movie names, poster url, 
        return movie_names,poster_urls