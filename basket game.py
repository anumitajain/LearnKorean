#Basket game.
#Meghan Tran & Anumita Jain
from pygame import *
from random import *

font.init()
init()
screen = display.set_mode((1200, 800))


#IMAGES
basket = image.load("basket.jpg")
heartPic = image.load("heart.png")
screen.blit(heartPic, (880, 0))
screen.blit(heartPic, (960, 0))
screen.blit(heartPic, (1040, 0))
screen.blit(heartPic, (1120, 0))

#FONT
fnt = font.Font("Cyberbit.ttf", 50)
fntBasket = font.SysFont("Comic Sans MS", 29, False, False)
correctTxt = fntBasket.render("Correct!",True,(0,0,0))
incorrectTxt = fntBasket.render("Incorrect!",True,(0,0,0))
 

#RECTS
newRect = Rect(0, 799, 1200, 1) 

#MOVEBASKET
bx = 0
def moveBasket(bx):
    keys = key.get_pressed()    
    if keys[K_LEFT] and bx >= 10:
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
        if blitWhite == True:
            draw.rect(screen, (255,255,255), (0, 0))
        else:
            txtPic1 = fnt.render(fallingLets[i],True,(0,0,0))
            screen.blit(txtPic1, (i*200+85, fallingY[i]))

#MAKENEWLIST
def makeFallingList(let):
    fallingLets = [let]
    while len(fallingLets)<6:
        let = choice(listFalling_koreanCh)
        if let not in fallingLets:
            fallingLets.append(let)
    shuffle(fallingLets)
    return fallingLets
        
#RUNNING LOOP    
running=True
ty = 0
points = 0
state = "meh"
listFalling_koreanCh = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ", "ㅂ", "ㅅ", "ㅇ", "ㅈ", "ㄲ", "ㄸ", "ㅃ", "ㅆ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ", "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"]
listBasket_englishPh = ["g/k", "n/n", "d/t", "r/l", "m/m", "b/p", "s/t", "-/ng", "j/t", "kk/k", "tt/-", "pp/-", "ss/t", "jj/-", "ch/t", "k/k", "t/t", "p/p", "h/h", "a", "ae", "ya", "yae", "eo", "e", "yeo", "ye", "o", "wa", "wae", "eo", "yo", "u", "wo", "we", "wi", "yu", "eu", "ui", "i"] 
#if you get listBasket_englishPh[0:18] wrong, we should put a hint saying: "Remember, in listBasket_englishPh[0], it sounds like a g when it's on top of the vowel, but like a k when on the bottom." 
onBasket = choice(listBasket_englishPh)
KoIndex = listBasket_englishPh.index(onBasket) 
onBasketTxt = fntBasket.render(onBasket,True,(0,0,0))
lenOnBasket = 80 - int(len(onBasket)//2)*15
fallingLets = []
fallingLets.append(listFalling_koreanCh[KoIndex])

myClock = time.Clock()

while len(fallingLets)<6:        
    let = choice(listFalling_koreanCh)
    if let not in fallingLets:
        fallingLets.append(let)

shuffle(fallingLets)

fallingY = [randint(-500,0) for i in range(6)]

heart = [880, 0, 0, 73]
taken = [False, False, False, False, False, False]
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False            
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    bx = moveBasket(bx)
    blitWhite = False
    
    basketRect = Rect(bx, 639, 160, 160)
    
    screen.fill((255,255,255))
    screen.blit(heartPic, (880, 0))
    screen.blit(heartPic, (960, 0))
    screen.blit(heartPic, (1040, 0))
    screen.blit(heartPic, (1120, 0))
    draw.rect(screen,(255,255,255),basketRect,2)
    screen.blit(basket, (bx, 640))
    onBasketTxt = fntBasket.render(onBasket,True,(0,0,0)) #Errors: If fallingY[i] is the same for more than 1 i's they both blitWhite
    screen.blit(onBasketTxt, (bx+lenOnBasket, 640+78))
##    draw.rect(screen, (255,5,255), newRect)
    drawingLetters(fallingLets, fallingY)

    for i in range(6):
        fallingY[i] += 3
        getTxtSize = fnt.render(fallingLets[i], True, (0, 0, 0))
        textWidth = getTxtSize.get_width()
        textHeight = getTxtSize.get_height()
        if basketRect.collidepoint(i*200+85, fallingY[i]+15) and taken[i] == False:
            blitWhite = True
            draw.rect(screen, (255,255,255), (i*200+85, fallingY[i], textWidth, textHeight))
            screen.blit(basket, (bx, 640))
            screen.blit(onBasketTxt, (bx+lenOnBasket, 640+78))
            fallIndex = listFalling_koreanCh.index(fallingLets[i])
            if fallIndex == KoIndex:
                screen.blit(correctTxt, (100, 100))
                points += 100
            else:
                screen.blit(incorrectTxt, (100, 100))
                heart[2]+=80
            taken[i] = True
             
                
    if fallingY[0] > 800 and fallingY[1] > 800 and fallingY[2] > 800 and fallingY[3] > 800 and fallingY[4] > 800 and fallingY[5] > 800:
        fallingY = [- 100 + randint(-500, 0) for i in range(6)]
        onBasket = choice(listBasket_englishPh)
        KoIndex = listBasket_englishPh.index(onBasket)
        taken = [False, False, False, False, False, False]
        fallingLets = makeFallingList(listFalling_koreanCh[KoIndex])
                    
    for i in range(6):        
        fallingY[i] += 3
        getTxtSize = fnt.render(fallingLets[i], True, (0, 0, 0))
        textWidth = getTxtSize.get_width()
        textHeight = getTxtSize.get_height()
        if basketRect.collidepoint(i*200+85, fallingY[i]+15):
            draw.rect(screen, (255,255,255), (i*200+85, fallingY[i], textWidth, textHeight))
            screen.blit(basket, (bx, 640))
            screen.blit(onBasketTxt, (bx+lenOnBasket, 640+78))
            fallIndex = listFalling_koreanCh.index(fallingLets[i])
            if fallIndex == KoIndex:
                screen.blit(correctTxt, (100, 100))
                points += 100
            else:
                screen.blit(incorrectTxt, (100, 100))
                
    draw.rect(screen, (255,255,255), heart)
    pointsTxt = fntBasket.render("%d" %(points),True,(0,0,0))
    screen.blit(pointsTxt, (0, 0))
                   
                           
    print(fallingLets)
    print(KoIndex)
    print(fallingY)

    
    myClock.tick(60)    
    display.flip()
quit()
    
