# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:47:25 2019

@author: Nidhi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:46:36 2018

@author: Nidhi
"""

import nltk
import numpy as np
import random
import string

f=open('all/biology.csv','r', errors='ignore')
f1=open('all/cooking.csv','r', errors='ignore')
f2=open('all/crypto.csv','r', errors='ignore')
f3=open('all/diy.csv','r',errors='ignore')
f4=open('all/robotics.csv','r', errors='ignore')
f5=open('all/travel.csv','r', errors='ignore')

raw=f.read().lower()
raw1=f1.read().lower()
raw2=f2.read().lower()
raw3=f3.read().lower()
raw4=f4.read().lower()
raw5=f5.read().lower()

"""raw=raw.lower()"""
tags=['cooking','biology','crypto','diy','robotics','travel','physics']
nltk.download('punkt')
nltk.download('wordnet')
sent_tokens=nltk.sent_tokenize(raw+raw1+raw2+raw3+raw4+raw5)
word_tokens=nltk.word_tokenize(raw+raw1+raw2+raw3+raw4+raw5)

lemmer=nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict=dict((ord(punct),None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
question=input()
tags.append(question)
TfidfVec=TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
tfidf=TfidfVec.fit_transform(sent_tokens)
vals=cosine_similarity(tfidf[-1],tfidf)
idx=vals.argsort()[0][2]
flat=vals.flatten()
flat.sort()   
req_idf=flat[-2]
print(tags[idx])

