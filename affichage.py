import tkinter as tk

# création d'une fenêtre avec la classe Tk :
fenetre = tk.Tk()

# ajout d'un titre à ma fenêtre : 
fenetre.title("Groupe 4 - Victor-Kevin-Hichem-Bertrand-Gwenn")

# Définir les dimensions par défaut la fenêtre principale :
# fenetre.geometry("800x600")
# finalement c'est le canvas qui défini la taille du graph

# Insertion surface dessinable (canvas) dans la fenêtre : 
canvas = tk.Canvas(fenetre, width=800, height=600, bg="white")
canvas.pack()

# création d'un ligne pointillé
canvas.create_line(0, 100, 200, 0, fill="blue", dash=(4, 4))

# création des cercles pour les villes ou points
canvas.create_oval(10, 20, 20, 10, fill="red")

# création de la légende
label = tk.Label(fenetre, text="legende : nombre d'itération, meilleure distance, etc...")
label.pack()

# appui sur touche pour afficher/fermer la fenêtre : 
fenetre.bind('<Escape>', lambda x: fenetre.destroy())
# fenetre.bind("<KeyPress-n>", afficher les N meilleures routes trouvées en gris clair)
# fenetre.bind("<KeyPress-c>", afficher une matrice de coûts de déplacements entre les Lieux)

# affichage de la fenetre créée : 
fenetre.mainloop()