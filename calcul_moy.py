import tkinter as tk
from tkinter import messagebox


def calculer_produit():
    try:

        nombre1 = float(entree1.get())
        nombre2 = float(entree2.get())


        resultat = nombre1 * nombre2


        if resultat == int(resultat):
            resultat = int(resultat)


        label_resultat.config(text=f"Le produit de {nombre1} et {nombre2} est: {resultat}")

    except ValueError:

        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides.")



fenetre = tk.Tk()
fenetre.title("Calculateur de produit")
fenetre.geometry("400x250")


cadre = tk.Frame(fenetre, padx=20, pady=20)
cadre.pack(expand=True)


label1 = tk.Label(cadre, text="Premier nombre:")
label1.grid(row=0, column=0, sticky="w", pady=(0, 10))

entree1 = tk.Entry(cadre, width=15)
entree1.grid(row=0, column=1, pady=(0, 10), padx=(10, 0))
entree1.focus_set()

# Créer et placer le deuxième label et champ de saisie
label2 = tk.Label(cadre, text="Deuxième nombre:")
label2.grid(row=1, column=0, sticky="w", pady=(0, 10))

entree2 = tk.Entry(cadre, width=15)
entree2.grid(row=1, column=1, pady=(0, 10), padx=(10, 0))

# Créer et placer le bouton de calcul
bouton = tk.Button(cadre, text="Calculer le produit", command=calculer_produit)
bouton.grid(row=2, column=0, columnspan=2, pady=(10, 20))

# Créer et placer le label pour afficher le résultat
label_resultat = tk.Label(cadre, text="", font=("Arial", 10, "bold"))
label_resultat.grid(row=3, column=0, columnspan=2)

# Associer la touche Entrée à la fonction calculer_produit pour les deux champs de saisie
entree1.bind("<Return>", lambda event: entree2.focus_set())
entree2.bind("<Return>", lambda event: calculer_produit())

# Lancer la boucle principale
fenetre.mainloop()