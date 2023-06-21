import urllib
# %pip install requests_html
import requests
# !pip install requests
from requests_html import HTMLSession
import mysql.connector

# Connect to the database
# mysql = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="seopro"
# )

# # Create a cursor object
# mycursor = mysql.cursor()

# # Execute an SQL query to select the last row from the table
# mycursor.execute("SELECT uid, niche FROM given_niche_ar ORDER BY id DESC LIMIT 1")

# # Fetch the last row from the table
# niche_arr = mycursor.fetchone()

# # # Convert niche[0] to a string
# # niche= str(niche_arr[0])

# # # Print the last row as a string
# # print(niche)

# # Extract the id and niche values from the row
# uid = niche_arr[0]
# niche = niche_arr[1]

# # Print the niche and id values
# print(niche)
# print(uid)
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
    
    # query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
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

links = scrape_google("سيارات")
for link in links:
  print(link)

from nltk.tokenize import  word_tokenize
import nltk
nltk.download('punkt')
# # EXAMPLE_TEXT = """
# # أبو عبد الله محمد بن موسى الخوارزمي عالم رياضيات وفلك
# # وجغرافيا مسلم. يكنى باسم الخوارزمي وأبي جعفر. قيل أنه ولد حوالي 164هـ 781م (وهو غير مؤكد) وقيل أنه توفي بعد 232هـ أي (بعد 847م). يعتبر
# # من أوائل علماء الرياضيات المسلمين حيث ساهمت أعماله بدور كبير في تقدم الرياضيات في عصره. اتصل بالخليفة العباسي المأمون وعمل في بيت الحكمة في 
# # بغداد وكسب ثقة الخليفة إذ ولاه المأمون بيت الحكمة كما عهد إليه برسم خارطة للأرض عمل فيها أكثر من سبعين جغرافيا. قبل وفاته في 850 م/232 هـ
# # كان الخوارزمي قد ترك العديد من المؤلفات في علوم الرياضيات والفلك والجغرافيا ومن أهمها

# # """
# EXAMPLE_TEXT=links
# print(word_tokenize(EXAMPLE_TEXT))

# links=scrape_google('cars')
import numpy as np
from fake_useragent import UserAgent
import re
from urllib.request import Request, urlopen
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import math

from bs4 import BeautifulSoup

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
# word_tokens = 

    filtered_sentence = [w for w in word_tokens]

    # print(word_tokens)
    # print('---------------------------------')
    # print(filtered_sentence)

    filtered_sentence = [w for w in word_tokens if not w in word_tokens]

    # print(word_tokens)
    # print('---------------------------------')
    # print(filtered_sentence)
    filtered_sentence = [w for w in word_tokens if not w.lower() in word_tokens]

    print(word_tokens)
    print('---------------------------------')
    print(filtered_sentence)
stop_words = set(nltk.corpus.stopwords.words("arabic"))
from nltk.stem.isri import ISRIStemmer
import re
st = ISRIStemmer()
u=[]
# w=filtered_sentence
for word in word_tokens:
    if word not  in stop_words:
    #won't take the input correctly, input = output of tokenization# w= 'كلمات'
        print(word+"-->"+st.stem(word))

        u.append(st.stem(word))
        # print('LAAAAAAAAA')
        # print(u)

# import nltk

# from nltk.stem.porter import *
# p_stemmer = PorterStemmer()




# for word in  filtered_sentence:
#     print(word+' --> '+p_stemmer.stem(word))

# from nltk.stem.snowball import SnowballStemmer
# s_stemmer = SnowballStemmer(language='english')



# for word in filtered_sentence:
#     print(word+' --> '+s_stemmer.stem(word))
# u=p_stemmer.stem(word)

# import fasttext.util
# import fasttext

# # Download the pre-trained Arabic word vectors
# fasttext.util.download_model('ar', if_exists='ignore')  # Download only if not already downloaded

# # Load the pre-trained word vectors
# model = fasttext.load_model('cc.ar.300.bin')

# # Define a function to find alternative words
# def find_alternative_words(word, topn=6):
#     # Find the most similar words based on cosine similarity
#     alternative_words = model.get_nearest_neighbors(word, k=topn)

#     # Extract the alternative words
#     alternative_words = [alt_word[1] for alt_word in alternative_words]

#     return alternative_words

# # Example usage
# input_word = u
# # for word in input_word:
# alternative_words = find_alternative_words(input_word)
# # for word in input_word:
# # Print the alternative words
# print(f"Alternative words for '{input_word}':")
# for i, alt_word in enumerate(alternative_words, start=1):
#     print( f"{i}. {alt_word}")



# import fasttext.util
# import fasttext

# # Download the pre-trained Arabic word vectors
# fasttext.util.download_model('ar', if_exists='ignore')  # Download only if not already downloaded

# # Load the pre-trained word vectors
# model = fasttext.load_model('cc.ar.300.bin')

# # Define a function to find alternative words
# def find_alternative_words(u, topn=6):
#     # Find the most similar words based on cosine similarity
#     alternative_words = model.get_nearest_neighbors(u, k=topn)

#     # Extract the alternative words
#     alternative_words = [alt_word[1] for alt_word in alternative_words]

#     return alternative_words

# # Example usage
# # x=[u]
# # for item in x:
# #     print(item)
# # print(x)
# # input_words = u  # Replace with your list of words
# x=[]
# for word in u:
#     alternative_words = find_alternative_words(word)
#     print(word)
#     # Print the alternative words
#     print(f"Alternative words for '{word}':")
#     for i, alt_word in enumerate(alternative_words, start=1):
#         print(f"{i}. {alt_word}")
#     print()  # Add a newline after each word's alternative words


