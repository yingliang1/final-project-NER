# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 17:37:22 2019

@author: liangying
"""
import re
File = open("nltk1.txt", "w")
for line in open("nltk.txt"):
    line = re.sub("[('')]", '', line)
    File.write(str(line))
    print (line)


