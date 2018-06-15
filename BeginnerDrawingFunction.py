#drawbeginner
#attempt to sseperate drawing and user input analysis
#did not work out
from pygame import *
from random import *
import speech_recognition as sr
import time
font.init()
init()
Fontt = font.SysFont("Comic Sans MS", 20, False, False)
smallfont = font.SysFont("Comic Sans MS", 15, False, False)
screen = display.set_mode((1200,800))
#screen.fill((255, 255, 255))

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


def drawbeginner(screen,words,w,string,recording, heart):
    fnt = font.Font("cyberbit.ttf",60)
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
    txtPic = fnt.render(words[w],True,(0,0,0)) #This only picks one word and only resets when the code loops

    #Font and word stuff
    
    definitions =["hi, bye","hello","My name is", "How are you"]
    #word = randint(0,3) #picks the word in the list
    
    #heart = [880, 0, 0, 73]

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

    
    draw.rect(screen, (0), micRect, 2)
    draw.rect(screen, (0), KtxtRect, 2)
    draw.rect(screen, (0), statusRect, 2)

    if string == words[w]:
        screen.blit(correct, (500, 600))
        display.flip()
        time.sleep(2)
        draw.rect(screen, (255,255,255), incorrectRect)
    else:
        if heart[2] == 320:
                screen.blit(gameOver, (0, 0))
        else:
            if string != "":
                screen.blit(incorrect, (500, 600))
                display.flip()
                time.sleep(2)
                draw.rect(screen, (255,255,255), statusRect)
                draw.rect(screen, (0,0,0), statusRect, 2)
                draw.rect(screen, (255,255,255), incorrectRect)
                draw.rect(screen, (255,255,255), heart)

    if recording == True:
        draw.rect(screen, (255,255,255), (465,442, 303, 30))
        recordnotif = Fontt.render("Recording...", True, (0,0,0))
        screen.blit(recordnotif,(465,442))
        spokentext = fnt.render(string, True, (0,0,0))
        screen.blit(spokentext, (400,465))
        if string == words[w]:
            screen.blit(correct, (500, 600))
            display.flip()
            time.sleep(2)
            draw.rect(screen, (255,255,255), incorrectRect)
        else:
            if heart[2] == 320:
                screen.blit(gameOver, (0, 0))
            else:
                screen.blit(incorrect, (500, 600))
                display.flip()
                time.sleep(2)
                draw.rect(screen, (255,255,255), statusRect)
                draw.rect(screen, (0,0,0), statusRect, 2)
                draw.rect(screen, (255,255,255), incorrectRect)
                draw.rect(screen, (255,255,255), heart)

    else:
        draw.rect(screen, (255,255,255), (465,442, 303, 30))
        screen.blit(startRecording, (465, 442))

    
        
    #if recording == True:
##        draw.rect(screen, (255,255,255), (465,442, 303, 30))
##        recordnotif = Fontt.render("Recording...", True, (0,0,0))
##        screen.blit(recordnotif,(465,442))
##        spokentext = fnt.render(string, True, (0,0,0))
##        screen.blit(spokentext, (400,465))
##        if string == words[w]:
##            
##        else:
##            if heart[2] == 320:
##                screen.blit(gameOver, (0, 0))
##            else:
##                screen.blit(incorrect, (500, 600))
##                display.flip()
##                time.sleep(2)
##                draw.rect(screen, (255,255,255), statusRect)
##                draw.rect(screen, (0,0,0), statusRect, 2)
##                draw.rect(screen, (255,255,255), incorrectRect)
##                heart[2]+=80
##                draw.rect(screen, (255,255,255), heart)
##    else:
##        recording = False
##        draw.rect(screen, (255,255,255), (465,442, 303, 30))
##        screen.blit(startRecording, (465, 442))

    display.flip()


def beginner():
    #Font and word stuff
    fnt = font.Font("cyberbit.ttf",60)
    words = ["안녕","여보세요","내 이름은","잘 지냈어요"]
    definitions =["hi, bye","hello","My name is", "How are you"]
    w = randint(0,3) #picks the word in the list
    heart = [880, 0, 0, 73]
    string = ""

    correct = Fontt.render("Correct!", True, (0, 255, 0))
    incorrect = Fontt.render("Incorrect!", True, (255, 0, 0))
    Pronounce= Fontt.render("Try to pronounce this word.", True, (0,0,0))
    startRecording = Fontt.render("^CLICK to start recording.", True, (0,0,0))
    NoUnderstand = smallfont.render("Google Speech Recognition could not understand audio.", True, (0,0,0))
    
    #RECTS
    beginnerRect = Rect(80, 200, 500, 120)
    micRect = Rect(530, 300, 140, 140)
    KtxtRect = Rect(400, 150, 400, 100)
    correctRect = Rect(500, 600, 200, 50)
    statusRect = Rect(400, 480, 400, 80)
    incorrectRect = Rect(500, 600, 200, 50)

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
        drawbeginner(screen,words,w,string,recording, heart)
##        draw.rect(screen, (0), micRect, 2)
##        draw.rect(screen, (0), KtxtRect, 2)
##        draw.rect(screen, (0), statusRect, 2)
        
        if micRect.collidepoint(mx,my)and mb[0] == 1:
            recording = True #add to function if making
            drawbeginner(screen,words,w,string,recording, heart)
            #draw.rect(screen, (255,255,255), (465,442, 303, 30))
            #recordnotif = Fontt.render("Recording...", True, (0,0,0))
            #screen.blit(recordnotif,(465,442))
            string = record() #add to function if making
            ###drawbeginner(screen,words,w,string,recording, heart)
            #spokentext = fnt.render(string, True, (0,0,0))
            #screen.blit(spokentext, (400,465))
            if string == words[w]: #word needs to be added too
                #drawbeginner(screen,words,w,string,recording, heart)
##                screen.blit(correct, (500, 600))
##                display.flip()
##                time.sleep(2)
##                draw.rect(screen, (255,255,255), incorrectRect)
                break
            else:
                heart[2]+=80
                #drawbeginner(screen,words,w,string,recording, heart)
##                if heart[2] == 320: #so does heart
##                    screen.blit(gameOver, (0, 0))
##                else:
##                    screen.blit(incorrect, (500, 600))
##                    display.flip()
##                    time.sleep(2)
##                    draw.rect(screen, (255,255,255), statusRect)
##                    draw.rect(screen, (0,0,0), statusRect, 2)
##                    draw.rect(screen, (255,255,255), incorrectRect)
##                    heart[2]+=80
##                    draw.rect(screen, (255,255,255), heart)
                    #b = randint(0,3)
                    #txtPic2 = fnt.render(words[b],True,(0,0,0))
                   # screen.blit(txtPic2,(400,150))
                        
        else:
            recording = False
            drawbeginner(screen,words,w,string,recording, heart)
##            recording = False
##            draw.rect(screen, (255,255,255), (465,442, 303, 30))
##            screen.blit(startRecording, (465, 442))

        display.flip()
    return "beginner"

page = "beginner"

while page != "exit":
    if page == "beginner":
        beginner()

quit()


