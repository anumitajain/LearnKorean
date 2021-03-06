#Basket game.
#Meghan Tran & Anumita Jain
from pygame import *
from random import *

font.init()
init()
screen = display.set_mode((1200, 800))
highscoreList = [0]

#IMAGES
basket = image.load("basketRealReal.jpg")
heartPic = image.load("heart.png")
helpIcon = image.load("help.jpg")
helpIconDarker = image.load("help_dark.jpg")

#FONT
fnt = font.Font("Cyberbit.ttf", 50)
fntBasket = font.SysFont("Comic Sans MS", 29, False, False)
correctTxt = fntBasket.render("Correct!",True,(0,0,0))
incorrectTxt = fntBasket.render("Incorrect!",True,(0,0,0))
scoreTxt = fntBasket.render("Score: ", True, (0,0,0))

listFalling_koreanCh = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
listBasket_englishPh = ["g/k", "n/n", "d/t", "r/l", "m/m", "b/p", "s/t", "-/ng", "j/t", "kk/k", "tt/-", "pp/-", "ss/t", "jj/-", "ch/t", "k/k", "t/t", "p/p", "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "eo", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"] 

#GAMEINTRO
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
            gameIntro()
            
        display.flip()
    return highscoreList

#BLITHIGHSCORE
def blitHighScore(highscore):
    fntScore = font.SysFont("Comic Sans MS", 40, False, False)
    highScore_Txt = fntScore.render("Highscore: %d" %(highscore),True,(0,0,0))
    
                                  
#MOVEBASKET
##bx = 0
def moveBasket(bx):
    keys = key.get_pressed()    
    if keys[K_LEFT] and bx >= 0:
        bx -= 7
    if keys[K_RIGHT] and bx < 1040:
        bx += 7
    return bx

#BLITLETTER
def blitLetter(wordsA):
    txtPic = fnt.render(wordsA[x],True,(0,0,0))
    return txtPic
    

#DRAWINGLETTERS
def drawingLetters(fallingLets,fallingY):
    for i in range(6):
##        if blitWhite == True:
##            draw.rect(screen, (255,255,255), (0, 0))
##        else:
        txtPic1 = fnt.render(fallingLets[i],True,(0,0,0))
        screen.blit(txtPic1, (i*200+85, fallingY[i]))

#MAKENEWLIST
def makeFallingList(let):
    fallingLets = [let]
    while len(fallingLets)<6:
        lets = choice(listFalling_koreanCh)
        if lets not in fallingLets:
            fallingLets.append(lets)
    shuffle(fallingLets)
    return fallingLets

#BASKETGAME
def basketGame():
    running=True
    bx = 0
    points = 0
    lives = 0
    listFalling_koreanCh = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
    listBasket_englishPh = ["g/k", "n/n", "d/t", "r/l", "m/m", "b/p", "s/t", "-/ng", "j/t", "kk/k", "tt/-", "pp/-", "ss/t", "jj/-", "ch/t", "k/k", "t/t", "p/p", "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "eo", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"] 
    onBasket = choice(listBasket_englishPh)
    KoIndex = listBasket_englishPh.index(onBasket) 
    onBasketTxt = fntBasket.render(onBasket,True,(0,0,0))
    fallingLets = []
    fallingLets.append(listFalling_koreanCh[KoIndex])

    myClock = time.Clock()

    while len(fallingLets)<6:        
        let = choice(listFalling_koreanCh)
        if let not in fallingLets:
            fallingLets.append(let)

    shuffle(fallingLets)

    fallingY = [randint(-500,0) for i in range(6)]

    heart = [800, 0, 0, 73]
    taken = [False, False, False, False, False, False]

    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
                
        mx, my = mouse.get_pos()
        mb = mouse.get_pressed()
        bx = moveBasket(bx)
        blitWhite = False
       
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

        if helpRect.collidepoint(mx,my):
                screen.blit(helpIconDarker, (10, 50))
        if mb[0] == 1 and helpRect.collidepoint(mx,my):
           showChart()
           points = points//2
        
        for i in range(6):
            fallingY[i] += 2
            getTxtSize = fnt.render(fallingLets[i], True, (0, 0, 0))
            textWidth = getTxtSize.get_width()
            textHeight = getTxtSize.get_height()
            if basketRect.collidepoint(i*200+85, fallingY[i]+15) and taken[i] == False:
                blitWhite = True
                draw.rect(screen, (255,255,255), (i*200+85, fallingY[i], textWidth, textHeight))
                screen.blit(basket, (bx, 710))
                screen.blit(onBasketTxt, ((bx+80)-textWidthFirst//2, 755))
                fallIndex = listFalling_koreanCh.index(fallingLets[i])
                if fallIndex == KoIndex:
                    screen.blit(correctTxt, (100, 100))
                    points += 100
                else:
                    screen.blit(incorrectTxt, (100, 100))
                    heart[2]+=80
                    lives += 1
                    if heart[2] == 1200:
                        gameOver()
                taken[i] = True
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
            taken = [False, False, False, False, False, False]
            fallingLets = makeFallingList(listFalling_koreanCh[KoIndex])
                        
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

quit()
