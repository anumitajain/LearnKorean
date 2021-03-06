from pygame import *
from random import *
import speech_recognition as sr
import time 

#Setting fonts
font.init()
init()
Fontt = font.SysFont("Comic Sans MS", 20, False, False)
smallfont = font.SysFont("Comic Sans MS", 15, False, False)
#SCREEN
screen = display.set_mode((1200,800))
screen.fill((255, 255, 255))
korean = {"사과":"apple", "오렌지":"orange","바나나":"bannana",
          "배": "pear","포도":"grape","수박":"watermelon",
          "감자":"potato","토마토":"tomato","가지": "eggplant",
          "콜리 플라워":"cauliflower","양배추":"cabbage","후추":"pepper"} #used in concentration()

english = {"apple":"사과","orange":"오렌지","bannana":"바나나", "pear":"배",
               "grape":"포도","watermelon":"수박", "potato":"감자",
               "tomato":"토마토","eggplant":"가지", "cauliflower":"콜리 플라워",
               "cabbage":"양배추" ,"pepper":"후추"} #used in concentration()
cardstop=[Rect(x*140+40, 200, 120, 175) for x in range(8)] #top row of cards #used in concentration()
cardsbot= [Rect(x*140+40, 475, 120, 175) for x in range(8)] #bottom row of cards #used in concentration()


