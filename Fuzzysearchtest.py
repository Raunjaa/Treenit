# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 11:26:57 2018

@author: jraunama
"""
#testiteksti alla
"""
   Митинымъ сыномъ Шадрина, на Нечаевѣ четвертонатцатомъ жеребью: дв. Минка Ивашковъ, сынъ его Дорошко, сѣютъ ржы 4 коробьи, а сѣна косятъ 20 копенъ, обжа; а старого дохода шло боранъ, полоть мяса, 2 коробьи ржы, 2 воробьи овса; а ключнику сыръ, лопатка боранья, горсть лну. А нового дохода 5 денегъ, боранъ, полоть мяса, пятокъ лну, острамокъ сѣна, 3 воробьи ржы, пол- пяты коробьи овса, коробья съ четверткою ячмени, четвертка пшеницы, четвертка хмелю.
   Грузовыхъ: Д. Горка Игонево!!hnpn!!pn, вопчѣ съ Ивановскими обжами Кузмина сына Савелко- ва, что за Ондрюшкою за Одинцовымъ, да съ Николскими обжами Неревского конца, что за Васюкомъ за Мунзорою за Хлуденевымъ, на Нечаевѣ половинѣ: дв. Корманко да Терешко Сменовы, дв. Гаврилко Янушовъ да Мартынко Окинѳовъ, дв. Селиванко Спировъ, сѣютъ ржы.Грузовыхъ: Д. Горка Игонево!!hnpn!!pn, вопчѣ съ Ивановскими обжами Кузмина сына Савелко- ва, 
что за Ондрюшкою за Одинцовымъ, да съ Николскими обжами Неревского конца, что за Васюкомъ за Мунзорою за Хлуденевымъ, на Нечаевѣ половинѣ: дв. Корманко да Терешко Сменовы, дв. Гаврилко Янушовъ да Мартынко Окинѳовъ, дв. Селиванко Спировъ, сѣютъ ржы.I дв.Терехъ Иваш¬ковъ, дв.Гридка Ивашковъ.2Иго.
"""


import re
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
file = open('data/NovgoTest.txt', encoding ="UTF-8")
text = file.read()
file.close()
abbreviations = "(дв|Д)[.]"
def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(abbreviations,"\\1<prd>",text)
    text = text.replace(".",".<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

sentences = split_into_sentences(text)
print(sentences)


sentences_hit = []
for sentence in sentences:
        for word in sentence.split():
            if int(fuzz.ratio(word, "Иго")) > 80:
                sentences_hit.append(sentence)
print(sentences_hit) #antaa tyhjän tuplen tulokseksi

