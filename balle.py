"""dans le main
balle=b.Balle(...)
dans le while
    balle.show(ecran)
    
"""
import pygame as p
import constantes as c
import random

class Balle:
    def __init__(self, coords, longueurs):
        """"""        
        self.x=coords[0]
        self.y=coords[1]
        self.dx=longueurs[0] #largeur de la balle
        self.dy=longueurs[1] #hauteur de la balle
        self.deplX= c.vitesse_balle[0] #déplacement sur l'axe X
        self.deplY= c.vitesse_balle[1] #déplacement sur l'axe Y
    def show(self, ecran):
        p.draw.rect(ecran, c.couleur_blanc, (self.x, self.y, self.dx, self.dy))
    def deplacement(self):
        if self.y > (c.dimension_ecran[1]-self.dy): #si la balle cogne contre mur bas
            self.deplY = -abs(self.deplY) #déplacement sur l'axe Y
        if self.y < 0:
            self.deplY= abs(self.deplY)
        if self.x > (c.dimension_ecran[0]-self.dx):
            self.deplX= -abs(self.deplX)
        self.x += self.deplX
        self.y += self.deplY
    def coords_milieu_balle(self):
        """Renvoie les coordonnées du milieu de la balle sous forme de tuple"""
        return self.x + int(self.dx/2),self.y + int(self.dy/2)
            
