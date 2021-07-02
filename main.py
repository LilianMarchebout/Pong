import pygame
from pygame.locals import *
import raquette as r
import constantes as c
import game as g
import balle as b

pygame.init()

ecran = pygame.display.set_mode(c.dimension_ecran)
raquette = r.Raquette((0,0),(c.largueur_raquette,c.longueur_raquette))

while c.continuer: 
    raquette.show(ecran)
    for event in pygame.event.get():
        if event.type == QUIT:
            c.continuer = False
    pygame.display.flip()
    
pygame.quit()