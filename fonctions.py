import math
import constantes as c

def balle_raquette(balle, raquette):
    """Retourne si la balle touche la raquette"""
    #return (raquette.x < balle.x < raquette.x+raquette.dx) and (raquette.y < balle.y < raquette.y+raquette.dy)
    return (balle.x < raquette.x+raquette.dx) and (raquette.y < balle.y < raquette.y+raquette.dy)

def frappe(balle, raquette):
    """Retourne le nouveau vecteur vitesse après que la balle ait touché la raquette"""
    #impact_ref_raquette_y = raquette.coords_milieu_raquette()[1]-balle.coords_milieu_balle()[1]
    a = angle(balle,raquette)
    return 3*math.sin(180-a), 3*math.cos(180-a)
        
def angle(balle,raquette):
    """"Retourne l'angle"""
    return (90/raquette.dy)*balle.coords_milieu_balle()[1]+(45-(90/raquette.dy)*(raquette.y+raquette.dy))
