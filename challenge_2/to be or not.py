# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 01:56:44 2019

@author: Nidhi
"""
import nltk
output=['am','are','were','was','is','been','being','be']
user_input=input()
para=input()
count=0
i=0
idx=[]
for word in para.split(' '):
    i=i+1
    if word=='----':
        count=count+1
        idx.append(i)
i=0
word_dict={}
if int(count) == int(user_input):
    print('hello')
    for word in para.split(' '):
        
        word_dict[i]=word
        i=i+1

from nltk import pos_tag,word_tokenize
tagged=[]
c=0
present=0
past=0
text = word_tokenize(para)
tagged.append(nltk.pos_tag(text))
for items in tagged:
    for item in items:
        if item[1] in ['VBP','VBZ']:
            present=present+1
        if item[1] in ['VBD','VBN']:

            past=past+1
output=[]
i=0            
if past>present:
    tense='past'
else:
    tense='present'
if tense==str('past'):
    for i in idx:
        if word_dict[i-2][-1]=='s':
            output.append('were')
        if word_dict[i-2] in ['i','I']:
            output.append('was')
        if word_dict[i-2] in ['he', 'she','it', 'this','that']:
            output.append('was')
        if (pos_tag(word_dict[i-2]) in ['WP','WP$','WRB'] or word_dict[i-2] in ['how']) and word_dict[i] in ['he', 'she','it', 'this','that']:
            output.append('was')
        if word_dict[i-2] in ['they','their','you','we','these']:
            output.append('were')
        if (pos_tag(word_dict[i-2]) in ['WP','WP$','WRB'] or word_dict[i-2] in ['how']) and word_dict[i] in ['they','these']:
            output.append('were')
        if pos_tag(word_dict[i-2]) in ['NNP','NN']:
            output.append('was')
        if word_dict[i-2] in ['has','have','had','hasn\'t','haven\'t','hadn\'t']:
            output.append('been')
        if word_dict[i-2] in ['is','am','was','were','not']:
            output.append('being')
        if word_dict[i-2] in ['will','would','can','could','wouldn\'t','couldn\'t','should','shouldn\'t','may','might','to']:
            output.append('be')
if tense==str('present'):
    for i in idx:
        
        if word_dict[i-2][-1]=='s':
            output.append('are')
        if word_dict[i-2] in ['i','I']:
            output.append('am')
        if word_dict[i-2] in ['he','she','it','this','that','there']:
            output.append('is')
        if (pos_tag(word_dict[i-2]) in ['WP','WP$','WRB'] or word_dict[i-2] in ['how']) and word_dict[i] in ['he', 'she','it', 'this','that']:
            output.append('is')
        if pos_tag(word_dict[i-2]) in ['NNP','NN']:
            output.append('is')
        if word_dict[i-2] in ['they','their','you','we','these','those']:
            output.append('are')
        if (pos_tag(word_dict[i-2]) in ['WP','WP$','WRB'] or word_dict[i-2] in ['how']) and word_dict[i] in ['they','these','you']:
            output.append('are')
        if word_dict[i-2] in ['has','have','had','hasn\'t','haven\'t','hadn\'t']:
            output.append('been')
        if word_dict[i-2] in ['is','am','was','were','not']:
            output.append('being')
        if word_dict[i-2] in ['will','would','can','could','wouldn\'t','couldn\'t','should','shouldn\'t','may','might','to']:
            output.append('be')
            
     
      
       
            
            
        
for out in output:
    print(out+'\n')