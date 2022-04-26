import numpy as np
import pandas as pd 
import tkinter as tk
import random
import os

random.seed(1)
np.random.seed(1)


class Lieu : 
#Definition d'un Lieu avec point geometrique (x, y)

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, lieu_suivant):
    #Calcule la distance euclidienne entre le lieu(x1, y1) et le lieu suivant(x2, y2)
        dist = np.sqrt((self.x - lieu_suivant.x)**2 + (self.y - lieu_suivant.y)**2)

        return dist

class Graph :

    # Générer des lieux aléatoirement
    def __init__(self, LARGEUR, HAUTEUR, NB_LIEUX) :
        self.LARGEUR = LARGEUR
        self.HAUTEUR = HAUTEUR
        self.NB_LIEUX = NB_LIEUX
        self.liste_lieux = [Lieu(random.randint(0, LARGEUR), random.randint(0, HAUTEUR)) for _ in range(NB_LIEUX)]


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
