
import streamlit as st
import streamlit.components.v1 as components
import numpy as np
from PIL import Image
import requests
import urllib.request
import searchquery
import pandas as pd
import matplotlib.pyplot as plt
from gensim import corpora,models, similarities
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
import time
import pickle
import string
from gensim.models import CoherenceModel

st.set_page_config(page_title="Movie Recommendation", layout="wide")
st. markdown("<h2 style='text-align: center; color: black;'>Movie Recommendation</h2>", unsafe_allow_html=True)
c1, c2 = st.columns([2,2])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row; justify-content: flex-start;} </style>', unsafe_allow_html=True)
# st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-size:1rem; padding-left:2px; padding-right:10px;}</style>', unsafe_allow_html=True)
st.write('<style>div.block-container{padding-top:6rem;}</style>', unsafe_allow_html=True)





@st.cache
def lda(title2):
    nltk.download('stopwords')
    nltk.download('wordnet')

    test = searchquery.search_query("LDAModel.model","lda_dict","lda_corpus","movie_data_nn.csv","NN_lda.csv")
    test.load_info()
    a,b = test.search(title2)
    return a,b
@st.cache
def dataread():
    data = pd.read_csv("movie_data_with_nn_poster.csv")
    return data

with c1:
    st.write('Enter keywords related to plot')
    title2 = st.text_input('Plot', 'Romantic Love')
    st.write('Movies whose plots are similar to ',title2,':')
    a,b = lda(title2)    
    urllib.request.urlretrieve(b[0],'im1.png')
    im1 = Image.open("im1.png")
    urllib.request.urlretrieve(b[1],'im2.png')
    im2 = Image.open("im2.png")
    urllib.request.urlretrieve(b[2],'im3.png')
    im3 = Image.open("im3.png")
    # urllib.request.urlretrieve(b[3],'im4.png')
    # im4 = Image.open("im4.png")
    urllib.request.urlretrieve(b[4],'im5.png')
    im5 = Image.open("im5.png")
    urllib.request.urlretrieve(b[5],'im6.png')
    im6 = Image.open("im6.png")
    images_on_page2= [im1,im2,im3,im5,im6] 
    st.image(images_on_page2, width = 150,caption = [a[0],a[1],a[2],a[4],a[5]])

with c2:
    st.write('Enter Movie Title')
    data = dataread() 
    option = st.selectbox('Movie title',tuple(list(data['Title'])))
    id = data.index[data['Title'] == option].tolist()[0]
    Movies = data.loc[id].at["5 Nearest"]  
    movie_names = Movies.split(",") 
    poster_links = data.loc[id].at["Poster_nn"]
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


html_temp =""" <div class='tableauPlaceholder' id='viz1650746687657' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Mo&#47;MovieRunningChart&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='MovieRunningChart&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Mo&#47;MovieRunningChart&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1650746687657');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1000px';vizElement.style.height='827px';} else { vizElement.style.width='100%';vizElement.style.height='727px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"""
components.html(html_temp,width = 4000,height = 700)

