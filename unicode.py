# -*- coding: utf-8 -*-
from pygame import *
init()
one_moment = "等一下"
easy = "그것은 쉽다"
screen = display.set_mode((640,480))
fnt = font.Font("cyberbit.ttf",60)
txtPic = fnt.render(easy,True,(255,255,255))
screen.blit(txtPic,(100,100))

running = True
while running:
    for evnt in event.get():                
        if evnt.type == QUIT:
            running = False

    display.flip()

quit()
