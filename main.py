import pygame as p
import raquette as r
import constantes as c
import game as g
import balle as b
import time

p.init()

ecran = p.display.set_mode(c.dimension_ecran)

#Creation des objets 
raquette = r.Raquette(c.coordonnees_raquette_initiales,(c.largueur_raquette,c.longueur_raquette))
balle = b.Balle(c.coordonnes_balle_initiales, (c.taille_balle,c.taille_balle))

while c.continuer: 
    p.draw.rect(ecran, c.couleur_noire, (0,0,c.dimension_ecran[0],c.dimension_ecran[1])) #Fond
    for event in p.event.get():
        if event.type == p.QUIT:
            c.continuer = False
        #Action de la raquette
        if event.type == p.KEYDOWN:
            if event.key == p.K_UP: #Haut
                raquette.up(c.vitesse_raquette)
            if event.key == p.K_DOWN: #Bas
                raquette.down(c.vitesse_raquette)
    #Action de la balle
    balle.deplacement()
    #Actualise
    raquette.show(ecran)
    balle.show(ecran)
    p.display.flip()
    time.sleep(0.01)
    
p.quit()