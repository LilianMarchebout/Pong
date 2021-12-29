_import pygame as p
import raquette as r
import constantes as c
import balle as b
import time
import fonctions as f


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
    if f.balle_raquette(balle,raquette): #s'il y a impact 
        balle.deplX, balle.deplY = f.frappe(balle,raquette)
        #print(f.angle(balle,raquette))
        #print(raquette.x, balle.x, raquette.x+raquette.dx)
        #print(raquette.y, balle.y, raquette.y+raquette.dy)
        
        #c.t /= 1.1 #ajoute de la vitesse à la balle
    #Actualise
    raquette.show(ecran)
    balle.show(ecran)
    p.display.flip()
    time.sleep(0.01)
    c.t += 1

p.quit()