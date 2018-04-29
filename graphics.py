#Graphics
#-----------------------------------------------
from pygame import *
#-----------------------------------------------
rec = ((1200, 800))
screen = display.set_mode(rec)
screen.fill((255, 255, 255))
#-----------------------------------------------
blueArrowPic = image.load("blueArrow.png")
screen.blit(blueArrowPic, (300, 150))
micPic = image.load("micPic.jpg")
screen.blit(micPic, (530, 300))
#-----------------------------------------------
micRect = Rect(530, 300, 140, 140)
txtRect = Rect(400, 150, 400, 100)
correctRect = Rect(500, 600, 200, 50)
statusRect = Rect(400, 480, 400, 80)
draw.rect(screen, (0), micRect, 2)
draw.rect(screen, (0), txtRect, 2)
draw.rect(screen, (0), correctRect, 2)
draw.rect(screen, (0), statusRect, 2)
#-----------------------------------------------
running=True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            triPic = screen.copy()
            if e.button == 1:
               linePic = screen.copy()
               lineStartx,lineStarty = e.pos

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
#-------------------------------------------------
    

#--------------------------------------------------
    display.flip()
quit()
