#Concentration

from random import *
from pygame import *
screen = display.set_mode((1200,800))
screen.fill((255, 255, 255))

font.init()
init()
ArialFont = font.SysFont("Arial", 150, True, False)

korean = {"사과":"apple", "주황색":"orange","바나나":"bannana","배": "pear","포도":grape,"수박":watermelon,"감자":potato,"토마토,":tomato,"가지": eggplant,"콜리 플라워":cauliflower,"양배추":cabbage,"후추":pepper }
#english = {"apple":사과,"orange":주황색,"bannana":바나나, "pear":배,"grape":포도,"watermelon":수박, "poatato":감자, "tomato":토마토,"eggplant":가지,"cauliflower":콜리 플라워 ,"cabbage":양배추 ,"pepper":후추}
kwords = korean.keys()
shuffle (kwords)
for k in kwords[:8]:
    print(korean[k])
##food =[foodwords, fooddefs]
##shuffle(foodwords)
##shuffle(fooddefs)
###shuffle(food)
##print (food)

title= ArialFont.render("Concentration", True, (255,0, 100))
cardstop=[Rect(x*140+40, 200, 120, 175) for x in range(8)] #top row of cards
cardsbot= [Rect(x*140+40, 475, 120, 175) for x in range(8)] #bottom row of cards

#for x in range(8):
    



running=True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
            
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    screen.fill((0,0,0))

    screen.blit(title, (160, 9))
    for r,v in zip(cardstop, cardsbot): #Don't really know what zip does...was in sir's code
        draw.rect(screen,(255,255,255),r)
        draw.rect(screen,(255,255,255),v)

    
    display.flip()
quit()