#AHAHAHAHAHAAHAHHAHAHAHAAHAAHAHAHHAHAHAHHAAHHAHAAHAHAH#
import fasttext.util
import fasttext
import pandas as pd
# Download the pre-trained Arabic word vectors
fasttext.util.download_model('ar', if_exists='ignore')  # Download only if not already downloaded

# Load the pre-trained word vectors

# df = pd.read_csv("F:/last semester/final project/seopro/python/arabic_dataset_classifiction.csv")
model = fasttext.load_model('cc.ar.300.bin')
# model = fasttext.load_model(model)
# Define a function to find alternative words
def find_alternative_words(words, topn=6):
    alternative_words_list = []
    for word in words:
        # Find the most similar words based on cosine similarity
        alternative_words = model.get_nearest_neighbors(word, k=topn)

        # Extract the alternative words
        alternative_words = [alt_word[1] for alt_word in alternative_words]

        alternative_words_list.append(alternative_words)

    return alternative_words_list

# Example usage


print(u)
print('kaksksk')
# for word in u:
#     input_words.append(word)  # Replace with your list of words
# print(input_words)
alternative_words_list = find_alternative_words(u)

# Print the alternative words for each word
for i, word in enumerate(u):
    print(f"Alternative words for '{word}':")
    alternative_words = alternative_words_list[i]
    for j, alt_word in enumerate(alternative_words, start=1):
        
        print(f"{j}. {alt_word}")
        # print(alt_word)
    print()

# import fasttext.util
# import fasttext
# import pandas as pd

# # Download the pre-trained Arabic word vectors
# fasttext.util.download_model('ar', if_exists='ignore')  # Download only if not already downloaded

# # Load the pre-trained word vectors
# model = fasttext.load_model('cc.ar.300.bin')

# # Read the DataFrame from the CSV file
# df = pd.read_csv("F:/last semester/final project/seopro/python/arabic_dataset_classifiction.csv")

# # Extract the Arabic words from the DataFrame
# arabic_words = df['word'].tolist()

# # Define a function to find better alternative words for Arabic words
# def find_better_alternatives(word, topn=6):
#     # Find the most similar words based on cosine similarity
#     alternative_words = model.get_nearest_neighbors(word, k=topn)
    
#     # Extract the alternative words
#     alternative_words = [alt_word[1] for alt_word in alternative_words]
    
#     return alternative_words

# # Iterate over the Arabic words and find better alternative words
# for word in arabic_words:
#     alternative_words = find_better_alternatives(u)
    
#     # Print the original word and its alternative words
#     print(f"Original word: {word}")
#     print(f"Alternative words: {', '.join(alternative_words)}")
#     print()


# import pandas as pd

# # Read the DataFrame from the CSV file
# df = pd.read_csv("F:/last semester/final project/seopro/python/arabic_dataset_classifiction.csv")

# # Define a function to find better alternative words for a given word
# def find_better_alternatives(word, topn=6):
#     # Filter the DataFrame for words similar to the input word
#     similar_words = df[df['word'].str.startswith(word, na=False)]
    
#     # Sort the similar words by their frequency in descending order
#     similar_words = similar_words.sort_values('frequency', ascending=False)
    
#     # Get the top n alternative words
#     alternative_words = similar_words['alternative_word'].head(topn).tolist()
    
#     return alternative_words

# # Prompt the user to enter a word
# input_word = u

# # Check if the word exists in the dictionary
# if input_word in df['word'].values:
#     # Find better alternative words for the input word
#     alternative_words = find_better_alternatives(input_word)
    
#     # Print the alternative words
#     print(f"Alternative words for '{input_word}':")
#     for i, alt_word in enumerate(alternative_words, start=1):
#         print(f"{i}. {alt_word}")
# else:
#     print(f"The word '{input_word}' is not found in the dictionary.")



# import pandas as pd

# def find_better_alternatives(word, df, topn=5):
#     filtered_words = df[df['word'].str.startswith(word)]['alternative_word']
#     return filtered_words.head(topn).tolist()

# # Read the CSV file into a DataFrame
# df = pd.read_csv("F:/last semester/final project/seopro/python/arabic_dataset_classifiction.csv")

# # Prompt the user to enter a word
# input_word = u

# # Find better alternative words
# alternative_words = find_better_alternatives(input_word, df)

# # Print the alternative words
# print(f"Better alternative words for '{input_word}':")
# for i, alt_word in enumerate(alternative_words, start=1):
#     print(f"{i}. {alt_word}")


# import pandas as pd

# def find_better_alternatives(word, df, topn=5):
#     filtered_words = df[df['YOUR_WORD_COLUMN_NAME'].str.startswith(word)]['alternative_word']
#     return filtered_words.head(topn).tolist()

# # Read the CSV file into a DataFrame
# df = pd.read_csv("F:/last semester/final project/seopro/python/arabic_dataset_classifiction.csv")

# # Prompt the user to enter a word
# input_word = input("Enter a word in Arabic: ")

# # Find better alternative words
# alternative_words = find_better_alternatives(input_word, df)

# # Print the alternative words
# print(f"Better alternative words for '{input_word}':")
# for i, alt_word in enumerate(alternative_words, start=1):
#     print(f"{i}. {alt_word}")
