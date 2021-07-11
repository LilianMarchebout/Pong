import math

def balle_raquette(balle, raquette):
    """Retourne si la balle touche la raquette"""
    return (raquette.x < balle.x < raquette.x+raquette.dx) and (raquette.y < balle.y < raquette.y+raquette.dy)

def frappe(balle, raquette):
    """Retourne le nouveau vecteur vitesse après que la balle ait touché la raquette"""
    impact_ref_raquette_y = raquette.coords_milieu_raquette()[1]-balle.coords_milieu_balle()[1]
    angle = math.sin(impact_ref_raquette_y/30*math.pi/2)
    return -balle.deplX, balle.deplY*angle*math.sqrt(5)
        