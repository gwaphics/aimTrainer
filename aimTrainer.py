# import modules
import pygame, random

pygame.init()
  
# Define the background color 
# using RGB color coding. 
background_colour = (0, 0, 0) 
  
# Define the dimensions of 
# screen object(width,height) 
win = pygame.display.set_mode((500,500)) 
  
# Set the caption of the screen 
pygame.display.set_caption('Aimworks') 
  
# Fill the background colour to the screen 
win.fill(background_colour) 
  
# Update the display using flip 
pygame.display.flip()

# Timer
counter, text = 15, '15'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('Consolas', 30)
titleFont = pygame.font.SysFont('Consolas', 50)

# Difficulty
difficulty = "easy"

radius = 45

# Class for the circle / target
class circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        
circle = circle(100, 100, radius)

# Define all position choices for circle to be in
# Pos num [X, Y, circle in position or not?]
# True = circle in spot | False = spot is open
pos1 = [83, 83, False]
pos2 = [249, 83, False]
pos3 = [415, 83, False]

pos4 = [83, 249, False]
pos5 = [249, 249, False]
pos6 = [415, 249, False]

pos7 = [83, 415, False]
pos8 = [249, 415, False]
pos9 = [415, 415, False]

positions = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9]

randPos1 = [83, 83, True]
randPos2 = [249, 83, True]
randPos3 = [415, 83, True]

# Choose random position for circle 1
def chooseRandPos1():
    global randPos1
    
    randPos1 = random.choice(positions)
    if randPos1[2] == True: # If position is taken choose another one
        chooseRandPos1()
    elif randPos1[2] == False: # If position is open then make it taken
        randPos1[2] == True

# Choose random position for circle 2
def chooseRandPos2():
    global randPos2
    
    randPos2 = random.choice(positions)
    if randPos2[2] == True:
        chooseRandPos2()
    elif randPos2[2] == False:
        randPos2[2] == True

# Choose random position for circle 3
def chooseRandPos3():
    global randPos3
    
    randPos3 = random.choice(positions)
    if randPos3[2] == True:
        chooseRandPos3()
    elif randPos3[2] == False:
        randPos3[2] == True
        
circle1Clicked = False
circle2Clicked = False
circle3Clicked = False

# Variable to keep our game loop running 
running = False
menu = True

bestScore = 0
score = 0

# menu screen
while menu:
    pygame.time.delay(100) #input delay
    mousex, mousey = pygame.mouse.get_pos() #get mouse cordinates on screen
    
    #Draws text to screen
    win.blit(titleFont.render("Aimworks", True, (255, 255, 255)), (150, 50))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu = False
        #Checks for mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #Mouse click commands here
            if mousex >= 185 and mousex <= 320 and mousey >= 220 and mousey <= 250:
                if difficulty == "easy":
                    difficulty = "medium"
                elif difficulty == "medium":
                    difficulty = "hard"
                elif difficulty == "hard":
                    difficulty = "easy"
            if mousex >= 160 and mousex <= 350 and mousey >= 400 and mousey <= 450:
                running = True
                menu = False
    
    text = "Best Score:"+str(bestScore)
    win.blit(font.render(text, True, (255, 255, 255)), (155, 110))
            
    if difficulty == "easy":
        radius = 45
        win.blit(font.render('  Easy  ', True, (0, 0, 0), (20, 155, 20)), (185, 220))
    if difficulty == "medium":
        radius = 35
        win.blit(font.render(' Medium ', True, (0, 0, 0), (20, 20, 155)), (185, 220))
    if difficulty == "hard":
        radius = 25
        win.blit(font.render('  Hard  ', True, (0, 0, 0), (155, 20, 20)), (185, 220))
        
    pygame.draw.circle(win, (155,155,155), (210, 270), 5)
    pygame.draw.circle(win, (155,155,155), (250, 270), 5)
    pygame.draw.circle(win, (155,155,155), (290, 270), 5)
        
    if difficulty == "easy":
        pygame.draw.circle(win, (255,255,255), (210, 270), 5)
    if difficulty == "medium":
        pygame.draw.circle(win, (255,255,255), (250, 270), 5)
    if difficulty == "hard":
        pygame.draw.circle(win, (255,255,255), (290, 270), 5)
        
    win.blit(titleFont.render(' Start ', True, (0, 0, 0), (255, 255, 255)), (160, 400))
    
    #Updates screen so text is displayed
    pygame.display.update()
    
  
