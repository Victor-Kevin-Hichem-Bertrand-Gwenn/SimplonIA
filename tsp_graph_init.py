import numpy as np
import pandas as pd
from random import randint
import random 



# Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter.
# La classe disposera d'une fonction de calcul de distance euclidienne entre 2 lieux.
class Lieu:
    lieu_liste = []

    def __init__ (self, x, y):
        # x, y = coordonnées du lieu
        self.x = x 
        self.y = y      
        # Lieu.lieu_liste = lieu_liste   

    def lieu (x, y):
        # lieu_liste = []
        Lieu.lieu_liste.append(x)
        Lieu.lieu_liste.append(y)
        return Lieu.lieu_liste

    # def distance(x,y):
    #         # retourne la distance euclidienne de x et de y
    #     dis = np.sqrt(np.sum((x-y)**2))
    #     return dis 

    def distance_2_lieux (x1, y1, x2, y2):
        # calcul distance euclidienne entre les 2 lieux
        dis = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        print(dis)
        return dis




# Cette classe est utilisée pour mémoriser une liste de lieux (variable liste_lieux).
class Graph :
    nb_lieux = 20
    largeur=800
    hauteur=600

    def __init__(self, liste_lieux,largeur=800, hauteur=600):
        self.liste_lieux = liste_lieux 
        self.hauteur = hauteur
        self.largeur = largeur 

    # méthode pour lister les lieux : on ajoute aléatoirement des coordonnées
    def lister_lieu():
        # largeur=800
        # hauteur=600
        # création d'une liste_lieux avec x et y aléatoires
        for lieu in range(Graph.nb_lieux):
            x = randint(0, Graph.largeur)
            y = randint(0, Graph.hauteur)
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
            df = pd.DataFrame(data, columns=['x', 'y'], index=index_lieux)
            # sauvegarde du df
            df.to_csv (r"C:\Users\utilisateur\Documents\microsoft_ia\Cahier d'apprentissage\Projets\projet_isen\script\df.csv", index = False, header=True)
            # chargement du df
            load = pd.read_csv('df.csv')
            print(load)

    # def save_csv(chemin):
    #     df = df.to_csv (chemin, index = False, header=True)

    # def load_csv(nom_fichier):
    #     load = pd.read_csv(nom_fichier)

    def calcul_matrice_cout_od():
        df = pd.read_csv('df.csv')
        n_df=(df.values)

        # array de 0 de dimension 20*20
        matrix=np.zeros(((df.values).shape[0],(df.values).shape[0]))

        # boucles pour calculer la distance entre chaque lieu
        for i in range((df.values).shape[0]):
            for j in range((df.values).shape[0]):
                matrix[i,j]=np.sqrt(np.sum((n_df[i]-n_df[j])**2))
        print(matrix)
        print("------------------")
        print(matrix.shape)
        return matrix 

    
    # def plus_proche_voisin(self,lieu,matrice_od):
    #     self.le_plus_proche_voisin = np.argmin(matrice_od[lieu])
    #     return self.le_plus_proche_voisin
