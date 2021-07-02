import pygame
class Raquette:
    def __init__(self, coords, longueurs):
        self.x, self.y = coords[0], coords[1]
        self.dx, self.dy = longueurs[0], longueurs[1]
    def show(self, ecran):
        """Affiche la raquette à l'écran"""
        pygame.draw.rect(ecran, (0,0,0), (self.x,self.y,self.dx,self.dy))
    def up(self, vitesse):
        """Change ses coordonnées lorsque la raquette va vers le haut"""
        self.y -= vitesse
        self.dy -= vitesse
    def down(self, vitesse):
        """Change ses coordonnées lorsque la raquette va vers le bas"""
        self.y += vitesse
        self.dy += vitesse
