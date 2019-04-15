# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:37:24 2019

@author: liangying
"""

from nltk.tag import StanfordNERTagger

# Optional
import os
java_path = "C:/Program Files/Java/jdk-10.0.2/bin/java.exe"
os.environ['JAVA_HOME'] = java_path
File = open("nono.txt", "w")
eng_tagger = StanfordNERTagger(model_filename=r'E:\StanfordNLTK\classifiers\english.all.3class.distsim.crf.ser.gz',path_to_jar=r'E:\StanfordNLTK\stanford-ner.jar')
for line in open("test.txt"):
    ners=eng_tagger.tag(line.split())
    from itertools import groupby
    for tag, chunk in groupby(ners, lambda x:x[1]):
        if tag != "O":
           test= "%-12s"%tag, " ".join(w for w, t in chunk)
           #File = open("nono.txt", "w")
           File.write(str(test)+"\n")
    File.write("0,0\n")
   
    

