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

englishadv = {"apple":"사과","orange":"오렌지","bannana":"바나나", "pear":"배",
               "grape":"포도","watermelon":"수박", "potato":"감자",
               "tomato":"토마토","eggplant":"가지", "cauliflower":"콜리 플라워",
               "cabbage":"양배추" ,"pepper":"후추"} #used in concentrationadv() 

englishult = {"apple":"사과","orange":"오렌지","bannana":"바나나", "pear":"배",
               "grape":"포도","watermelon":"수박", "potato":"감자",
               "tomato":"토마토","eggplant":"가지", "cauliflower":"콜리 플라워",
               "cabbage":"양배추" ,"pepper":"후추"} #some words} #all the words we are using
                                                              #combines beginner, intermediate and advanced

englishint = {"hi":"안녕","bye":"안녕","hello":"여보세요","My name is":"내 이름은",
              "How are you":"잘 지냈어요", "How much?":"","Good morning":"", "Good night":""}#concentrationint()

englishbeg = {"g/k":"ㄱ", "n/n":"ㄴ", "d/t":"ㄷ", "r/l":"ㄹ", "m/m":"ㅁ", "b/p":"ㅂ", "s/t":"ㅅ", "-/ng":"ㅇ", "j/t":"ㅈ", "kk/k":"ㄲ", "tt/-":"ㄸ", "pp/-":"ㅃ", "ss/t":"ㅆ", "jj/-":"ㅉ", "ch/t":"ㅊ", "k/k":"ㅋ", "t/t":"ㅌ", "p/p":"ㅍ", "a":"ㅏ", "ae":"ㅐ", "ya":"ㅑ", "yae":"ㅒ", "eo":"ㅓ", "e":"ㅔ", "yeo":"ㅕ", "ye":"ㅖ", "o":"ㅗ", "wa":"ㅘ", "wae":"ㅙ", "eo":"ㅚ", "yo":"ㅛ", "u":"ㅜ", "wo":"ㅝ", "we":"ㅞ", "wi":"ㅟ", "yu":"ㅠ", "eu":"ㅡ", "ui":"ㅢ", "i":"ㅣ"}

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
def speakkoreanIntro():
    running= True
    myClock = time.clock()
    font.init()
    init()
    ArialFont = font.SysFont("Arial", 40, True, False)
    buttons = [Rect(450,y*150+270,300,80) for y in range(3)]
    vals = ["beginner","intermediate","advanced"] #Vals that will be blitted on screen
    compvals = ["sk beginner","sk intermediate","sk advanced"]
    
    while running:
        for e in event.get():
            if e.type == QUIT:
                return "menu"
            
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        screen.fill((255,255,255))
        y = 0
        for r,v,c in zip(buttons,vals, compvals):
            draw.rect(screen,(222,168,55),r)
            #draw.circle(screen,(222,55,55),(r.x+50,r.y+20),20)
            txt = ArialFont.render(v, True, (0,0,0))
            screen.blit(txt, (490, y*150 + 285))
            y+=1
            #display.flip()
            if r.collidepoint(mx,my):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    return c
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()
def concentrationIntro():
    running= True
    myClock = time.clock()
    font.init()
    init()
    ArialFont = font.SysFont("Arial", 40, True, False)
    buttons = [Rect(450,y*150+90,300,80) for y in range(4)]
    vals = ["beginner","intermediate","advanced", "ultimate"] #Vals that will be blitted on screen
    compvals = ["c beginner","c intermediate","c advanced", "ultimate"]
    
    while running:
        for e in event.get():
            if e.type == QUIT:
                return "menu"
            
        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()
        screen.fill((255,255,255))
        y = 0
        for r,v,c in zip(buttons,vals, compvals):
            draw.rect(screen,(168,222,55),r)
            #draw.circle(screen,(222,55,55),(r.x+50,r.y+20),20)
            txt = ArialFont.render(v, True, (0,0,0))
            screen.blit(txt, (490, y*150 + 105))
            y+=1
            #display.flip()
            if r.collidepoint(mx,my):
                draw.rect(screen,(0,255,0),r,2)
                if mb[0]==1:
                    time.sleep (1) #so user doesn't pick card when picking mode
                    return c
            else:
                draw.rect(screen,(255,255,0),r,2)
                
        display.flip()

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

