#Zara F - Assignment 18 - Catch the Dot Game - ICS3U
#setup
import pygame
import random
import math
pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Move the Square")
clock = pygame.time.Clock()

x, y = 300, 200
speed = 5
score = 0
speedup = 0

#score text
scoretext = "Score: " + str(score)
scorefont = pygame.font.SysFont("tahoma", 20) #get font settings ready
textsurface = scorefont.render(scoretext, False, (255,255,255)) #text, no antialiasing, white text colour
screen.blit(textsurface,(0,0)) #put text surface onto normal screen

# dot placement
def dotcolour():
    #random dot colour
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    #make sure colours aren't so dark they blend into the background (by setting one rgb value to max)
    whichrgb = random.randint(1,3)
    if whichrgb ==1:
        r=255
    elif whichrgb == 2:
        g=255
    else:
        b=255
    return r,g,b

def dotloc():
    #dot location
    dotx = random.randint(20,580)
    doty = random.randint(20,380)
    return dotx,doty

dotcent = dotloc()
dotcol = dotcolour()
pygame.draw.circle(screen, dotcol, dotcent, 10) #make dot

#main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  
#arrow presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
#keeping square on screen
    if x > 560:
        x=560
    if x < 0:
        x=0
    if y > 360:
        y=360
    if y < 0:
        y=0
#cover previous frame and put new square position
    screen.fill((0, 0, 0)) #black screen
    pygame.draw.circle(screen, dotcol, dotcent, 10) #show dot again    
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 40, 40)) #screen, colours, coords + sizes
    screen.blit(textsurface,(0,0)) #put text surface onto normal screen again
    pygame.display.update() #show new screen
    clock.tick(60 + (speedup*10)) #make sure square doesn't move too fast + add speed every 5 points

    squarecent = (x+20,y+20) #get square center
    
    if math.dist(squarecent,dotcent)<30: #if aquare center <30 pixels from dot center
        score+=1 #raise score
        scoretext = "Score: " + str(score) #update text variable
        textsurface = scorefont.render(scoretext, False, (255,255,255)) #show updated text
        dotcent = dotloc() #change dot location
        dotcol = dotcolour() #change dot colour
        pygame.draw.circle(screen, dotcol, dotcent, 10) #draw new dot
        if score!= 0 and score%5 ==0: #if score divisible by 5 and isn't 0
            speedup +=1 #increase speed increasing variable
        
pygame.quit()
