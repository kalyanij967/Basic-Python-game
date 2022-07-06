import pygame
pygame.init() #Initiating pygame

window=pygame.display.set_mode((900,700))#Setting up the window size of x-axis and y-axis using set and display is used to allow user to see the window
pygame.display.set_caption("my new game")#Giving name to the game window 

icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

spaceship=pygame.image.load("icon.png")
spaceship_x=200 #posiiton of image on x-axis
spaceship_y=300 #posiiton of image on y-axis

def display_spaceship(x,y):
    window.blit(spaceship,(x,y))#blit function helps in adding images to our window
bg=pygame.image.load("Background.jpg")

gameon=True
while gameon:
    window.blit(bg,(0,0))#Adding background image 

    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            gameon=False
    keys=pygame.key.get_pressed()
    # Adding conditions on key pressed 
    if keys[pygame.K_LEFT]:
        spaceship_x-=1
    if keys[pygame.K_RIGHT]:
        spaceship_x+=1
    if keys[pygame.K_UP]:
        spaceship_y-=1
    if keys[pygame.K_DOWN]:
        spaceship_y+=1

    display_spaceship(spaceship_x,spaceship_y)
    pygame.display.update()#Enabling user to close the window 

pygame.quit()
    

