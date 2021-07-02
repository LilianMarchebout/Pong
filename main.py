import pygame as p
import raquette as r
import constantes as c
import game as g
import balle as b
import time

def balle_raquette(balle, raquette):
    """Retourne si la balle touche la raquette"""
    #return (raquette.x < balle.x < raquette.x+raquette.dx) and (raquette.y < balle.y < raquette.y+raquette.dy)
    return raquette.x == balle.x and raquette.y < balle.y < raquette.y+raquette.dy
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
    if balle.x < 0:
        c.continuer = False
    if balle_raquette(balle,raquette): 
        balle.deplX= c.vitesse_balle[0] #Marche pas
    #Actualise
    raquette.show(ecran)
    balle.show(ecran)
    p.display.flip()
    time.sleep(0.01)

p.quit()