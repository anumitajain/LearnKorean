#Concentration3
#Hopefully a better version of concentration 2
#A game within Learn Korean but not developed enough to be put into a function and integrated properly
#need 2 functions
#one that draws stuff
#one that is the turn
#for i in range(100):
#
from random import *
from pygame import *
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

enlist = list(english.keys())
shuffle(enlist)
kwords = list(enlist[:8])  #actually english words
ewords = list(enlist[:8])
print(ewords)
shuffle(kwords)#must shuffle outside loop so words don't keep flashing
print(kwords)


cardstop=[Rect(x*140+40, 200, 120, 175) for x in range(8)] #top row of cards
cardsbot= [Rect(x*140+40, 475, 120, 175) for x in range(8)] #bottom row of cards

kwordstate =[] #records all the word states.
               #Will only be used when changing the state
ewordstate = []
cardmodeT =[]
cardmodeB = []
for i in range(len(ewords)): #one loop for 4 lists because they all have the same length
    ewordstate.append([ewords[i],"covered"]) #because every word starts off covered
    kwordstate.append([kwords[i],"covered"]) #same list as ewordstate
    cardmodeT.append([cardstop[i], "covered"])
    cardmodeB.append([cardsbot[i],"covered"])
print(kwordstate)
print(ewordstate)
    
def drawscene(screen, ewords, endict, kwordstate, ewordstate,topcards, bottomcards):  #draws everything
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
        
        c=0 
        for i in range(len(kwordstate)):
            if kwordstate[i][1] == "covered":
                #print(topcards[i])
                draw.rect(screen,(0,0,0), (topcards[i]))
                #c += 1 #means user hasn't won yet
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

        return True
        #if c > 0 :
            #return True

    #return False #means user has won
  
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
                        drawscene(screen, ewords, english, kwordstate, ewordstate, cardstop, cardsbot)
                        click1 = True
                        break
            
           
        if click1== True: #so user can only select second card after first card has been selected
            for i in range(len(bottomcards)):
                c2 = i #will count how many times it loops before it breaks
                if bottomcards[i].collidepoint(mx,my) and mb[0] == 1:
                    if ewordstate[i][1] == "covered":
                        card2 = ewords[i]
                        #print(c2-1)
                        ewordstate[i][1] = "uncovered"  #screen should redraw at this point again
                        #print(ewordstate)
                        drawscene(screen, ewords, english,kwordstate, ewordstate, cardstop, cardsbot)
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
                drawscene(screen, ewords, english, kwordstate, ewordstate, cardstop, cardsbot)
            else:
                kwordstate[c1][1] = "covered" #for some reason this doesn't change to covered
                ewordstate[c2][1] = "covered"
                #screen.blit(incorrect, (500, 400))
                ##time.wait(1100)
                #display.flip()
                time.wait(1100)
                drawscene(screen, ewords, english, kwordstate, ewordstate, cardstop, cardsbot)
                

    display.flip()

#p1 = Rect(150,280,80,30)
#p2 = Rect(570,280,80,30)

#running=True
#while running:
#    for e in event.get():
#        if e.type == QUIT:
#            running = False


##        if e.type == MOUSEBUTTONDOWN:
##            if person == "p1 wait":
##                if cardstop[0].collidepoint(e.pos):
##                    person = "p1 move"
##                    timer = 100
##            if person == "p2 wait":
##                if p2.collidepoint(e.pos):
##                    person = "p2 move"
##                    timer = 100
##
##    timer -= 1
##    if timer == 0 and turn == "p1 move":
##        turn = "p2 wait"
##    if timer == 0 and turn == "p2 move":
##        turn = "p1 wait"
##
##
##            
   # mb = mouse.get_pressed()
   # mx, my = mouse.get_pos()
   # screen.fill((0,0,0))

    

drawscene(screen, ewords, english, kwordstate, ewordstate, cardstop, cardsbot)
turn(kwords, ewords, korean, english,kwordstate,ewordstate, cardstop, cardsbot)
##    for r,v in zip(cardstop, cardsbot): #Don't really know what zip does...was in sir's code
##        draw.rect(screen,(255,255,255),r)
##        draw.rect(screen,(255,255,255),v)
##        
##    c=0 #card space
##    for k in kwords[:8]: #top row korean
##        if len(k)> 4: #special cases for diff len strings so spacing looks good
##            txt = fnt3.render(kwords[c][:2], True, (0,0,0)) #so the text fits in the rectangle and looks pretty
##            txt2 = fnt3.render(kwords[c][2:], True, (0,0,0))
##            screen.blit(txt,(c*140 +70, 240))
##            screen.blit(txt2, (c*140 + 45, 280))
##            c+=1
##        elif len(k) > 2:
##            txt = fnt2.render(kwords[c], True, (0,0,0))
##            screen.blit(txt, (c*140 +40, 250))
##            c+=1
##        elif len (k) == 1:
##            txt = fnt.render(kwords[c], True, (0,0,0))
##            screen.blit(txt, (c*140 +70, 240))
##            c+=1
##        else:
##            txt = fnt.render(kwords[c], True, (0,0,0))
##            screen.blit(txt, (c*140 +40, 240))
##            c+=1
##    c=0
##    for e in ewords:#bottom row english
##        if len(korean[e])>= 9:
##            txt = cfnt1.render(korean[e], True, (0,0,0))
##            screen.blit(txt, (c*140+47, 545))
##            c+=1
##        elif len(korean[e])>=7:
##            txt = cfnt2.render(korean[e], True, (0,0,0))
##            screen.blit(txt, (c*140+47, 545))
##            c+=1
##        elif len(korean[e]) ==6 :
##            txt = cfnt.render(korean[e], True, (0,0,0))
##            screen.blit(txt, (c*140+47, 537))
##            c+=1
##        else:
##            txt = cfnt.render(korean[e], True, (0,0,0))
##            screen.blit(txt, (c*140+60, 535))
##            c+=1

    
    #display.flip()
quit()

