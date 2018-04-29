# -*- coding: utf-8 -*-
from pygame import *
import codecs
import requests

raw = requests.get("https://www.topikguide.com/6000-most-common-korean-words-1/")

init() #idk if this serves a purpose
file = codecs.open("koreanWords.txt", "r","utf-8")
file1= file.read().strip("\n")
enFile = file1.encode('utf-8')
print(type(file1))
print(enFile)
relatedlist = []
kwords =[]
kdefs = []
pos = 0
for line in file: 
    if line == file[pos]: #checks if the line is the line we want to remove
        file.remove(line) 
        pos +=3 #+3 because every 3 pos there is a number

    
for newline in file: #new variable because new list?
    c = 0
    if c%2 == 0:
        kwords.append(newline)
    else:
        kdefs.append(newline)

 
