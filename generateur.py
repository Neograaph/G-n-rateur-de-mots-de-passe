import tkinter as tk
from tkinter import ttk
import random
import string

def generer_mot_de_passe():
    longueur = int(longueur_entry.get())
    caracteres_autorises = string.ascii_letters
    if utiliser_chiffres.get():
        caracteres_autorises += string.digits
    if utiliser_caracteres_speciaux.get():
        caracteres_autorises += string.punctuation
    mot_de_passe = ''.join(random.choice(caracteres_autorises) for _ in range(longueur))
    mot_de_passe_label.config(text="Mot de passe généré : " + mot_de_passe)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Générateur de mots de passe")

# Cadre pour contenir les éléments
cadre = ttk.Frame(fenetre, padding="20")
cadre.grid(row=0, column=0)

# Étiquette et champ de saisie pour la longueur du mot de passe
longueur_label = ttk.Label(cadre, text="Longueur du mot de passe :")
longueur_label.grid(row=0, column=0, padx=5, pady=5)
longueur_entry = ttk.Entry(cadre)
longueur_entry.grid(row=0, column=1, padx=5, pady=5)

# Cases à cocher pour l'inclusion des chiffres et des caractères spéciaux
utiliser_chiffres = tk.IntVar()
utiliser_chiffres_checkbutton = ttk.Checkbutton(cadre, text="Utiliser des chiffres", variable=utiliser_chiffres)
utiliser_chiffres_checkbutton.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

utiliser_caracteres_speciaux = tk.IntVar()
utiliser_caracteres_speciaux_checkbutton = ttk.Checkbutton(cadre, text="Utiliser des caractères spéciaux", variable=utiliser_caracteres_speciaux)
utiliser_caracteres_speciaux_checkbutton.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

# Bouton pour générer le mot de passe
generer_button = ttk.Button(cadre, text="Générer", command=generer_mot_de_passe)
generer_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Étiquette pour afficher le mot de passe généré
mot_de_passe_label = ttk.Label(cadre, text="")
mot_de_passe_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Lancer la boucle principale de la fenêtre
fenetre.mainloop()
