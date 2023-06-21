

import requests
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession
import numpy as np
from fake_useragent import UserAgent
from urllib.request import Request, urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.data import url2pathname
import warnings
warnings.filterwarnings("ignore")
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *

from bs4 import BeautifulSoup
from nltk.tokenize import  word_tokenize
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords

import nltk

import logging #built in module in python used for logging msg from the program
import sys
args = sys.argv
logger = logging.getLogger() #object from the logging and the function returns the main entry point for the logger
# logger.setLevel(args[1] if args[1].strip() else logging.INFO)
logger.setLevel(args[1] if len(args) > 1 and args[1].strip() else logging.INFO) # sets logging level for the logger

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                              '%m-%d-%Y %H:%M:%S')  #format object is created to be able to identify the format of the msg

stdout_handler = logging.StreamHandler(sys.stdout) #this is where the printing happens in the console
stdout_handler.setLevel(args[1] if len(args) > 1 and args[1].strip() else logging.INFO)

stdout_handler.setFormatter(formatter)#specifies the fromat of the log msg that will be displayed

file_handler = logging.FileHandler('logs.log') #msg from the log is directed to this file
file_handler.setLevel(logging.DEBUG) #this line sets the logging level for the file, logging.DEBUG: lowest level which will capture all log msgs
file_handler.setFormatter(formatter) #specifies format of the log msg sent to the file

logger.addHandler(file_handler)# it ensures that log messages are also written to the 'logs.log' file.
logger.addHandler(stdout_handler) # This line adds the stdout handler to the logger. It ensures that log messages are displayed in the console as well.
nltk.download('stopwords', quiet=True) #(quiet=true)suppresses the progress bar and output during the download process.
nltk.download('punkt', quiet=True)

stop_words = set(stopwords.words('arabic')) 
stop_words.update(['le', 'eu', 'span', 'ago', 'pp', 'ue', 'div', 'src', 'page', 'egp', 'url', 'cdn', 'alt', 'com', 'net', 'org', 'cdn', 'img', 'google','eg','usd','http','https','net','us','eg'])




import mysql.connector

# Connect to the database
mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seopro"
)

# Create a cursor object
mycursor = mysql.cursor()

# Execute an SQL query to select the last row from the table
mycursor.execute("SELECT uid, niche FROM given_niche_ar ORDER BY id DESC LIMIT 1")

# Fetch the last row from the table
niche_arr = mycursor.fetchone()

# # Convert niche[0] to a string
# niche= str(niche_arr[0])

# # Print the last row as a string
# logger.info(niche)

# Extract the id and niche values from the row
uid = niche_arr[0]
niche = niche_arr[1]

# Print the niche and id values
# logger.info(niche)
# logger.info(uid)

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
        # logger.info(e)
        return e

def scrape_google(query): #the function where we actually scrape google
    
    # query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    links = list(response.html.absolute_links)  
    #extracts all the absolute links from the HTML response using the .absolute_links property. It converts the set of links into a list and assigns it to the links variable.
    #links to avoid:
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.'
                      )
    # google_domains = ('https://www.google.', 
    #                   'https://google.')
    for url in links[:]: # :this is to make a copy of links to avoid any potential probs
        if url.startswith(google_domains):  # if one of the links outputted is in google domain, remove those links
            links.remove(url)

    return links
links = scrape_google(niche) #
# for link in links:
#   logger.info(link)



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
text=[]
for i in links:
  t=get_text(i)
  if t:
    text.append(t)

    word_tokens = word_tokenize(t)
    filtered_sentence = [w for w in word_tokens if not w.lower() in word_tokens]






stop_words = set(nltk.corpus.stopwords.words("arabic"))
from nltk.stem.isri import ISRIStemmer
import re
st = ISRIStemmer()

# w=filtered_sentence
for word in filtered_sentence:
    if word not  in stop_words:
    #won't take the input correctly, input = output of tokenization# w= 'كلمات'
        # logger.info(word+"-->"+st.stem(word))
        u=st.stem(word)


    

def tf_idf_analysis(keyword):
    v = TfidfVectorizer(min_df=1,analyzer='word',ngram_range=(1,2),stop_words=list(stop_words))
    x = v.fit_transform(text)
    f = pd.DataFrame(x.toarray(), columns = v.get_feature_names_out())
    d=pd.concat([pd.DataFrame(f.mean(axis=0)),pd.DataFrame(f.max(axis=0))],axis=1)
    tf=pd.DataFrame((f>0).sum(axis=0))
    d=d.reset_index().merge(tf.reset_index(),on='index',how='left')
    d.columns=['word','average_tfidf','max_tfidf','frequency']
    d['frequency']=round((d['frequency']/len(text))*100)
    d['max_tfidf'] = d['max_tfidf'].round(3)
    d['average_tfidf'] = d['average_tfidf'].round(3)

    d= d[d['word'].str.isalpha()].sort_values('frequency',ascending=False).head(35)
    
    return d

import requests


# Call the tf_idf_analysis function and store the output in a DataFrame variable
output_df = tf_idf_analysis(u)
# logger.info (output_df)
# Convert the DataFrame to a dictionary
output_dict = output_df.to_dict('records')

sql = "INSERT INTO keyword_ar (word, average_tfidf, max_tfidf, frequency, niche, uid) VALUES (%s, %s, %s, %s, %s, %s)"
for row in output_dict:
    val = (row['word'], row['average_tfidf'], row['max_tfidf'], row['frequency'], niche, uid)
    mycursor.execute(sql, val)


mysql.commit()

# Print a message to confirm that the data has been saved
# logger.info("Data has been saved to the database.")
print("success")





