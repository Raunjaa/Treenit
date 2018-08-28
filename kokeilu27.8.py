# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 18:22:50 2018

@author: jraunama
"""

import re

abbreviations = ('дв.', 'Д.')
text = ''.join(open('data/NovgoTest.txt', encoding= "UTF-8").readlines())
for sentence in text:
    sentences = re.split(r' *[\.\?!][\'"\)\]]* +', text)
    if not sentence.endswith(abbreviations)
print(sentences)

"""
from nltk import tokenize
file = open('data/NovgoTest.txt', encoding ="UTF-8")
text = file.read()
file.close()
print(tokenize.sent_tokenize(text))
"""