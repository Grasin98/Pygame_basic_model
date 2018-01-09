# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 00:50:44 2018

@author: NISARG
"""

import pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
color=(0,0,255)

clock = pygame.time.Clock()
#crashed = False
carImg = pygame.image.load('C:/Users/NISARG/Pictures/racecar.png')

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()
    
    
def car(x,y):
    gameDisplay.blit(carImg, (x,y))
  
def message_display(text):
    largeText=pygame.font.Font("freesansbold.ttf",115)
    TextSurf,TextRect =text_objects(text,largeText)
    TextRect.center=((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update ()
    time.sleep(2)
    game_loop()
    
def things(thing_x,thing_y,thing_width,thing_height,thing_color):
    pygame.draw.rect(gameDisplay,color,[thing_x,thing_y,thing_width,thing_height])
   
def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("Dodged "+str(count),True,black)
    gameDisplay.blit(text,(0,0))    
    
        
def crash() :
    message_display("You Crashed")
    
def game_loop( ):
    
    gameExit=False
    x_change=0
    y_change=0
    car_width=73

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    
    thing_start_x =random.randrange(0,display_width)
    thing_start_y=-600
    thing_speed=3
    thing_width=100
    thing_height=100
    dodged=0
    
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                quit()
        
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                elif event.key==pygame.K_RIGHT:
                    x_change=5
                elif event.key==pygame.K_UP:
                    y_change=-5
                elif event.key==pygame.K_DOWN:
                    y_change=5
                
                
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or pygame.K_RIGHT:
                    x_change=0
                    y_change=0
                    
        x +=  x_change
        y +=  y_change
        gameDisplay.fill(white)
        things(thing_start_x,thing_start_y,thing_width,thing_height,color)
        
        thing_start_y+=thing_speed
        car(x,y)    
        things_dodged(dodged)
        
        if (x>display_width-car_width or x<0) or (y>display_width-car_width  or y<0):
            print("You crashed")
            crash()
            gameExit=True
        if thing_start_y > display_height:
            thing_start_y= 0-thing_height
            thing_start_x=random.randrange(0,display_width)
            dodged+=1
            thing_speed+=3
            #thing_width+=(dodged*1.2)    
            
        if y< thing_start_y+thing_height:
            print("y_crossover")
            
            if x >  thing_start_x and x< thing_start_x+thing_width or (x+car_width) >thing_start_x and (x+car_width)<thing_start_x+thing_width:
                print("x_crossover")
                crash()
            
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()

    