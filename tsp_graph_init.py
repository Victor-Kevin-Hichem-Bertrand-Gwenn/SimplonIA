import numpy as np
import pandas as pd 
import tkinter as tk
import random
import os

LARGEUR = 800
HAUTEUR = 600
NB_LIEUX = 10

random.seed(1)
np.random.seed(1)

# Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter.
# La classe disposera d'une fonction de calcul de distance euclidienne entre 2 lieux.
class Lieu : 
    ''' Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter.
    '''

    #Definition d'un Lieu aléatoirement ou avec point geometrique (x, y)
    def __init__(self, *args) -> None:
        if args:
            self.x = args[0]
            self.y = args[1]
        else:
            self.x = random.randrange(LARGEUR)
            self.y = random.randrange(HAUTEUR)


    def distance(self, lieu_suivant):
        '''Calcule la distance euclidienne entre un lieu et un autre
        '''
        #Calcule la distance euclidienne entre le lieu(x1, y1) et le lieu suivant(x2, y2)
        dist = np.sqrt((self.x - lieu_suivant.x)**2 + (self.y - lieu_suivant.y)**2)

        return dist


# Cette classe est utilisée pour mémoriser une liste de lieux (variable liste_lieux).
class Graph :

    def __init__(self, LARGEUR, HAUTEUR, NB_LIEUX) :
        self.liste_lieux = [Lieu(random.randint(0, LARGEUR), random.randint(0, HAUTEUR)) for _ in range(NB_LIEUX)]

    # Générer des lieux aléatoirement ou à partir d'une liste de Lieu
    def __init__(self, *args) -> None:
        if args:
            self.liste_lieux = args[0]
        else:
            self.liste_lieux = [Lieu(random.randrange(LARGEUR), random.randrange(HAUTEUR)) for _ in range(NB_LIEUX)]        


    #TODO: Pop lieu1 pour obtenir une matrice triangulaire à laquelle on ajoute une diagonale de 0 et on transpose les valeurs
    def calcul_matrice_cout_od(self) -> np.array:
        # array de 1 de dimension n*n
        lieux = len(self.liste_lieux)
        distance_matrice = np.ones((lieux,lieux))

        # boucles pour calculer la distance entre chaque lieu
        for i,lieu1 in enumerate(self.liste_lieux):
            for j, lieu2 in enumerate(self.liste_lieux):
                distance_matrice[i, j] = lieu1.distance(lieu2)

        self.matrice_cout_od = distance_matrice

        return distance_matrice


    def plus_proche_voisin_iter(self, lieu):
        '''Renvoie le plus proche voisin d'un lieu de manière iterative sur les colonnes.
        '''
        
        # Récupération de l'index du lieu de départ.

        index = self.liste_lieux.index(lieu)

        # Récupération de la liste des distances du lieu de départ aux autres.
        dist_lieux = self.matrice_cout_od[index]

        # Récupération de la valeur minimale en ignorant le 0.
        dist_min = np.sort(dist_lieux)[1]

        # Récupération de l'index de la distance minimale.
        index_dist_min = np.where(dist_lieux == dist_min)[0][0]

        # Récupération du lieu associé à la distance minimale.
        lieu_dist_min = self.liste_lieux[index_dist_min]

        return lieu_dist_min
    
    
    def plus_proche_voisin_argmin(self, lieu):
        '''Renvoie le plus proche voisin d'un lieu
        '''

        # Récupération de l'index du lieu de départ.
        index = self.liste_lieux.index(lieu)

        # Masque des valeurs 0
        masked_array = np.ma.MaskedArray(self.matrice_cout_od[index], self.matrice_cout_od[index]==0)

        # Récupération de l'index de la distance minimale.
        index_dist_min = np.argmin(masked_array)

        # Récupération du lieu associé à la distance minimale.
        lieu_dist_min = self.liste_lieux[index_dist_min]

        return lieu_dist_min

    def charger_graph(self, fname):
        '''Charge une liste de lieux à partir d'un fichier csv des coordonnées
        '''

        # Chargement du fichier csv.
        data_csv = np.loadtxt(
            fname,
            delimiter=',',
            dtype = float)

        # Création de la liste des lieux à partir des coordonnées chargées.
        lieux_charges = [Lieu(data[0], data[1]) for data in data_csv]

        # Affectation de la variable d'instance.
        self.liste_lieux = lieux_charges


    def sauvegarder_graph(self, fname):
        '''Sauvegarde un fichier csv contenant la liste des coordonnées des lieux du graph
        '''

        # Initialisation de la liste des lieux.
        liste_lieux_array = []

        # Parcours des lignes du fichier.
        for lieu in self.liste_lieux:
            liste_lieux_array.append([lieu.x, lieu.y])

        # Enregistrement du fichier csv.
        np.savetxt(
            fname,
            liste_lieux_array,
            delimiter = ',',
            fmt = "%3.2e"
        )
        

    def dataframe():
        # numérotation des lieux 
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


class Route:
    '''Cette classe sert à générer une route traversant tous les lieux d'un graph.
    '''

    def __init__(self, *args) -> None:
        if args:
            self.ordre = args[0]
            print(self.ordre)
            if args[0][0] != 0:
                self.ordre.insert(0, 0)
            if args[0][-1] != 0:
                self.ordre.insert(len(self.ordre), 0)
        else:
            self.ordre = [0]
            liste_index_lieux = [i for i in range(1, NB_LIEUX)]
            random.shuffle(liste_index_lieux)
            self.ordre.extend(liste_index_lieux)
            self.ordre.append(0)
    
    
    def calcul_distance_route(self, graph:Graph):
        '''Calcul la distance totale d'une route
        '''
        
        dist_totale = 0

        # Parcours de l'ensemble des distances dans l'ordre des lieux de la route
        for i, index_lieu in enumerate(self.ordre[:-1]):
            dist_totale += graph.liste_lieux[index_lieu].distance(graph.liste_lieux[self.ordre[i+1]])

        return dist_totale
    

    @classmethod
    def ordre(cls,nb_lieux):
        cls.ordre = [0]
        tmp = list(range(1,nb_lieux))
        random.shuffle(tmp)
        cls.ordre.extend(tmp)
        cls.ordre.append(0)
        return cls.ordre


    @classmethod
    def calcul_distance_route(cls, ordre, matrice_od) :
        cls.distance = 0
        for i in range(len(ordre)-1):
            cls.distance += matrice_od[ordre[i],ordre[i+1]]
        return cls.distance


class Affichage:
    x_cercle = 20
    y_cercle = 20

    def __init__(self, graph:Graph) -> None:
        
        # création d'une fenêtre avec la classe Tk :
        fenetre = tk.Tk()

        # ajout d'un titre à ma fenêtre : 
        fenetre.title("Groupe 4 - Victor-Kevin-Hichem-Bertrand-Gwenn")

        # Insertion surface dessinable (canvas) dans la fenêtre : 
        canvas = tk.Canvas(fenetre, width=LARGEUR, height=HAUTEUR, bg="white")
        canvas.pack()

        # création d'une ligne pointillée
        for lieu in graph.liste_lieux:
            plus_proche_voisin = graph.plus_proche_voisin_argmin(lieu)
            canvas.create_line(
                lieu.x + self.x_cercle/2,
                lieu.y + self.y_cercle/2,
                plus_proche_voisin.x + self.x_cercle/2,
                plus_proche_voisin.y + self.y_cercle/2,
                fill="blue",
                dash=(4, 4)
            )

        # création des cercles pour les villes ou points
        for i, lieu in enumerate(graph.liste_lieux):
            canvas.create_oval(
                lieu.x,
                lieu.y,
                lieu.x + self.x_cercle,
                lieu.y + self.y_cercle,
                fill="silver")

            canvas.create_text(
                lieu.x + self.x_cercle/2,
                lieu.y + self.y_cercle/2,
                text = i
            )


        # création de la légende
        label = tk.Label(fenetre, text="legende : nombre d'itération, meilleure distance, etc...")
        label.pack()

        # appui sur touche pour afficher/fermer la fenêtre : 
        fenetre.bind('<Escape>', lambda x: fenetre.destroy())
        # fenetre.bind("<KeyPress-n>", afficher les N meilleures routes trouvées en gris clair)
        # fenetre.bind("<KeyPress-c>", afficher une matrice de coûts de déplacements entre les Lieux)

        # affichage de la fenetre créée : 
        fenetre.mainloop()
