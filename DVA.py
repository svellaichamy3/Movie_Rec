
import streamlit as st
import numpy as np
from PIL import Image
import requests
import urllib.request
import searchquery
import pandas as pd
import matplotlib.pyplot as plt
from gensim import corpora,models, similarities
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
import time
import pickle
import string
from gensim.models import CoherenceModel
# nltk.download('stopwords')
# nltk.download('wordnet')
st.set_page_config(page_title="Movie Recommendation", layout="wide")
st. markdown("<h2 style='text-align: center; color: black;'>Movie Recommendation</h2>", unsafe_allow_html=True)
c1, c2 = st.columns([2,2])

st.write('<style>div.row-widget.stRadio > div{flex-direction:row; justify-content: flex-start;} </style>', unsafe_allow_html=True)

st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-size:1rem; padding-left:2px; padding-right:10px;}</style>', unsafe_allow_html=True)
st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)

# with c1:
    
    # test = searchquery.search_query("LDAModel.model","lda_dict","lda_corpus","movie_data_nn.csv","NN_lda.csv")
    # test.load_info()
    # st.write('Enter keywords related to plot')
    # title2 = st.text_input('Plot', 'Romantic Love')
    # st.write('Movies whose plots are similar to ',title2,':')
    # a,b = test.search(title2)
    # urllib.request.urlretrieve(b[0],'im1.png')
    # im1 = Image.open("im1.png")
    # urllib.request.urlretrieve(b[1],'im2.png')
    # im2 = Image.open("im2.png")
    # urllib.request.urlretrieve(b[2],'im3.png')
    # im3 = Image.open("im3.png")
    # # urllib.request.urlretrieve(b[3],'im4.png')
    # # im4 = Image.open("im4.png")
    # urllib.request.urlretrieve(b[4],'im5.png')
    # im5 = Image.open("im5.png")
    # urllib.request.urlretrieve(b[5],'im6.png')
    # im6 = Image.open("im6.png")
    # images_on_page2= [im1,im2,im3,im5,im6] 
    # st.image(images_on_page2, width = 150,caption = [a[0],a[1],a[2],a[4],a[5]])

with c2:
    data = pd.read_csv("movie_data_with_nn_poster.csv")
    titles_with_nn = data.loc[:,["Title","5 Nearest","Poster_nn"]]
    option = st.selectbox('Movie title',tuple(list(titles_with_nn['Title'])))
    id = data.index[data['Title'] == option].tolist()[0]
    Movies = titles_with_nn.loc[id].at["5 Nearest"]  
    movie_names = Movies.split(",") 
    poster_links = titles_with_nn.loc[id].at["Poster_nn"]
    poster_links = poster_links.replace("[","")
    poster_links = poster_links.replace("]","")
    poster_links = poster_links.replace("'","")
    poster_names =poster_links.split(",") 
    urllib.request.urlretrieve(poster_names[0],'ima1.png')
    ima1 = Image.open("ima1.png")
    urllib.request.urlretrieve(poster_names[1],'ima2.png')
    ima2 = Image.open("ima2.png")
    urllib.request.urlretrieve(poster_names[2],'ima3.png')
    ima3 = Image.open("ima3.png")
    urllib.request.urlretrieve(poster_names[3],'ima4.png')
    ima4 = Image.open("ima4.png")
    urllib.request.urlretrieve(poster_names[4],'ima5.png')
    ima5 = Image.open("ima5.png")
    images_on_page3= [ima1,ima2,ima3,ima4,ima5] 
    st.image(images_on_page3, width = 150,caption = movie_names)


year = st.slider('Show me the trends of the year', 1940, 2020,step=20)
a11 = Image.open(str(year)+".png")
st.image(a11, use_column_width=True, caption = ["Trends"])




