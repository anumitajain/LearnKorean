from pygame import *

intro = True
    while intro == True:
        for event in event.get():
            if event.type == QUIT:
                quit()
        chart = image.loat("chart.jpeg")
        screen.fill(255,255,255)
        screen.blit(chart, (100,100))
        fntBasket = font.SysFont("Comic Sans MS", 29, False, False)
        text1 = fntBasket.render("This chart shows you the Korean hangul and the matching English phenetic pronunciations.",True,(0,0,0))
        text2 = fntBasket.render("Take a good look at this chart if you want to do well!",True,(0,0,0))
        text3 = fntBasket.render("To access this chart, click the (icon). However, each time you do this, you'll lose half of your points.",True,(0,0,0))
        text4 = fntBasket.render("Happy catching!",True,(0,0,0))
        screen.blit(text1, (500, 100))
        screen.blit(text2, (500, 200))
        screen.blit(chart, (500, 240))
        screen.blit(text3, (500, 700))
        screen.blit(text4, (500, 800))
    display.flip()
    clock.tick(15)
quit()
