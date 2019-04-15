# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:58:53 2019

@author: liangying
"""

import re
import pandas as pd
import nltk


def parse_document(document):
   document = re.sub('\n', ' ', document)
   if isinstance(document, str):
       document = document
   else:
       raise ValueError('Document is not string!')
   document = document.strip()
   sentences = nltk.sent_tokenize(document)
   sentences = [sentence.strip() for sentence in sentences]
   return sentences


File = open("nono.txt", "w")
for line in open("test.txt"):
    sentences = parse_document(line)
   
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    ne_chunked_sents = [nltk.ne_chunk(tagged) for tagged in tagged_sentences]
    named_entities = []
    for ne_tagged_sentence in ne_chunked_sents:
        for tagged_tree in ne_tagged_sentence:
            if hasattr(tagged_tree, 'label'):
                entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) 
                entity_type = tagged_tree.label() 
                named_entities=((entity_type, entity_name))
                File.write(str(named_entities)+ "\n")
        File.write("0,0\n")
  
                   
    #entity_frame = pd.DataFrame(named_entities)
    #File.write(str(entity_frame)+ "\n")
    