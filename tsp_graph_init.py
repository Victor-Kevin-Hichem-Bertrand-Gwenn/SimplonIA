import numpy as np
import random

LARGEUR = 800
HAUTEUR = 600
NB_LIEUX = 10

class Lieu:
    ''' Cette classe sert à mémoriser les coordonnées x et y du lieu à visiter.
    '''

    # def __init__(self, x, y) -> None:
    #     self.x = x
    #     self.y = y


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

        dist = np.sqrt(
            (self.x - lieu_suivant.x)**2 + (self.y - lieu_suivant.y)**2
        )

        return dist


class Graph():
    '''Cette classe est utilisée pour mémoriser une liste de lieux (variable liste_lieux).
    '''

    # def __init__(self, liste_lieux) -> None:
    #     self.liste_lieux = liste_lieux

    
    def __init__(self, *args) -> None:
        if args:
            self.liste_lieux = args[0]
        else:
            self.liste_lieux = []

            for i in range(NB_LIEUX):
                x = random.randrange(LARGEUR)
                y = random.randrange(HAUTEUR)
                self.liste_lieux.append(Lieu(x, y))


    #TODO: Pop lieu1 pour obtenir une matrice triangulaire à laquelle on ajoute une diagonale de 0 et on transpose les valeurs
    def calcul_matrice_cout_od(self):
        '''Calcule une matrice de distance entre chaque lieu du graphe
        '''

        # Définition des dimensions de la matrice de distances.
        n_lieux = len(self.liste_lieux)
        matrice_dist = np.ones((n_lieux, n_lieux))

        # Parcours de l'ensemble des lieux de la variable d'instance liste_lieux.
        for i, lieu1 in enumerate(self.liste_lieux):
            for j, lieu2 in enumerate(self.liste_lieux) :
                matrice_dist[i][j] = lieu1.distance(lieu2)

        # Instanciation de la variable d'instance matrice_cout_od.
        self.matrice_cout_od = matrice_dist

        return matrice_dist


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


class Route:
    '''Cette classe sert à générer une route traversant tous les lieux d'un graph.
    '''

    # def __init__(self, liste_index_lieux) -> None:
    #     self.ordre = liste_index_lieux
    #     if liste_index_lieux[0] != 0:
    #         self.ordre.insert(0, 0)
    #     if liste_index_lieux[-1] != 0:
    #         self.ordre.insert(-1, 0)


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