#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
from pygame import mixer
import random
import time
#initialize pygame
pygame.init()

screenX = 800
screenY = 500
screen = pygame.display.set_mode((screenX, screenY))

#colours
green = (0, 205, 0)
black = (0, 0, 0)
white = (250, 250, 250)
red = (180, 0, 0)
yellow = (250, 250, 0)
blue = (0, 0, 205)

#title
pygame.display.set_caption("Snake Game by Tony O.G")
icon = pygame.image.load("snake.png")
pygame.display.set_icon(icon)


#background sound
mixer.music.load("snake_jazz.wav")
mixer.music.play(-1)

snakebody = 10

#clock
clock = pygame.time.Clock()
  
#Message font set
font = pygame.font.SysFont(None, 30)


#Message prompt style
def prompt(msg, colour):
    message = font.render(msg, True, colour)
    screen.blit(message, [screenX/3 - 100, screenY/3 - 30])

#Score
def show_score(score_value):
    score = font.render("Score: " + str(score_value), True, yellow)
    screen.blit(score, (10, 10))
    
#snake object
def the_snake(snake_list, snakebody):
    for x in snake_list:
        pygame.draw.rect(screen,green,[x[0], x[1], snakebody, snakebody])
    

#game loop
def gameloop():
    snakeX = 150
    snakeY = 370
   
    snakeX_change = 0
    snakeY_change = 0
    
    snake_length = 1
    snake_list = list()
    snakebody = 10
 
    
    foodX = round(random.randrange(0, screenX - snakebody) / 10.0) * 10.0
    foodY = round(random.randrange(0, screenY - snakebody) / 10.0) * 10.0
    
    score_value = 0
    
    running = True
    game_over = False
    while running:
    
        #screen colour set
        screen.fill((150, 50, 50))
    
        while game_over == True:
        
            screen.fill(white)
            prompt("GAME OVER, press R to restart or Q to quit", blue)
            pygame.display.update()
        
            for events in pygame.event.get():
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_q:
                        running = False
                        game_over = False
                        
                    if events.key == pygame.K_r:
                        gameloop()
                    
                    
                     
        for event in pygame.event.get():
            #closing game code
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                running = False
            #keystroke event for checking keyboard input and moving snake
            if event.type == pygame.KEYDOWN:
                #ove = movement.get(event.key, move)
                if event.key == pygame.K_LEFT:
                    snakeX_change = -snakebody
                    snakeY_change = 0
                    #print("left arrow key has been pressed")
                elif event.key == pygame.K_RIGHT:
                    snakeX_change = +snakebody
                    snakeY_change = 0
                    #print("right arrow key has been pressed")
                elif event.key == pygame.K_UP:
                    snakeY_change = -snakebody
                    snakeX_change = 0
                     #print("up arrow key has been pressed")
                elif event.key == pygame.K_DOWN:
                    snakeY_change = +snakebody
                    snakeX_change = 0
                     #print("down arrow key has been pressed")
        
        
            if event.type == pygame.KEYUP:
                print("key has been released")
    
        #setting boundary
        if snakeX >= screenX-10 or snakeX <= 0 or snakeY >= screenY - 10 or snakeY <= 0:
            game_over = True
        snakeX += snakeX_change
        snakeY += snakeY_change
        
        #snake increase
        snake_head = list()
        snake_head.append(snakeX)
        snake_head.append(snakeY)
        snake_list.append(snake_head)
        
        if len(snake_list) > snake_length:
            del snake_list[0]
            
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
        
        the_snake(snake_list, snakebody)
        
        show_score(snake_length - 1)
        
        pygame.display.update()
    
        #food
        pygame.draw.rect(screen, black,[foodX, foodY, snakebody, snakebody])
        pygame.display.update()
        
        clock.tick(20)
         
        #snake eating food
        if snakeX == foodX and snakeY == foodY:
            foodX = round(random.randrange(0, screenX - snakebody) / 10.0) * 10.0 
            foodY = round(random.randrange(0, screenY - snakebody) /10.0) * 10.0 
            snake_length += 1
            score_value += 1
            
    pygame.quit()  
    quit()
    
gameloop()          
  


# In[ ]:




