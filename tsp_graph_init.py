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

    # Créer la matrice euclidienne de chaque points 
    def calcul_matrice_cout_od(self):
        self.matrice_od = np.zeros((self.NB_LIEUX, self.NB_LIEUX))

        for i in range(self.nb_lieux):
            for j in range(self.NB_LIEUX):
                if i == j: break
                self.matrice_od[i][j] = Lieu.distance(self.liste_lieux[i], self.liste_lieux[j])
                self.matrice_od[i][j] = self.matrice_od[i][j]

        self.matrice_od = pd.DataFrame(self.matrice_od)

    