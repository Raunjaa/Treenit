# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:10:18 2018
*Иго
@author: jraunama
"""


file = open('data/NovgoTest.txt', encoding ="UTF-8")
text = file.read().lower()
file.close()
def remove_punc(paskatpois):
    punctuation = ',!@#$%^&*()_-+={}[]:;"\'|<>,.?/~`'
    for marker in punctuation:
        paskatpois = paskatpois.replace(marker, "")
    return paskatpois
text = remove_punc(text)
text = text.split()
"""
number_of_Иго = 0

for word in text:
    if word.startswith("Иго"):
        number_of_Иго += 1
print('Igo:n määrä on', number_of_Иго)
"""
"""
number_of_Иго = text.count("дв")
print(number_of_Иго)
"""
def count_in_list(item_to_count, list_to_search):
    number_of_hits = 0
    for word in list_to_search:
        if word.startswith(item_to_count):
            number_of_hits += 1
    return number_of_hits
"""
for word in text:
    print(word, count_in_list(word, text))
"""
def counter2(list_to_search):
    unique_words = set(list_to_search)
    for word in unique_words:
        print(word, count_in_list(word, list_to_search))
        
counter2(text)
"""
def counter(list_to_search):
    counts = {}
    for word in text:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return(counts)
print(counter(text))
"""



