def skbeginner():
    
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
    return "skbeginner"
def skintermediate():
    
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
    return "sk intermediate"

def concentrationint():
    
    enlist = list(englishint.keys())
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
        if key.get_pressed()[27]:
            running = False
            return "menu"

        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()        
        myClock = time.clock()
        print(myClock)
        drawscene(screen,click,myClock, ewords, kwords, englishint, kwordstate, ewordstate, cardstop, cardsbot)
        ret = turn(myClock,kwords, ewords, koreanint, englishint,kwordstate,ewordstate, cardstop, cardsbot)
        if ret != "play":
            return ret
        else:
            return "c intermediate" 
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
def concentrationadv():
    
    enlist = list(englishadv.keys())
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
        if key.get_pressed()[27]:
            running = False
            return "menu"

        mb = mouse.get_pressed()
        mx, my = mouse.get_pos()        
        myClock = time.clock()
        print(myClock)
        drawscene(screen,click,myClock, ewords, kwords, englishadv, kwordstate, ewordstate, cardstop, cardsbot)
        ret = turn(myClock,kwords, ewords, koreanint, englishadv,kwordstate,ewordstate, cardstop, cardsbot)
        if ret != "play":
            return ret
        else:
            return "c advanced" 
    
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
                return "c intermediate"
            
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
            return "c intermediate"
        
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

font.init()
init()
screen = display.set_mode((1200, 800))
#the highscore is kept during the time the game runs. If you replay the game (press the replay button), the highscore will be kept, but if you exit out of the game, the highscore will be lost.
highscoreList = [0]

#GLOBAL RELATED LISTS FOR BASKET GAME
listFalling_koreanCh = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
listBasket_englishPh = ["g/k", "n/n", "d/t", "r/l", "m/m", "b/p", "s/t", "-/ng", "j/t", "kk/k", "tt/-", "pp/-", "ss/t", "jj/-", "ch/t", "k/k", "t/t", "p/p", "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "eo", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"] 

