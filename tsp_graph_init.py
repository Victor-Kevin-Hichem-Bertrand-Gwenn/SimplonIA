import numpy as np
from random import randint
import random 

# Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter.
# La classe disposera d'une fonction de calcul de distance euclidienne entre 2 lieux.
class Lieu:
    lieu_liste = []

    def __init__ (self, x, y, lieu_liste=[]):
        # x, y = coordonnées du lieu
        self.x = x 
        self.y = y      
        Lieu.lieu_liste = lieu_liste   

    def lieu (x, y):
        lieu_liste = []
        lieu_liste.append(x)
        lieu_liste.append(y)
        return lieu_liste

    def distance(x,y):
            # retourne la distance euclidienne de x et de y
        dis = np.sqrt(np.sum((x-y)**2))
        return dis 


    def distance_2_lieux (x1, y1, x2, y2):
        # calcul distance euclidienne entre les 2 lieux
        dis = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(dis)
        return dis




# Cette classe est utilisée pour mémoriser une liste de lieux (variable liste_lieux).
class Graph :

    def __init__(self, liste_lieux, nb_lieux=20, largeur=800, hauteur=600):
        self.nb_lieux = nb_lieux 
        self.liste_lieux = liste_lieux 
        self.hauteur = hauteur
        self.largeur = largeur 

    # méthode pour lister les lieux : on ajoute aléatoirement des coordonnées
    def lister_lieu():
        nb_lieux=20
        largeur=800
        hauteur=600
        # création d'une liste_lieux avec x et y aléatoires
        for lieu in range(nb_lieux):
            x = randint(0, largeur)
            y = randint(0, hauteur)
            ajout = Lieu.lieu(x, y)
            Lieu.lieu_liste.append(ajout)
    

# liste des lieux
Graph.lister_lieu()
# affichage de la liste
print(Lieu.lieu_liste)
print("_____________________")

# récupérer x et y pour chaque lieu
for coordonnees in Lieu.lieu_liste :
    print(coordonnees)

