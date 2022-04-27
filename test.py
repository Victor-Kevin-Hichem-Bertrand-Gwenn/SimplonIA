from tsp_graph_init import Lieu, Graph, Route, Affichage

lieu1 = Lieu(50, 100)

lieu2 = Lieu(100, 100)

dist1 = lieu1.distance(lieu2)

graph1 = Graph([lieu1, lieu2])
graph2 = Graph()

mat1 = graph1.calcul_matrice_cout_od()
mat2 = graph2.calcul_matrice_cout_od()

lieu_min11 = graph1.plus_proche_voisin_argmin(lieu1)
# lieu_min21 = graph2.plus_proche_voisin(lieu1)

graph1.sauvegarder_graph("test.csv")
graph1.charger_graph("test.csv")

graph2.sauvegarder_graph("test.csv")
graph2.charger_graph("test.csv")

route1 = Route()
route2 = Route()

# Affichage(graph2)

lieu_depart = graph2.liste_lieux[0]
lieux_visites = []
parcours = []

for lieu in graph2.liste_lieux:
    print(lieu)
    lieux_visites.append(lieu)
    if lieux_visites == graph2.liste_lieux:
        continue
    else:
        parcours.append(graph2.plus_proche_voisin_argmin(lieu, lieux_visites))

print("OK")
