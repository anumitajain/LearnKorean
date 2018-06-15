#BROKEN PRE-HISTORic Version of Concentrationfuntionworks.py
from random import *
from pygame import *
import time

screen = display.set_mode((1200,800))
#screen.fill((255,255,255))
korean = {"사과":"apple", "주황색":"orange","바나나":"bannana",
          "배": "pear","포도":"grape","수박":"watermelon",
          "감자":"potato","토마토":"tomato","가지": "eggplant",
          "콜리 플라워":"cauliflower","양배추":"cabbage","후추":"pepper"}

english = {"apple":"사과","orange":"주황색","bannana":"바나나", "pear":"배",
               "grape":"포도","watermelon":"수박", "poatato":"감자",
               "tomato":"토마토","eggplant":"가지", "cauliflower":"콜리 플라워",
               "cabbage":"양배추" ,"pepper":"후추"}
cardstop=[Rect(x*140+40, 200, 120, 175) for x in range(8)] #top row of cards
cardsbot= [Rect(x*140+40, 475, 120, 175) for x in range(8)] #bottom row of cards



def concentration():
    
    enlist = list(english.keys())
    shuffle(enlist)
    kwords = list(enlist[:8])  #actually english words
    ewords = list(enlist[:8])
    shuffle(kwords)#must shuffle outside loop so words don't keep flashing

    kwordstate =[] #records all the word states.
                   #Will only be used when changing the state
    ewordstate = []

    for i in range(len(ewords)): #one loop for 4 lists because they all have the same length
        ewordstate.append([ewords[i],"covered"]) #because every word starts off covered
        kwordstate.append([kwords[i],"covered"]) #same list as ewordstate
       
    print(kwordstate)
    print(ewordstate)

    running=True
    while running:
        for e in event.get():
            if e.type == QUIT:
                return "menu"
                running = False

        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()        


        drawscene(screen, ewords, kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
        turn(kwords, ewords, korean, english,kwordstate,ewordstate, cardstop, cardsbot)

        for i in range(len(kwordstate)):
            if kwordstate[i][1] == "solved":
                s +=1

        if s == 8:
            if replayRect.collidepoint(mx,my) and mb[0]==1:
                return "concentration" 

    
def drawscene(screen, ewords, kwords, endict, kwordstate, ewordstate,topcards, bottomcards):  #draws everything
    font.init()
    init()
    ArialFont = font.SysFont("Arial", 150, True, False)
    cfnt = font.SysFont("Comic Sans MS", 30, False, False)
    cfnt1 = font.SysFont("Comic Sans MS", 20, True, False)
    cfnt2 = font.SysFont("Comic Sans MS", 25, True, False)
    fnt = font.Font("cyberbit.ttf",60)
    fnt2 = font.Font("cyberbit.ttf",40)
    fnt3 = font.Font("cyberbit.ttf",30)
    correct = cfnt.render("Correct!", True, (0, 255, 0))
    incorrect = cfnt.render("Incorrect!", True, (255, 0, 0))
    win = True
    running=True
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        screen.fill((255,255,255))
        
        title= ArialFont.render("Concentration", True, (100,100, 100))
        screen.blit(title, (160, 9))
        
        w=0 
        for i in range(len(kwordstate)):
            if kwordstate[i][1] == "covered":
                #print(topcards[i])
                draw.rect(screen,(0,0,0), (topcards[i]))
                w += 1 #means user hasn't won yet
            else:
                draw.rect(screen,(0,0,0), (topcards[i]))
                #screen.blit(correct, (550, 900))
                if len(endict[kwords[i]])> 4: #special cases for diff len strings so spacing looks good
                    txt = fnt3.render(endict[kwords[i]][:2], True, (255,255,255)) #so the text fits in the rectangle and looks pretty
                    txt2 = fnt3.render(endict[kwords[i]][2:], True, (255,255,255))
                    screen.blit(txt,(i*140 +70, 240))
                    screen.blit(txt2, (i*140 + 45, 280))
                elif len(endict[kwords[i]]) > 2:
                    txt = fnt2.render(endict[kwords[i]], True, (255,255,255))
                    screen.blit(txt, (i*140 +40, 250))
                elif len (endict[kwords[i]]) == 1:
                    txt = fnt.render(endict[kwords[i]], True, (255,255,255))
                    screen.blit(txt, (i*140 +70, 240))
                else:
                    txt = fnt.render(endict[kwords[i]], True, (255,255,255))
                    screen.blit(txt, (i*140 +40, 240))

        for i in range(len(ewordstate)): 
            if ewordstate[i][1] == "covered":
                draw.rect(screen,(0,0,0), bottomcards[i])
                w += 1
            else:
                draw.rect(screen,(0,0,0), bottomcards[i])
                #screen.blit(correct, (550, 400))
                if len(ewords[i])>= 9:
                    txt = cfnt1.render(ewords[i], True, (255,255,255))
                    screen.blit(txt, (i*140+47, 545))
                elif len(ewords[i])>=7:
                    txt = cfnt2.render(ewords[i], True, (255,255,255))
                    screen.blit(txt, (i*140+47, 545))
                elif len(ewords[i]) ==6 :
                    txt = cfnt.render(ewords[i], True, (255,255,255))
                    screen.blit(txt, (i*140+47, 537))
                else:
                    txt = cfnt.render(ewords[i], True, (255,255,255))
                    screen.blit(txt, (i*140+60, 535))
                    
        display.flip()

        
        if w > 0 :
            return True

    return False #means user has won
  
#clickone= False #checks if user has picked first card
def turn(kwords,ewords, krdict, endict, kwordstate, ewordstate, topcards, bottomcards):
    click1= False #checks if user has picked first card
    click2 = False
    running=True
    c1 = 0 #card place top
    c2 = 0 #card place bottom
    cfnt = font.SysFont("Comic Sans MS", 40, False, False)
    correct = cfnt.render("Correct!", True, (0, 255, 0))
    incorrect = cfnt.render("Incorrect!", True, (255, 0, 0))
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        
        #tt = 0  #turn counter top
        #tb = 0 #turn counter bottom

        if click1 == False: #so user can only select one top card at a time
            for i in range(len(topcards)):
                c1 = i #will count how many times it loops before it breaks
                if topcards[i].collidepoint(mx,my) and mb[0] == 1:
                    if kwordstate[i][1] == "covered":     
                        card1 = kwords[i]
                        kwordstate[i][1] = "uncovered" #screen should redraw at this point
                        drawscene(screen, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
                        click1 = True
                        break
            
           
        if click1== True: #so user can only select second card after first card has been selected
            for i in range(len(bottomcards)):
                c2 = i #will count how many times it loops before it breaks
                if bottomcards[i].collidepoint(mx,my) and mb[0] == 1:
                    if ewordstate[i][1] == "covered":
                        card2 = ewords[i]
                        ewordstate[i][1] = "uncovered"  #screen should redraw at this point again
                        drawscene(screen, ewords,kwords,english,kwordstate, ewordstate, cardstop, cardsbot)
                        click2 = True
                        break
                
        #print(clickone, click2)                
        if click1==True and click2 == True:
            click1 = False #so new turn runs smoothly
            click2 = False#
            print(card1,card2)
            if str(card1) == str(card2):
                kwordstate[c1][1] = "solved" #for some reason this changes kwordstate[7][1] to solved instead of [c1-1][1]
                ewordstate[c2][1] = "solved" #screen should redraw here too
                screen.blit(correct, (500, 400))
                display.flip()
                time.wait(600)
                drawscene(screen, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
            else:
                kwordstate[c1][1] = "covered" #for some reason this doesn't change to covered
                ewordstate[c2][1] = "covered"
                #screen.blit(incorrect, (500, 400))
                ##time.wait(1100)
                #display.flip()
                time.wait(1100)
                drawscene(screen, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
                

    display.flip()


#running=True
#while running:
#    for e in event.get():
#        if e.type == QUIT:
#            running = False


concentration()   

##drawscene(screen, ewords, english, kwordstate, ewordstate, cardstop, cardsbot)
##turn(kwords, ewords, korean, english,kwordstate,ewordstate, cardstop, cardsbot)

##for i in range(len(kwordstate)):
##    if kwordstate[i][1] == "solved":
##        s +=1
##
##if s == 8:
##    if replayRect.collideoint(mx,my) and mb[0]==1:
##        concentration()
##user = False
##if user = True:
    

    
    #display.flip()
quit()

