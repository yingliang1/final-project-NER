# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 21:31:42 2019

@author: liangying
"""
import difflib
import numpy as np
import pandas as pd

stanforddata=pd.read_csv('E:/test1_1.csv')
stanfordx=np.array(stanforddata)
stanfordtype=stanfordx[:,0]
stanfordvalue=stanfordx[:,1]
STANFORDORG=[]
STANFORDLOC=[]
STANFORDPER=[]
for i in range(len(stanfordx)):
    if stanfordtype[i]=='ORGANIZATION':
        STANFORDORG.append(stanfordvalue[i])
    elif stanfordtype[i]=='LOCATION    ':
        STANFORDLOC.append(stanfordvalue[i])
    elif stanfordtype[i]=='PERSON      ':
        STANFORDPER.append(stanfordvalue[i])



comparedata=pd.read_csv('E:/compare.csv')
comparex=np.array(comparedata)
comparetype=comparex[:,0]
comparevalue=comparex[:,1]
COMORG=[]
COMLOC=[]
COMPER=[]
for i in range(len(comparex)):
    if comparetype[i]=='ORGANIZATION':
        COMORG.append(comparevalue[i])
    elif comparetype[i]=='LOCATION':
        COMLOC.append(comparevalue[i])
    elif comparetype[i]=='LOCATION    ':
        COMLOC.append(comparevalue[i])
    elif comparetype[i]=='PERSON      ':
        COMPER.append(comparevalue[i])
    elif comparetype[i]=='PERSON':
        COMPER.append(comparevalue[i])
        
nltkdata=pd.read_csv('E:/test1_2.csv')
nltkx=np.array(nltkdata)
nltktype=nltkx[:,0]
nltkvalue=nltkx[:,1]
NLTKORG=[]
NLTKLOC=[]
NLTKPER=[]
for i in range(len(nltkx)):
    if nltktype[i]=='ORGANIZATION':
        NLTKORG.append(nltkvalue[i])
    elif nltktype[i]=='GPE':
        NLTKLOC.append(nltkvalue[i])
    elif nltktype[i]=='FACILITY':
        NLTKLOC.append(nltkvalue[i])
    elif nltktype[i]=='PERSON':
        NLTKPER.append(nltkvalue[i])        


a=0
for i in range(len(COMORG)):
    for j in range(len(STANFORDORG)):
        seq = difflib.SequenceMatcher(None, COMORG[i], STANFORDORG[j])
        ratio = seq.ratio()
        if (ratio>0.8):
            a=a+1
ACCUORG=a/len(COMORG)
#print(ACCUORG)

b=0
for i in range(len(COMLOC)):
    for j in range(len(STANFORDLOC)):
        seq = difflib.SequenceMatcher(None, COMLOC[i], STANFORDLOC[j])
        ratio = seq.ratio()
        if (ratio>0.8):
            b=b+1
ACCULOC=b/len(COMLOC)
#print(ACCULOC)

c=0
for i in range(len(COMPER)):
    for j in range(len(STANFORDPER)):
        seq = difflib.SequenceMatcher(None, COMPER[i], STANFORDPER[j])
        ratio = seq.ratio()
        if (ratio>0.8):
            c=c+1
ACCUPER=c/len(COMPER)
#print(ACCUPER)
print((ACCUORG+ACCULOC+ACCUPER)/3)


a1=0
for i in range(len(COMORG)):
    for j in range(len(NLTKORG)):
        seq = difflib.SequenceMatcher(None, COMORG[i], NLTKORG[j])
        ratio = seq.ratio()
        if (ratio>0.8):
            a1=a1+1
ACCUORG1=a1/len(COMORG)
#print(ACCUORG)

b1=0
for i in range(len(COMLOC)):
    for j in range(len(NLTKLOC)):
        seq = difflib.SequenceMatcher(None, COMLOC[i], NLTKLOC[j])
        ratio = seq.ratio()
        if (ratio>0.8):
            b1=b1+1
ACCULOC1=b/len(COMLOC)
#print(ACCULOC)

c1=0
for i in range(len(COMPER)):
    for j in range(len(NLTKPER)):
        seq = difflib.SequenceMatcher(None, COMPER[i], NLTKPER[j])
        ratio = seq.ratio()
        if (ratio>0.8):
            c1=c1+1
ACCUPER1=c1/len(COMPER)
#print(ACCUPER)
print((ACCUORG1+ACCULOC1+ACCUPER1)/3)





            


