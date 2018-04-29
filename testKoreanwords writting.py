#Hardcode version of koreanwordfileread.py
# -*- coding: utf-8 -*-
from pygame import *
from random import *
init()
screen = display.set_mode((640,480))
fnt = font.Font("cyberbit.ttf",60)
words = ["안녕","여보세요","안녕","내 이름은","잘 지냈어요"]
definitions =["hi","hello","bye", "My name is", "How are you"]
while True:
    a = randint(0,4)
    txtPic = fnt.render(words[a],True,(255,255,255))
    screen.blit(txtPic,(100,100))

    running = True
    while running:
        for evnt in event.get():                
            if evnt.type == QUIT:
                running = False

        display.flip()

quit()


    

              
