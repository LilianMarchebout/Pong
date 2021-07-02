import pygame as p
import constantes as c
class Raquette:
    def __init__(self, coords, longueurs):
        self.x, self.y = coords[0], coords[1]
        self.dx, self.dy = longueurs[0], longueurs[1]
    def show(self, ecran):
        """Affiche la raquette à l'écran"""
        p.draw.rect(ecran, c.couleur_blanc, (self.x,self.y,self.dx,self.dy))
    def up(self, vitesse):
        """Change ses coordonnées lorsque la raquette va vers le haut"""
        if self.y > 0:
            self.y -= vitesse
    def down(self, vitesse):
        """Change ses coordonnées lorsque la raquette va vers le bas"""
        if self.y < c.dimension_ecran[1]-self.dy:
            self.y += vitesse
    def coords_milieu_raquette(self):
        """Renvoie les coordonnées du milieu de la raquette sous forme de tuple"""
        return self.x + int(self.dx/2),self.y + int(self.dy/2)
