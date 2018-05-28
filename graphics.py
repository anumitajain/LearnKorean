#LAnguage learning project
#modes: start page, beginner, intermediate, advanced
#help page/instructions, concentration, falling words
#Anumita Jain and Meghan Tran
#-----------------------------------------------
from pygame import *
from random import *
import speech_recognition as sr
import time
#-----------------------------------------------
font.init()
init()
Fontt = font.SysFont("Comic Sans MS", 20, False, False)
smallfont = font.SysFont("Comic Sans MS", 15, False, False)
screen = display.set_mode((1200,800))
screen.fill((255, 255, 255))
#------------------------------------------------
#FONT LOADING
correct = Fontt.render("Correct!", True, (0, 255, 0))
incorrect = Fontt.render("Incorrect!", True, (255, 0, 0))
Pronounce= Fontt.render("Try to pronounce this word.", True, (0,0,0))
startRecording = Fontt.render("^CLICK to start recording.", True, (0,0,0))
NoUnderstand = smallfont.render("Google Speech Recognition could not understand audio.", True, (0,0,0))

#IMAGE LOADING
blueArrowPic = image.load("blueArrow.png")    
micPic = image.load("micPic.jpg")
heartPic = image.load("heart.png")
gameOver = image.load("game over.png")

#RECTS
beginnerRect = Rect(80, 200, 500, 120)
micRect = Rect(530, 300, 140, 140)
KtxtRect = Rect(400, 150, 400, 100)
correctRect = Rect(500, 600, 200, 50)
statusRect = Rect(400, 480, 400, 80)
incorrectRect = Rect(500, 600, 200, 50)
    
#------------------------------------------------------
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
    

#-----------------------------------------------
fnt = font.Font("cyberbit.ttf",60)
words = ["안녕","여보세요","내 이름은","잘 지냈어요"]
definitions =["hi, bye","hello","My name is", "How are you"]
running= True
click = False
heart = [880, 0, 0, 73]
a = randint(0,3)
txtPic = fnt.render(words[a],True,(0,0,0))

while running:
    recording = False
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == MOUSEBUTTONDOWN:
            click = True
            if e.button == 1:
                linePic = screen.copy()
                lineStartx,lineStarty = e.pos

    mb = mouse.get_pressed()
    mx, my = mouse.get_pos()
    screen.fill((255,255,255))
    screen.blit(Pronounce, (400, 120))
    screen.blit(startRecording, (465, 442))
    screen.blit(blueArrowPic, (300, 150))
    screen.blit(micPic, (530, 300))
    screen.blit(txtPic,(400,150))
    draw.rect(screen, (0), micRect, 2)
    draw.rect(screen, (0), KtxtRect, 2)
    draw.rect(screen, (0), statusRect, 2)
    screen.blit(heartPic, (880, 0))
    screen.blit(heartPic, (960, 0))
    screen.blit(heartPic, (1040, 0))
    screen.blit(heartPic, (1120, 0))
    
    if micRect.collidepoint(mx,my):
        if mb[0] == 1:
            recording = True  
            draw.rect(screen, (255,255,255), (465,442, 303, 30))
            recordnotif = Fontt.render("Recording...", True, (0,0,0))
            screen.blit(recordnotif,(465,442))
            string = record()
            spokentext = fnt.render(string, True, (0,0,0))
            screen.blit(spokentext, (400,465))
            if string == words[a]:
                screen.blit(correct, (500, 600))
                display.flip()
                time.sleep(2)
                draw.rect(screen, (255,255,255), incorrectRect)
                break
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
                    heart[2]+=80
                    draw.rect(screen, (255,255,255), heart)
                    #b = randint(0,3)
                    #txtPic2 = fnt.render(words[b],True,(0,0,0))
                   # screen.blit(txtPic2,(400,150))
                    
        else:
            recording = False
            draw.rect(screen, (255,255,255), (465,442, 303, 30))
            screen.blit(startRecording, (465, 442))
                    
                
                
#-------------------------------------------------
    

#--------------------------------------------------
    display.flip()
quit()

