# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 14:47:09 2019

@author: Nidhi
"""

user_input=input()
user_input=2*int(user_input)+1
flag=0
import nltk
set_A=[]
set_B=[]
nltk.download('punkt')
nltk.download('wordnet')
lemmer=nltk.stem.WordNetLemmatizer()


for i in range(int(user_input)):
    
    text=input()
    if text!='*****' and flag==0:
        text=text.lower()
        set_A.append(text)
    if text =='*****':
        flag=1
    if flag==1:
        text=text.lower()
        set_B.append(text)
set_B=set_B[1:]
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
TfidfVec=TfidfVectorizer()
i=0
dict={}
for item in set_A:
    i=i+1
    set_B.append(item)
    tfidf=TfidfVec.fit_transform(set_B)
    vals=cosine_similarity(tfidf[-1],tfidf)
    index=vals.argsort()[0][-2]
    dict[index]=i
    set_B.remove(item)
for key,value in dict.items():
    print(value)
