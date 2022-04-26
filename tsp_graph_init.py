import numpy as np
class Lieu :
    
    def __init__(self, coordonnee_X, coordonnee_Y):
        self.coordonnee_X = coordonnee_X
        self.coordonnee_Y = coordonnee_Y
    
    def distance_euclidienne(self,nouveau_lieu):
        distance = np.sqrt((self.coordonnee_X- nouveau_lieu.coordonnee_X)**2 + (self.coordonnee_Y - nouveau_lieu.coordonnee_Y))
        return distance

class Graph :
    def __init__(self,liste_lieux) :
        self.liste_lieux = liste_lieux
        largeur = 800
        hauteur = 600
        nb_lieux = 20
        matrice_od = []

    def calcul_matrice_cout_od(self):
        lieux = len(self.liste_lieux)
        distance_matrice = np.ones((lieux,lieux))
        for i,lieu1 in enumerate(self.liste_lieux):
            for j, lieu2 in enumerate(self.liste_lieux):
                distance_matrice[i, j] = lieu1.distance_euclidienne(lieu2)

        self.matrice_cout_od = distance_matrice

        return distance_matrice

    def plus_proche_voisin(self,lieu,matrice_od):
        self.le_plus_proche_voisin = np.argmin(matrice_od[lieu])
        return self.le_plus_proche_voisin
        






lieu = Lieu(50, 100)

lieu2 = Lieu(100, 100)

dist = lieu.distance_euclidienne(lieu2)

graph = Graph([lieu,lieu2])
mat = graph.calcul_matrice_cout_od()
print("ok")