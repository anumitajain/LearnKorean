#LearnKorean.py
#Using functions to create different modes
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

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        display.flip()
        audio = r.listen(source)
        
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        string = r.recognize_google(audio, language = "ko").lower()
        #print(type(splitData))
        #string = " ".join(splitData)
        return string
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:  #What is e?
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def start():
    running= True
    myClock = time.clock()
    font.init()
    init()
    ArialFont = font.SysFont("Arial", 40, True, False)
    buttons = [Rect(450,y*100+270,300,80) for y in range(5)]
    vals = ["beginner","intermediate","advanced","concentration","falling words"]
    
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
            screen.blit(txt, (480, y*100 + 285))
            y+=1
            if r.collidepoint(mx,my):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return v
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()
def beginner():
    
    #IMAGE LOADING
    blueArrowPic = image.load("blueArrow.png")    
    micPic = image.load("micPic.jpg")
    heartPic = image.load("heart.png")
    gameOver = image.load("game over.png")
    #FONT LOADING
    correct = Fontt.render("Correct!", True, (0, 255, 0))
    incorrect = Fontt.render("Incorrect!", True, (255, 0, 0))
    Pronounce= Fontt.render("Try to pronounce this word.", True, (0,0,0))
    startRecording = Fontt.render("^CLICK to start recording.", True, (0,0,0))
    NoUnderstand = smallfont.render("Google Speech Recognition could not understand audio.", True, (0,0,0))

    #Font and word stuff
    fnt = font.Font("cyberbit.ttf",60)
    words = ["안녕","여보세요","내 이름은","잘 지냈어요"]
    definitions =["hi, bye","hello","My name is", "How are you"]
    word = randint(0,3) #picks the word in the list
    txtPic = fnt.render(words[word],True,(0,0,0)) #This only picks one word and only resets when the code loops
    heart = [880, 0, 0, 73]
    
    #RECTS
    beginnerRect = Rect(80, 200, 500, 120)
    micRect = Rect(530, 300, 140, 140)
    KtxtRect = Rect(400, 150, 400, 100)
    correctRect = Rect(500, 600, 200, 50)
    statusRect = Rect(400, 480, 400, 80)
    incorrectRect = Rect(500, 600, 200, 50)
    #FILL AND BLIT
    screen.fill((255,255,255))
    screen.blit(Pronounce, (400, 120))
    screen.blit(startRecording, (465, 442))
    screen.blit(blueArrowPic, (300, 150))
    screen.blit(micPic, (530, 300))
    screen.blit(txtPic,(400,150))
    screen.blit(heartPic, (880, 0))
    screen.blit(heartPic, (960, 0))
    screen.blit(heartPic, (1040, 0))
    screen.blit(heartPic, (1120, 0))

    recording = False
    running = True
    while running:
        for evnt in event.get():          
            if evnt.type == QUIT:
                running = False
                return "menu"
            if evnt.type == MOUSEBUTTONDOWN:
                click = True
        if key.get_pressed()[27]:
            running = False
            return "menu"
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        draw.rect(screen, (0), micRect, 2)
        draw.rect(screen, (0), KtxtRect, 2)
        draw.rect(screen, (0), statusRect, 2)
        
        if micRect.collidepoint(mx,my) and mb[0] == 1:
            recording = True #add to function if making 
            draw.rect(screen, (255,255,255), (465,442, 303, 30))
            recordnotif = Fontt.render("Recording...", True, (0,0,0))
            screen.blit(recordnotif,(465,442))
            string = record() #add to function if making
            spokentext = fnt.render(string, True, (0,0,0))
            screen.blit(spokentext, (400,465))
            if string == words[word]: #word needs to be added too
                screen.blit(correct, (500, 600))
                display.flip()
                time.sleep(2)
                draw.rect(screen, (255,255,255), incorrectRect)
                break
            else:
                if heart[2] == 240: #so does heart
                    screen.blit(gameOver, (0, 0))
                    display.flip()
                    time.sleep(5)
                    return "menu"
                else:
                    screen.blit(incorrect, (500, 600))
                    display.flip()
                    time.sleep(2)
                    draw.rect(screen, (255,255,255), statusRect)
                    draw.rect(screen, (0,0,0), statusRect, 2)
                    draw.rect(screen, (255,255,255), incorrectRect)
                    heart[2]+=80
                    draw.rect(screen, (255,255,255), heart)
                    #b = randint(0,3)
                    #txtPic2 = fnt.render(words[b],True,(0,0,0))
                   # screen.blit(txtPic2,(400,150))
                    
        else:
            recording = False
            draw.rect(screen, (255,255,255), (465,442, 303, 30))
            screen.blit(startRecording, (465, 442))

        display.flip()
    return "beginner"
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
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                return "menu"
        if key.get_pressed()[27]: running = False

        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()        


        drawscene(screen, ewords, kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
        ret = turn(kwords, ewords, korean, english,kwordstate,ewordstate, cardstop, cardsbot)
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
    #correct = cfnt.render("Correct!", True, (0, 255, 0))
    #incorrect = cfnt.render("Incorrect!", True, (255, 0, 0))
##    win = True
##    running=True
##    while running:
##        for e in event.get():
##            if e.type == QUIT:
##                running = False
              
    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    screen.fill((255,255,255))
    
    title= ArialFont.render("Concentration", True, (100,100, 100))
    screen.blit(title, (160, 9))
    
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
                return "menu"
            if key.get_pressed()[27]:  #esc key
                running = False
                return "menu"
            
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
                #print("It's me!!!!")
                time.sleep(1)
                drawscene(screen, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
            else:
                kwordstate[c1][1] = "covered" #for some reason this doesn't change to covered
                ewordstate[c2][1] = "covered"
                #screen.blit(incorrect, (500, 400))
                ##time.wait(1100)
                #display.flip()
                time.sleep(1)
                drawscene(screen, ewords,kwords, english, kwordstate, ewordstate, cardstop, cardsbot)
                
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