#GAMEINTRO
#the intro page for the basket game. You only see it once.
def gameIntro():
    myClock = time.Clock()
    intro = True
    while intro == True:
        for n in event.get():
            if n.type == QUIT:
                quit()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        
        chart = image.load("hangul.jpg")
        startImage = image.load("start.jpg")
        startImageDarker = image.load("start_dark.jpg")
        helpIcon = image.load("help.jpg")
        
        screen.fill((255,255,255))
        
        fntMenu = font.SysFont("Comic Sans MS", 20, False, False)
        fntMenuBigger = font.SysFont("Comic Sans MS", 25, False, False)
        text1 = fntMenuBigger.render("This chart shows you the Korean hangul and the matching English phonetic pronunciations.",True,(0,0,0))
        text2 = fntMenu.render("Take a good look at this chart if you want to do well!",True,(0,0,0))
        text3 = fntMenu.render("To access this chart, click the        icon. However, each time you do this, you'll lose half of your points.",True,(0,0,0))

        textWidth1 = text1.get_width()
        textWidth2 = text2.get_width()
        textWidth3 = text3.get_width()
        startImageWidth = startImage.get_width()
        startRect = Rect(600-startImageWidth//2, 720, 172, 70)
        screen.blit(text1, (600-textWidth1//2, 10))
        screen.blit(text2, (600-textWidth2//2, 60))
        screen.blit(chart, (383, 110))
        screen.blit(text3, (600-textWidth3//2, 670))
        draw.rect(screen, (255,255,255), startRect, 2) 
        screen.blit(startImage, (600-startImageWidth//2, 720))
        screen.blit(helpIcon, (410, 668))
        
        if startRect.collidepoint(mx,my):
            screen.blit(startImageDarker, (600-startImageWidth//2, 720))
        if mb[0] == 1 and startRect.collidepoint(mx,my):
            intro = False
        display.flip()

#SHOWCHART
#shows the chart that contains the hangul characters and the matching English phonetic sounds for basket game.
#you can access it by clicking the help button during the game, but you lose half your points in exchange. 
def showChart():
    intermission = True
    while intermission == True:
        for u in event.get():
            if u.type == QUIT:
                quit()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.fill((255,255,255))
        chart = image.load("hangul_intermission.jpg")
        chartWidth = chart.get_width()
        continueIcon = image.load("continueIcon.jpg")
        continueIcon_dark = image.load("continueIcon_dark.jpg")
        screen.blit(chart, (600-chartWidth//2, 0))
        continueRect = Rect(1100, 350, 100, 100)
        draw.rect(screen, (255,255,255), continueRect)
        screen.blit(continueIcon, (1100, 350))
        if continueRect.collidepoint(mx,my):
            screen.blit(continueIcon_dark, (1100, 350))
        if mb[0] == 1 and continueRect.collidepoint(mx,my):
            intermission = False
        display.flip()

#GAMEOVER
#the game-over page for the basket game.
#you can exit the game (by clicking the x in the right corner), or replay the game (goes to the screen with falling Korean characters aka 'basketGame()'), or go to the main menu.
#also shows how many points you got before you died, and underneath, the highscore. (Highscore 
def gameOver(points, highscoreList):
    gameOver = True 
    while gameOver == True:
        for b in event.get():
            if b.type == QUIT:
                quit()
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        screen.fill((255,255,255))
        
        fntPoints = font.SysFont("Comic Sans MS", 79, False, False)
        fntScore = font.SysFont("Comic Sans MS", 40, False, False)
        whiteRectangle = image.load("whiteRectangle.png")
        yellowBackground = image.load("yellowBackground.jpg")
        screen.blit(yellowBackground, (0, 0))
        whiteWidth = whiteRectangle.get_width
        whiteHeight = whiteRectangle.get_height
        screen.blit(whiteRectangle, (600-444, 400-300))
        homeIcon = image.load("homeIcon.jpg")
        homeRect = Rect(700, 550, 100, 100)
        draw.rect(screen, (255,255,255), homeRect)
        screen.blit(homeIcon, (700, 550))
        replayIcon = image.load("replay.jpg")
        replayRect = Rect(400, 550, 138, 100)
        draw.rect(screen, (255,255,255), replayRect)
        screen.blit(replayIcon, (400, 550))
        home2 = image.load("home2.jpg")
        replay2 = image.load("replay2.jpg")
        
        points_Txt = fntPoints.render("%d" %(points),True,(0,0,0))
        pointsWidth = points_Txt.get_width()
        screen.blit(points_Txt, (600-pointsWidth//2, 250))
        
        #how my highscoreList works: has a list with '0' in it. If the current point is higher than the last item in the list, it adds to the highscoreList.
        #it blits the last item in the list after everything, aka the highscore.
        if points > highscoreList[-1]:
            highscoreList.append(points)
                        
        highScore_Txt = fntScore.render("Highscore: %d" %(highscoreList[-1]),True,(0,0,0))
        highscoreWidth = highScore_Txt.get_width()
        screen.blit(highScore_Txt, (600-highscoreWidth//2, 350))

        if replayRect.collidepoint(mx,my):
            screen.blit(replay2, (400, 550))
        if homeRect.collidepoint(mx,my):
            screen.blit(home2, (700, 550))
        
        if replayRect.collidepoint(mx,my) and mb[0] == 1:
            basketGame()
        if homeRect.collidepoint(mx,my) and mb[0] == 1:  
            start()                                             
            
        display.flip()
    return highscoreList
                                  
#MOVEBASKET
#returns changed bx to move the basket left and right.
def moveBasket(bx):
    keys = key.get_pressed()    
    if keys[K_LEFT] and bx >= 0:
        bx -= 7
    if keys[K_RIGHT] and bx < 1040:
        bx += 7
    return bx

#DRAWINGLETTERS
#draws the falling Korean characters.
def drawingLetters(fallingLets,fallingY):
    fnt = font.Font("Cyberbit.ttf", 50)
    for i in range(6):
        txtPic1 = fnt.render(fallingLets[i],True,(0,0,0))
        screen.blit(txtPic1, (i*200+85, fallingY[i]))

#MAKENEWLIST
#it makes a new list of Korean characters for the second+ times it loops.
def makeFallingList(let):
    fallingLets = [let]
    while len(fallingLets)<6:
        lets = choice(listFalling_koreanCh)
        if lets not in fallingLets:
            fallingLets.append(lets)
    shuffle(fallingLets)
    return fallingLets

#BASKETGAME
#the actual basket game!
def basketGame():
    running=True
    #bx is the x-coordinate of the moving basket
    bx = 0
    #points is the number of points the user has while playing.
    points = 0
    #lives is the number of lives lost.
    lives = 0
    listFalling_koreanCh = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    listBasket_englishPh = ["g/k", "n/n", "d/t", "r/l", "m/m", "b/p", "s/t", "-/ng", "j/t", "kk/k", "tt/-", "pp/-", "ss/t", "jj/-", "ch/t", "k/k", "t/t", "p/p", "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "eo", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"] 
    onBasket = choice(listBasket_englishPh)
    #koIndex helps me find the related Korean phonetic for the random English word that's currently blitted on the basket.
    KoIndex = listBasket_englishPh.index(onBasket)
    fntBasket = font.SysFont("Comic Sans MS", 29, False, False)
    onBasketTxt = fntBasket.render(onBasket,True,(0,0,0))
    #fallingLets is a list of 6, containing the 6 Korean characters that fall down.
    fallingLets = []
    fallingLets.append(listFalling_koreanCh[KoIndex])
    correctTxt = fntBasket.render("Correct!",True,(0,0,0))
    incorrectTxt = fntBasket.render("Incorrect!",True,(0,0,0))
    scoreTxt = fntBasket.render("Score: ", True, (0,0,0))
    fnt = font.Font("Cyberbit.ttf", 50)
    basket = image.load("basketRealReal.jpg")
    heartPic = image.load("heart.png")
    helpIcon = image.load("help.jpg")
    helpIconDarker = image.load("help_dark.jpg")
    myClock = time.Clock()

    #fills up the fallingLets to its capacity of 6. Also makes sure the Korean phonetic of "onBasket" is in the list. Also makes sure there's no repeats.
    while len(fallingLets)<6:        
        let = choice(listFalling_koreanCh)
        if let not in fallingLets:
            fallingLets.append(let)

    shuffle(fallingLets)

    #creates random negative y-coordinates for the Korean characters to fall from.
    fallingY = [randint(-500,0) for i in range(6)]

    #credit goes to Mr. Mac (you).
    #'heart' is a list containing the rect coordinates for a white rect.
    #the rect increases the x-value to cover the heart-images when the wrong Korean character collides with the basket.
    #this creates the illusion that hearts/lives are being lost.
    heart = [800, 0, 0, 73]
    
    #credit goes to Noor (Nasri).
    #taken is a list that represents the states of the falling Korean characters.
    #later on in the function, if the related FallingLet is colliding with the basket, the False value changes to True.
    #this helps me draw the heartRect properly, blit over the falling Korean character, etc.
    taken = [False, False, False, False, False, False]

    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        bx = moveBasket(bx)

        #you can click on the helpRect to go to the helpful chart.
        helpRect = Rect(10, 50, 30, 30)
        draw.rect(screen, (255,255,255), helpRect)
        basketRect = Rect(bx, 710, 160, 90)
            
        screen.fill((255,255,255))
        screen.blit(heartPic, (800, 0))
        screen.blit(heartPic, (880, 0))
        screen.blit(heartPic, (960, 0))
        screen.blit(heartPic, (1040, 0))
        screen.blit(heartPic, (1120, 0))
        screen.blit(helpIcon, (10, 50))
        
        draw.rect(screen,(255,255,255),basketRect,2)
        screen.blit(basket, (bx, 710))
        onBasketTxt = fntBasket.render(onBasket,True,(0,0,0))
        textWidthFirst = onBasketTxt.get_width()
        screen.blit(onBasketTxt, ((bx+80)-textWidthFirst//2, 755))
        drawingLetters(fallingLets, fallingY)

        #calls showChart(). You lose half of your points though.        
        if helpRect.collidepoint(mx,my):
                screen.blit(helpIconDarker, (10, 50))
        if mb[0] == 1 and helpRect.collidepoint(mx,my):
           showChart()
           points = points//2

        #this is the action loop. Stuff happens here.
        for i in range(6):
            fallingY[i] += 2
            getTxtSize = fnt.render(fallingLets[i], True, (0, 0, 0))
            textWidth = getTxtSize.get_width()
            textHeight = getTxtSize.get_height()
            #credit to Noor
            #if a letter[i] collides with the basket and no action has been taken on it yet,
            if basketRect.collidepoint(i*200+85, fallingY[i]+15) and taken[i] == False: 
                #cover up the falling Korean character
                draw.rect(screen, (255,255,255), (i*200+85, fallingY[i], textWidth, textHeight))
                screen.blit(basket, (bx, 710))
                screen.blit(onBasketTxt, ((bx+80)-textWidthFirst//2, 755))
                #credit to Mr. Mac
                #fallingIndex is the index in the main Korean-list, of the collided fallingLet
                fallIndex = listFalling_koreanCh.index(fallingLets[i])
                if fallIndex == KoIndex:
                    screen.blit(correctTxt, (100, 100))
                    points += 100
                else:
                    screen.blit(incorrectTxt, (100, 100))
                    heart[2]+=80
                    lives += 1
                    #if the white heart-rect has covered up all the hearts:
                    if heart[2] == 1200:
                        gameOver()
                #now, some action has been taken on FallingLets[i].
                taken[i] = True
                #supposed to blit a white rect over the falling Letter, but doesn't work when the letter isn't colliding with the basket anymore.
                if taken[i] == True:
                    draw.rect(screen, (255,255,255), (i*200+85, fallingY[i], textWidth, textHeight))

        
        if lives == 5:
            gameOver(points, highscoreList)
                
        if taken[0] == taken[1] == taken[2] == taken[3] == taken[4] == taken[5] == False and fallingY[0] > 800 and fallingY[1] > 800 and fallingY[2] > 800 and fallingY[3] > 800 and fallingY[4] > 800 and fallingY[5] > 800:
            points -= 500
            
        if fallingY[0] > 800 and fallingY[1] > 800 and fallingY[2] > 800 and fallingY[3] > 800 and fallingY[4] > 800 and fallingY[5] > 800:
            fallingY = [- 100 + randint(-500, 0) for i in range(6)]
            onBasket = choice(listBasket_englishPh)
            KoIndex = listBasket_englishPh.index(onBasket)
            #if all the letters reach the bottom, they have to restart, and therefore they have to all turn into False
            #to show that no event has happened to them yet.
            taken = [False, False, False, False, False, False]
            fallingLets = makeFallingList(listFalling_koreanCh[KoIndex])

        #basically the second event loop. Stuff also happens here, but it's the repeat of the first one with different letters.                
        for i in range(6):        
            fallingY[i] += 2
            getTxtSize = fnt.render(fallingLets[i], True, (0, 0, 0))
            textWidth = getTxtSize.get_width()
            textHeight = getTxtSize.get_height()
            if basketRect.collidepoint(i*200+85, fallingY[i]+15):
                draw.rect(screen, (255,255,255), (i*200+85, fallingY[i], textWidth, textHeight))
                screen.blit(basket, (bx, 710))
                screen.blit(onBasketTxt, ((bx+80)-textWidthFirst//2, 755))
                fallIndex = listFalling_koreanCh.index(fallingLets[i])
                if fallIndex == KoIndex:
                    screen.blit(correctTxt, (100, 100))
                    points += 100
                else:
                    screen.blit(incorrectTxt, (100, 100))
                    
        draw.rect(screen, (255,255,255), heart)
        pointsTxt = fntBasket.render("%d" %(points),True,(0,0,0))
        screen.blit(scoreTxt, (0, 0))
        screen.blit(pointsTxt, (100, 0))

        myClock.tick(60)    
        display.flip()
        
gameIntro()
basketGame()


page = "menu"
while page != "exit":
    if page == "menu":
        page = start()
    if page == "concentration":
        page = concentrationIntro()
    if page == "c beginner":
        page = concentrationbeg()
    if page == "c intermediate":
        page = concentrationint()
    if page == "c advanced":
        page = concentrationadv()
    if page == "ultimate":
        page = concentrationult()
    if page == "speak korean":
        page = speakkoreanIntro()
    if page == "sk beginner":
        page = skbeginner()
    if page == "sk intermediate":
        page = skintermediate()
    if page == "sk advanced":
        page = skadvanced()
    if page == "concentration":
        page = concentration()
    if page == "basket game":
        page = gameIntro()
        page = basketGame()

quit()
    
