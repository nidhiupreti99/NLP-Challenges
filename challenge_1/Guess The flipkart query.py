# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 23:59:02 2019

@author: Nidhi
"""

#import nltk
import numpy as np
import random
import string
output=[]
f=open('training.txt','r', errors='ignore').read().split('\n')
train_X=[]
train_Y=[]
for line in f:
    idx=line.find('\t')
    train_X.append(line[:idx])
    train_Y.append(line[idx+1:])
from sklearn.feature_extraction.text import TfidfVectorizer
TfidfVec=TfidfVectorizer(stop_words='english')

tfidf=TfidfVec.fit_transform(train_X)
#Y=TfidfVec.fit_transform(train_Y)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20,random_state=0)
#Y=np.asarray()
model.fit(tfidf, train_Y)
user_input=input()
product=[]

for i in range(int(user_input)):
    user_input1=input()
    product.append(user_input1)
output=[]
for line in product:
    
    output.append(model.predict(TfidfVec.transform([line])))
for out in output:
    print(out+'\n')
    
  