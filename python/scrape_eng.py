# %pip install pandas
# %pip install requests_html
# %pip install scikit-learn
# %pip install nltk
# %pip install mysql-connector-python

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
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
from urllib.request import Request, urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.data import url2pathname
import warnings
warnings.filterwarnings("ignore")
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *

from bs4 import BeautifulSoup

from nltk.corpus import stopwords

import nltk

import logging
import sys
args = sys.argv
logger = logging.getLogger()
# logger.setLevel(args[1] if args[1].strip() else logging.INFO)
logger.setLevel(args[1] if len(args) > 1 and args[1].strip() else logging.INFO)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s', 
                              '%m-%d-%Y %H:%M:%S')

stdout_handler = logging.StreamHandler(sys.stdout)
# stdout_handler.setLevel(args[1] if args[1].strip() else logging.INFO)
stdout_handler.setLevel(args[1] if len(args) > 1 and args[1].strip() else logging.INFO)
stdout_handler.setFormatter(formatter)

file_handler = logging.FileHandler('logs.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

# nltk.download('stopwords')
# nltk.download('punkt')
import mysql.connector
# # Connect to the database
# mysql = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="seopro"
# )
# # Create a cursor object
# mycursor = mysql.cursor()
# # Execute an SQL query to select the last row from the table
# mycursor.execute("SELECT uid,url FROM given_url ORDER BY id DESC LIMIT 1")
# # Fetch the last row from the table
# url_arr = mycursor.fetchone()
# # Extract the id and niche values from the row
# uid = url_arr[0]
# url = url_arr[1]
# # Print the niche and id values
# print(url)
# print(uid)
import time
t0=time.time()

mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="seopro"
)
# Create a cursor object
mycursor = mysql.cursor()
# Execute an SQL query to select the last row from the table
mycursor.execute("SELECT uid,url FROM given_url ORDER BY id DESC LIMIT 1")
# Fetch the last row from the table
url_arr = mycursor.fetchone()
# Extract the id and niche values from the row
uid = url_arr[0]
url = url_arr[1]
# Print the niche and id values
logger.info(url)
logger.info(uid)

def get_text_from_url(url, words_per_line=5):
    # Send a GET request to the URL and retrieve its HTML content
    response = requests.get(url)
    html_content = response.text
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract the text content you need from the parsed HTML content
    output = soup.get_text()
    # Remove extra spaces and newlines from the text
    output = ' '.join(output.split())

    # Insert a newline after a certain number of words
    words = output.split()
    output = ''
    for i in range(len(words)):
        output += words[i] + ' '
        if (i + 1) % words_per_line == 0:
            output += '\n'

    return output

# Call the get_text_from_url function
# url = "https://choconutsworld.com/"
output = get_text_from_url(url, words_per_line=5)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in output.lower().split() if word not in stop_words]
    
# Tokenize the text into words
words = word_tokenize(' '.join(filtered_words))
logger.info(words)

    # Stem the words using Porter Stemmer
    # stemmer = PorterStemmer()
    # stemmed_words = [stemmer.stem(word) for word in words]
    
    # # Join the stemmed words into a string
    # stemmed_text = ' '.join(stemmed_words)
    
    # # Return the preprocessed text
    # return stemmed_text

# print (stemmed_text)



# print(stemmed_words)
# print(output)
# Call the get_text_from_url function

# sql = "INSERT INTO synonyms (words,url, uid) VALUES (%s, %s, %s)"
# # for row in output_df:
# val = (output_df, url, uid)
# mycursor.execute(sql, val)
# mysql.commit()
# # Print a message to confirm that the data has been saved
# print("Data has been saved to the database.")
import nltk
# !pip install gensim
import gensim.downloader as api
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
# Download the pre-trained Word2Vec model
model = api.load('word2vec-google-news-300')
# import nltk
# import gensim.downloader as api
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer
# nltk.download('wordnet')
# # Download the pre-trained Word2Vec model
# model = api.load('word2vec-google-news-300')

word_list = words

# # Load stop words and create a lemmatizer object
# stop_words = stopwords.words('english')
# lemmatizer = WordNetLemmatizer()

# # Define a function to preprocess text
# def preprocess(text):
#     tokens = nltk.word_tokenize(text.lower())
#     tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
#     tokens = [lemmatizer.lemmatize(token) for token in tokens]
#     return tokens

# # Preprocess the words in the list
# word_list_preprocessed = [preprocess(word) for word in word_list]

# Define a function to find the alternative words for a word with high Word2Vec similarity scores
def find_high_similarity_alternative_words(word_list, threshold=0.6):
    alternatives = []
    if word not in model:
        return alternatives
    for w, score in model.most_similar(word):
        if score > threshold:
            alternatives.append(w)
    return alternatives

# Find the higher ranking alternative words for each word in the list
alternatives_dict = {}
for word in word_list:
    alternatives = find_high_similarity_alternative_words(word)
    alternatives_dict[word] = alternatives

# Print the higher ranking alternative words for each word in the list
for word, alternatives in alternatives_dict.items():
    logger.info(word + ':', alternatives)
    sql = "INSERT INTO synonyms (words_before,words_after,url, uid) VALUES (%s,%s, %s, %s)"
# for row in output_df:
    val = (word,str(alternatives), url, uid)
    mycursor.execute(sql, val)
    mysql.commit()
# Print a message to confirm that the data has been saved
logger.info("Data has been saved to the database.")
logger.info(time.time()-t0)
print("success")