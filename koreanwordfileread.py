# -*- coding: utf-8 -*-
from pygame import *
init()
screen = display.set_mode((640,480))
words = open("koreanWords.txt").read().split().strip()
print(words)
