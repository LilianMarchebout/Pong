import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((300*2,200*2), pygame.RESIZABLE)
pos_rec = [300, 200]
v = 10
continuer = True
while continuer:
    pygame.draw.rect(ecran, (0,0,0), (0,0, 600, 400))
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_rec[0] -= v
            if event.key == pygame.K_RIGHT:
                pos_rec[0] += v
            if event.key == pygame.K_UP:
                pos_rec[1] -= v
            if event.key == pygame.K_DOWN:
                pos_rec[1] += v
    rec = pygame.draw.rect(ecran, (255,255,255), (pos_rec[0],pos_rec[1],10,10))        
    pygame.display.flip()    
pygame.quit()