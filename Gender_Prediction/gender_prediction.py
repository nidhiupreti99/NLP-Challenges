# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 23:00:56 2019

@author: Nidhi
"""

f=open('corpus4.txt','r',errors='ignore').read().split('\n')
user_input=input()
names=[]
for i in range(int(user_input)):
    name=input()
    names.append(name)
i=0
pos=[]
male=0
gender=[]
female=0
for name in names:
    for line in f:
        i=i+1
        for word in line.split(' '):
            
            if word==str(name):
                pos.append(i)
                
    for i in pos:
        for word in f[i-1].split(' '):
            word=word.lower()
            if word in ['he','his','him','he\'s','boy','male','man','son','sir','gentleman','mr.','mister']:
                male=male+1
            if word in ['she','her','female','girl','she\'s','hers','daughter','lady','ms.','mrs.','mistress']:
                female=female+1

                     
             
             
    if male>female:
        gender.append('Male')
    else:
        gender.append('Female')
    pos=[]
    male=0
    female=0
    i=0
          
for gender in gender:
    print(gender)
        
   
    
            
           
           

        
   
                

        
