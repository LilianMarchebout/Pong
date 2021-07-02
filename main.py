import pygame as p
import raquette as r
import constantes as c
import game as g
import balle as b

p.init()

ecran = p.display.set_mode(c.dimension_ecran)
raquette = r.Raquette((10,380),(c.largueur_raquette,c.longueur_raquette))

while c.continuer: 
    p.draw.rect(ecran, c.couleur_noire, (0,0,c.dimension_ecran[0],c.dimension_ecran[1])) #Fond
    raquette.show(ecran)
    for event in p.event.get():
        if event.type == p.QUIT:
            c.continuer = False
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP:
                if raquette.y > 0:
                    raquette.up(c.vitesse_raquette)
            if event.key == p.K_DOWN:
                if raquette.y < c.dimension_ecran[1]-raquette.dy:
                    raquette.down(c.vitesse_raquette)
    p.display.flip()
    
p.quit()