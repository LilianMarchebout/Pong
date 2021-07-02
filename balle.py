"""dans le main
balle=b.Balle(...)
dans le while
    balle.show(ecran)
    

"""

class Balle:
    def __init__(self, coords, longueurs):
        """"""        
        self.x=coords[0]
        self.y=coords[1]
        self.dx=longueurs[0] #largeur de la balle
        self.dy=longueurs[1] #hauteur de la balle
        self.deplX=4 #déplacement sur l'axe X
        self.deplY=3 #déplacement sur l'axe Y
    def show(self, ecran):
        pygame.draw.rect(ecran, c.couleur_blanc, (self.x, self.y, self.dx, self.dy))
    def deplacement(self):
        if self.y>(c.dimension_ecran[1]-10): #si la balle cogne contre mur bas
            self.deplY=-3 #déplacement sur l'axe Y
        if self.y<0: #contre mur haut
            self.deplY=3
        if self.x>(c.dimension_ecran[0]-10):
            self.deplX=-4
        self.x+=self.dx
        self.y+=self.dy
            

    
    
        