def start():
    running= True
    myClock = time.clock()
    font.init()
    init()
    ArialFont = font.SysFont("Arial", 40, True, False)
    buttons = [Rect(450,y*100+270,300,80) for y in range(3)]
    vals = ["falling words","speak korean","concentration"]
    
    while running:
        for e in event.get():
            if e.type == QUIT:
                return "exit"
            
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        screen.fill((255,255,255))
        y = 0
        for r,v in zip(buttons,vals):
            draw.rect(screen,(222,55,55),r)
            #draw.circle(screen,(222,55,55),(r.x+50,r.y+20),20)
            txt = ArialFont.render(v, True, (255,255,255))
            screen.blit(txt, (490, y*100 + 285))
            y+=1
            if r.collidepoint(mx,my):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()


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
    replayRect = Rect(1100,700,95,95)
    running=True
    click = 0
    
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                return "menu"
        if key.get_pressed()[27]: running = False

        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()        
        myClock = time.clock()
        print(myClock)
        drawscene(screen,click,myClock, ewords, kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
        ret = turn(myClock,kwords, ewords, korean, english,kwordstate,ewordstate, cardstop, cardsbot)
        if ret != "play":
            return ret
        else:
            return "concentration"
##        s=0
##        for i in range(len(kwordstate)):
##            if kwordstate[i][1] == "solved":
##                s +=1
##
##        if s == 8:
##            if replayRect.collidepoint(mx,my) and mb[0]==1:
##                return "concentration"
    #display.flip()
    #return "menu"

    
def drawscene(screen,click,myClock, ewords, kwords, endict, kwordstate, ewordstate,topcards, bottomcards):  #draws everything
    font.init()
    init()
    ArialFont = font.SysFont("Arial", 150, True, False)
    cfnt = font.SysFont("Comic Sans MS", 30, False, False)
    cfnt1 = font.SysFont("Comic Sans MS", 20, True, False)
    cfnt2 = font.SysFont("Comic Sans MS", 25, True, False)
    fnt = font.Font("cyberbit.ttf",60)
    fnt2 = font.Font("cyberbit.ttf",40)
    fnt3 = font.Font("cyberbit.ttf",30)

    redo = image.load("undo.png")
    redo = transform.scale(redo, (50,50))
    
    replayRect = Rect(500,695,50,50)
    
    
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    screen.fill((255,255,255))
    
    title= ArialFont.render("Concentration", True, (100,100, 100))
    screen.blit(title, (160, 9))
    clicktxt = cfnt.render(str(click), True, (0, 0, 0))
    screen.blit(clicktxt, (400, 685))
    draw.rect(screen, (255,255,255), replayRect)
    screen.blit(redo, (500,695))
##    print(myClock)
##    minutes = myClock//60
##    seconds = myClock%60
##    mintxt = cfnt2.render(str(minutes),True,(0,0,0))
##    sectxt = cfnt2.render(str(seconds),True,(0,0,0))
##    colon = cfnt2.render(":",True,(0,0,0))
##
##    screen.blit(mintxt, (500,685))
##    screen.blit(colon, (505, 685))
##    screen.blit(sectxt, (508,685))
   # w=0 
    for i in range(len(kwordstate)):
        if kwordstate[i][1] == "covered":
            #print(topcards[i])
            draw.rect(screen,(0,0,0), (topcards[i]))
            #w += 1 #means user hasn't won yet
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
           # w += 1
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

        
##        if w > 0 :
##            return True
##
##    return False #means user has won
  
#clickone= False #checks if user has picked first card
def turn(myClock, kwords,ewords, krdict, endict, kwordstate, ewordstate, topcards, bottomcards):
    click1= False #checks if user has picked first card
    click2 = False
    running=True
    c1 = 0 #card place top
    c2 = 0 #card place bottom
    cfnt = font.SysFont("Comic Sans MS", 40, False, False)
    cfnt2 = font.SysFont("Comic Sans MS", 25, True, False)
    correct = cfnt.render("Correct!", True, (0, 255, 0))
    incorrect = cfnt.render("Incorrect!", True, (255, 0, 0))
    replayRect = Rect(500,695,50,50)
    click = 0
    #myClock2 = time.clock()
    #minutes = myClock//60
    #seconds = myClock%60

    #myClock3 = myClock
    
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                return "menu"
            if key.get_pressed()[27]:  #esc key
                running = False
                return "menu"
            if key.get_pressed()[K_SPACE]:  #Replays game
                return "concentration"
            
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()

##        myClock2 = time.clock()    #I don't really understand how clocks work...I think I need one here
##        myClock3 = myClock+myClock2 #So my time isn't off
##        print(myClock3)
##        minutes = myClock3//60
##        seconds = int(myClock%60)
##
##        mintxt = cfnt2.render(str(minutes),True,(0,0,0))
##        sectxt = cfnt2.render(str(seconds),True,(0,0,0))
##        colon = cfnt2.render(":",True,(0,0,0))
##        screen.blit(mintxt, (500,685))
##        screen.blit(colon, (509, 685))
##        screen.blit(sectxt, (518,685))

        

        
        #tt = 0  #turn counter top
        #tb = 0 #turn counter bottom

        if replayRect.collidepoint(mx,my) and mb[0]==1:
            return "concentration"
        
        if click1 == False: #so user can only select one top card at a time
            for i in range(len(topcards)):
                c1 = i #will count how many times it loops before it breaks
                if topcards[i].collidepoint(mx,my) and mb[0] == 1:
                    click +=1
                    if kwordstate[i][1] == "covered":     
                        card1 = kwords[i]
                        kwordstate[i][1] = "uncovered" #screen should redraw at this point
                        drawscene(screen,click,myClock,ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
                        click1 = True
                        break
            
           
        if click1== True: #so user can only select second card after first card has been selected
            for i in range(len(bottomcards)):
                c2 = i #will count how many times it loops before it breaks
                if bottomcards[i].collidepoint(mx,my) and mb[0] == 1:
                    if ewordstate[i][1] == "covered":
                        card2 = ewords[i]
                        ewordstate[i][1] = "uncovered"  #screen should redraw at this point again
                        drawscene(screen,click,myClock, ewords,kwords,english,kwordstate, ewordstate, cardstop, cardsbot)
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
                #print("It's me!!!!")
                time.sleep(1)
                drawscene(screen,click,myClock, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
            else:
                kwordstate[c1][1] = "covered" #for some reason this doesn't change to covered
                ewordstate[c2][1] = "covered"
                time.sleep(1)
                drawscene(screen,click,myClock, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
                
    return "play"
    display.flip()

page = "menu"
while page != "exit":
    if page == "menu":
        page = start()
    if page == "beginner":
        page = beginner()
    if page == "concentration":
        page = concentration()

quit()
    
