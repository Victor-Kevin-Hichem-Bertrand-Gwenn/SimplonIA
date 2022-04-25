from tsp_graph_init import Lieu, Graph, Route

lieu = Lieu(50, 100)

lieu2 = Lieu(100, 100)

dist = lieu.distance(lieu2)

graph = Graph([lieu, lieu2])

mat = graph.calcul_matrice_cout_od()

lieu_min = graph.plus_proche_voisin(lieu)

graph.sauvegarder_graph("test.csv")

graph.charger_graph("test.csv")

route = Route()

print("OK")