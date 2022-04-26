import numpy as np
import pandas as pd
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
    nb_lieux = 20

    def __init__(self, liste_lieux,largeur=800, hauteur=600):
        self.liste_lieux = liste_lieux 
        self.hauteur = hauteur
        self.largeur = largeur 

    # méthode pour lister les lieux : on ajoute aléatoirement des coordonnées
    def lister_lieu():
        largeur=800
        hauteur=600
        # création d'une liste_lieux avec x et y aléatoires
        for lieu in range(Graph.nb_lieux):
            x = randint(0, largeur)
            y = randint(0, hauteur)
            ajout = Lieu.lieu(x, y)
            Lieu.lieu_liste.append(ajout)
        print(Lieu.lieu_liste)

    def dataframe():
            # numérotation des lieux 
            # nb_lieux=20
            index_lieux = []
            for element in range(1, Graph.nb_lieux+1):
                index_lieux.append(element)
            # convertir en dataframe
            data = Lieu.lieu_liste
            lieux = index_lieux
            df = pd.DataFrame(data, columns=['x', 'y'], index=lieux)
            # sauvegarde du df
            df.to_csv (r"C:\Users\utilisateur\Documents\microsoft_ia\Cahier d'apprentissage\Projets\projet_isen\script\df.csv", index = False, header=True)
            # chargement du df
            load = pd.read_csv('df.csv')
            print(load)

    # def save_csv():
    #     df.to_csv (r"C:\Users\utilisateur\Documents\microsoft_ia\Cahier d'apprentissage\Projets\projet_isen\script\df.csv", index = False, header=True)

    # def load_csv():
    #     load = pd.read_csv('df.csv')




        





