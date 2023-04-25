from flask import Flask
import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import numpy as np
from fake_useragent import UserAgent
import re
from urllib.request import Request, urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import math

from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/tfidf')
def get_text(url):
    try:
        req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req,timeout=5).read()
        soup = BeautifulSoup(webpage, "html.parser")
        texts = soup.findAll(text=True)
        res=u" ".join(t.strip() for t in texts if t.parent.name not in ['style', 'script', 'head', 'title', 'meta', '[document]'])
        return(res)
    except:
        return False
get_text('https://en.wikipedia.org/wiki/Machine_learning')
def get_source(url):
    """Return the source code for the provided URL. 
    Args: 
        url (string): URL of the page to scrape.
    Returns:
        response (object): HTTP response object from requests_html. 
    """
    try:
        session = HTMLSession()
        response = session.get(url)
        return response
    except requests.exceptions.RequestException as e:
        print(e)
def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)
    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links
scrape_google("cars")
from nltk.data import url2pathname
import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))
print(len(stop_words))
stop_words

import nltk
nltk.download('punkt')
# example_sent = get_text('https://en.wikipedia.org/wiki/Machine_learning')
stop_words = set(stopwords.words('english'))

links=scrape_google('cars')

text=[]
for i in links:
  t=get_text(i)
  if t:
    text.append(t)

    word_tokens = word_tokenize(t)
# word_tokens = 

    filtered_sentence = [w for w in word_tokens]

    # print(word_tokens)
    # print('---------------------------------')
    # print(filtered_sentence)

    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    # print(word_tokens)
    # print('---------------------------------')
    # print(filtered_sentence)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    print(word_tokens)
    print('---------------------------------')
    print(filtered_sentence)
import nltk

from nltk.stem.porter import *
p_stemmer = PorterStemmer()




for word in  filtered_sentence:
    print(word+' --> '+p_stemmer.stem(word))

from nltk.stem.snowball import SnowballStemmer
s_stemmer = SnowballStemmer(language='english')



for word in filtered_sentence:
    print(word+' --> '+s_stemmer.stem(word))
    u=p_stemmer.stem(word)

    

def tf_idf_analysis(keyword):
  v = TfidfVectorizer(min_df=1,analyzer='word',ngram_range=(1,2),stop_words=stop_words)
  x = v.fit_transform(text)

  f = pd.DataFrame(x.toarray(), columns = v.get_feature_names())
  d=pd.concat([pd.DataFrame(f.mean(axis=0)),pd.DataFrame(f.max(axis=0))],axis=1)
    
    
  tf=pd.DataFrame((f>0).sum(axis=0))


  d=d.reset_index().merge(tf.reset_index(),on='index',how='left')

  d.columns=['word','average_tfidf','max_tfidf','frequency']

  d['frequency']=round((d['frequency']/len(text))*100)

  return(d)


x= tf_idf_analysis(u)
x[x['word'].str.isalpha()].sort_values('max_tfidf',ascending=False).head(35)
# print(x)



if __name__ == "__main__":
    app.run(debug=True,port=4000)
    
 
