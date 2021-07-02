import pygame
import time
from random import choice, randint
from pygame.locals import *
pygame.init()

blanc=(255, 255, 255)
noir=(0, 0, 0)


ecran=pygame.display.set_mode((600,400))
balle=pygame.draw.rect(ecran, (120,32,60),(100,100,10,10))

class Ball:
    def __init__(self):
        self.x=0
        self.y=0
        self.taille

x=randint(0,600)
y=randint(0,400)
#dx=choice([3, -3])
dx=4
dy=3

continuer=1
while continuer:
    pygame.draw.rect(ecran, noir,(0,0,600,400))    
    for event in pygame.event.get():
        if event.type==QUIT:
            continuer=0
    if y>390:
        dy=-3
    if y<0:
        dy=3
    if x>590:
        dx=-4    
    x+=dx   
    y+=dy    
    balle=pygame.draw.rect(ecran, blanc,(x,y,10,10))    
    pygame.display.flip()
    time.sleep(0.01)
pygame.quit()
