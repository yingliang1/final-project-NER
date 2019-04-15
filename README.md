# final-project-NER
1. NLTK use nltk.py, and the test file is test.txt, the result file is test1_1.csv.
2. for StanfordNER implement, there need a port so we need use command line to implement, we should convert our path into nltk-stanford then 
install the setup.py first use 'python setup.py install', after install this file we need open stanford.py file and set the stanfor-ner jar 
into your own path. after these step finished, use stanford.py get the result use stanfordNER, and we need do some process for the result file 
like here I use untitled8.py to delete some special strings and use excel to split the string into type and Name-Entity, 
3. the final step after I got the result of compare.CSV, test1_1.CSV, test1_2.CSV file I use accu.py to calculate the accuracy.
