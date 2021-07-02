import pygame
from pygame.locals import *
import raquette as r
import constantes as c
import game as g
import balle as b

pygame.init()

ecran = pygame.display.set_mode(c.dimension_ecran)
raquette = r.Raquette((10,380),(c.largueur_raquette,c.longueur_raquette))

while c.continuer: 
    pygame.draw.rect(ecran, c.couleur_noire, (0,0,c.dimension_ecran[0],c.dimension_ecran[1])) #Fond
    raquette.show(ecran)
    for event in pygame.event.get():
        if event.type == QUIT:
            c.continuer = False
        if event.type == KEYDOWN:
            if event.key == K_UP:
                raquette.up(c.vitesse_raquette)
            if event.key == K_DOWN:
                raquette.down(c.vitesse_raquette)
    pygame.display.flip()
    
pygame.quit()