# NLP - Text Parsing, Stemming, Stopword removal, Term Frequency Matrix

import re
import string
import pandas as pd
import os

import nltk.corpus
from nltk.corpus.reader.plaintext import PlaintextCorpusReader

from nltk.corpus import stopwords 
nltk.download('stopwords')
from nltk.tokenize import word_tokenize 

import nltk
nltk.download('punkt')

from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

# read a file MLK_speech.txt
text="/@@@111Faculty      of Economic Sciences,,,, as an independent unit of the University of Warsaw, affirms its commitment to basic goals and values specified in the Mission Statement of the University of Warsaw. In regard to the way in which the mission of our Alma Mater refers to the discipline represented by the Faculty of Economic Sciences, we define the following goal and value as our priorities of special importance: unity of research and teaching is the foundation of the activities at the Faculty of Economic Sciences."
print(text)


# Text parsing 

# Preliminary cleaning

# replace special characters from text. 
# substituting "/", "@" and "|" and others by a space.
text_clean = re.sub('[^a-zA-Z0-9 \n\.]', '', text)
print(text_clean)

# Cleaning text
    
# a) to remove unnecessary spaces, punctuation and numbers

# remove unnecessary spaces
text_cleaner = re.sub(' +', ' ', text_clean)

# remove unnecessary punctuation - already done above using regex, you may try to define punctuation manually
re.sub(r'[^\w\s]','', text)

# remove unnecessary numbers
text_cleaner = re.sub('\d', '', text_cleaner)
print(text_cleaner)


# b) change letters to lower case

# change to lowercase
print(text_cleaner.lower())


# Stopword removal 

# In the case of "stopwords" in the package tm 
# supported languages are: Danish, Dutch,
# English, Finnish, French, German, Hungarian, Italian,
# Norwegian, Portuguese, Russian, Spanish and Swedish.
# Language names are case-sensitive.
 

# remove English stopwords
stop_words = set(stopwords.words('english')) 
word_tokens = word_tokenize(text_cleaner) 

filtered_sentence = [w for w in word_tokens if not w in stop_words] 
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence) 



# if necessaary: remove your own stopwords - as a vector of words:
stop_words_lst = ['a']

for w in stop_words_lst:
    pattern = r'\b'+w+r'\b'
    filtered_text = re.sub(pattern, '', text_cleaner)
    print (filtered_text)


# Stemming 


# Stemming reduces words to their root form
# For example, the reduction of words "move", "moved" 
# and "movement" to the core "move".


# stem document
ps = PorterStemmer() 
   
words = word_tokenize(text_cleaner) 
   
for w in words: 
    print(w, " : ", ps.stem(w)) 
    
    

# Term frequency matrix


wordlist = text_cleaner.split()

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + text_cleaner +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))
