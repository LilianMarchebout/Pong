import pygame
from pygame.locals import *
import raquette
import constantes
import game
import balle

pygame.init()

ecran = pygame.display.set_mode(constantes.dimension_ecran)
continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
    pygame.display.flip()
pygame.quit()