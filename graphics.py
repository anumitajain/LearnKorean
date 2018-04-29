#Graphics
#-----------------------------------------------
from pygame import *
#-----------------------------------------------
rec = ((1200, 800))
screen = display.set_mode(rec)
screen.fill((255, 255, 255))
#------------------------------------------------
font.init()
init()
Fontt = font.SysFont("Comic Sans MS", 20, False, False)
smallfont = font.SysFont("Comic Sans MS", 15, False, False)
correct = Fontt.render("Correct!", True, (0, 255, 0))
incorrect = Fontt.render("Incorrect!", True, (255, 0, 0))
TryToPronounceThisWord = Fontt.render("Try to pronounce this word.", True, (0,0,0))
startRecording = Fontt.render("^PRESS to start recording.", True, (0,0,0))
couldNotUnderstand = smallfont.render("Google Speech Recognition could not understand audio.", True, (0,0,0))
screen.blit(TryToPronounceThisWord, (400, 120))
screen.blit(startRecording, (465, 442))
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
