import numpy as np
class Lieu :
    
    def __init__(self, coordonnee_X, coordonnee_Y):
        self.coordonnee_X = coordonnee_X
        self.coordonnee_Y = coordonnee_Y
    
    def distance_euclidienne(self,nouveau_lieu):
        distance = np.sqrt((self.coordonnee_X- nouveau_lieu.coordonnee_X)**2 + (self.coordonnee_Y - nouveau_lieu.coordonnee_Y))
        return distance

class Graph :
    def __init__(self) :
        liste_lieux = []
        largeur = 800
        hauteur = 600
        nb_lieux = 20
        matrice_od = []

    def calcul_matrice_cout_od(self):
        lieux = self.liste_lieux
        
        for i in range(len(self.coordonnee_X)):
            for j in range(len(self.coordonnee_X)):
                r[i, j] = self.distance_euclidienne()