# game loop 
while running:
    pygame.time.delay(100) #input delay
    mousex, mousey = pygame.mouse.get_pos() #get mouse cordinates on screen
    
    if difficulty == "easy":
        circle.radius = 45
    elif difficulty == "medium":
        circle.radius = 35
    elif difficulty == "hard":
        circle.radius = 25
    
    if counter <= 0:
        if score > bestScore:
            bestScore = score
        menu = True
        running = False
    
    if randPos1[0] == 83 and randPos1[1] == 83 or randPos2[0] == 83 and randPos2[1] == 83 or randPos3[0] == 83 and randPos3[1] == 83:
        pos1[2] = True
    else:
        pos1[2] = False
    if randPos1[0] == 249 and randPos1[1] == 83 or randPos2[0] == 249 and randPos2[1] == 83 or randPos3[0] == 249 and randPos3[1] == 83:
        pos2[2] = True
    else:
        pos2[2] = False
    if randPos1[0] == 415 and randPos1[1] == 83 or randPos2[0] == 415 and randPos2[1] == 83 or randPos3[0] == 415 and randPos3[1] == 83:
        pos3[2] = True
    else:
        pos3[2] = False

    if randPos1[0] == 83 and randPos1[1] == 249 or randPos2[0] == 83 and randPos2[1] == 249 or randPos3[0] == 83 and randPos3[1] == 249:
        pos4[2] = True
    else:
        pos4[2] = False
    if randPos1[0] == 249 and randPos1[1] == 249 or randPos2[0] == 249 and randPos2[1] == 249 or randPos3[0] == 249 and randPos3[1] == 249:
        pos5[2] = True
    else:
        pos5[2] = False
    if randPos1[0] == 415 and randPos1[1] == 249 or randPos2[0] == 415 and randPos2[1] == 249 or randPos3[0] == 415 and randPos3[1] == 249:
        pos6[2] = True
    else:
        pos6[2] = False

    if randPos1[0] == 83 and randPos1[1] == 415 or randPos2[0] == 83 and randPos2[1] == 415 or randPos3[0] == 83 and randPos3[1] == 415:
        pos7[2] = True
    else:
        pos7[2] = False
    if randPos1[0] == 249 and randPos1[1] == 415 or randPos2[0] == 249 and randPos2[1] == 415 or randPos3[0] == 249 and randPos3[1] == 415:
        pos8[2] = True
    else:
        pos8[2] = False
    if randPos1[0] == 415 and randPos1[1] == 415 or randPos2[0] == 415 and randPos2[1] == 415 or randPos3[0] == 415 and randPos3[1] == 415:
        pos9[2] = True
    else:
        pos9[2] = False
    
# for loop through the event queue   
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = str(counter).rjust(3)
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mousex >= randPos1[0] - radius and mousex <= randPos1[0] + radius and mousey >= randPos1[1] - radius and mousey <= randPos1[1] + radius:
                circle1Clicked = True
            if mousex >= randPos2[0] - radius and mousex <= randPos2[0] + radius and mousey >= randPos2[1] - radius and mousey <= randPos2[1] + radius:
                circle2Clicked = True
            if mousex >= randPos3[0] - radius and mousex <= randPos3[0] + radius and mousey >= randPos3[1] - radius and mousey <= randPos3[1] + radius:
                circle3Clicked = True
        
    # fills window color as black
    win.fill((0,0,0))
    
    # Checks if circle was clicked and will change that spot to open |
    # Then will choose a new random spot and draw out the circle
    
    # Circle 1
    if circle1Clicked == True:
        score += 1
        chooseRandPos1()
        circle1Clicked = False
    pygame.draw.circle(win, (255,0,0), (randPos1[0], randPos1[1]), circle.radius)
    
    # Circle 2
    if circle2Clicked == True:
        score += 1
        chooseRandPos2()
        circle2Clicked = False
    pygame.draw.circle(win, (255,0,0), (randPos2[0], randPos2[1]), circle.radius)
    
    # Circle 3
    if circle3Clicked == True:
        score += 1
        chooseRandPos3()
        circle3Clicked = False
    pygame.draw.circle(win, (255,0,0), (randPos3[0], randPos3[1]), circle.radius)
    
    
    # Draws the timer
    scoreText = str(score)
    win.blit(font.render(text, True, (255, 255, 255)), (220, 10))
    win.blit(font.render(scoreText, True, (255, 255, 255), (0, 0, 0)), (450, 10))
    
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
    
pygame.quit()

