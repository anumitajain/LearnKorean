#How to write Font
font.init() #initializes font
init()
comicFont=font.SysFont("Comic Sans MS",21) #selects font. You can set whatever var you want for it
                                          #We will be usining "Font" instead of "SysFont"
Font = font.SysFont("Arial Narrow", 25, False, False)# Another font
#once you have chosen your font, you need to make a stamp or picture of it
# textvar = fontvar.render("string you want to write", True, (colour))
perminstruct = Font.render("*Scroll up or down to increase or " , True, (0,0,0))
#Now blit it onto the screen
#screen.blit(textvar, (x,y))
screen.blit(instructnames[35],(536,662))



