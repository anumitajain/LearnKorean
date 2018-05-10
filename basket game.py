#Basket game.
#----------------------------------
from pygame import *
#----------------------------------
screen = display.set_mode((1200, 800))
#----------------------------------
basket = image.load("basket.jpg")
#----------------------------------
bx = 0

def moveBasket(bx):
    keys = key.get_pressed()
    
    if keys[K_LEFT] and bx >= 10:
        bx -= 10
    if keys[K_RIGHT] and bx < 1040:
        bx += 10
    return bx
    
running=True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    bx = moveBasket(bx)
    
    screen.fill((255,255,255))
    screen.blit(basket, (bx, 640))

    myClock.tick(100)
    display.flip()
quit()
    
    
    
