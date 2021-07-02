import pygame
from pygame.locals import *
import raquette
import constantes as c
import game
import balle

pygame.init()

ecran = pygame.display.set_mode(c.dimension_ecran)


while c.continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.flip()
pygame.quit()