import tkinter as tk
from tkinter import messagebox


def calculer_double():
    try:
        nombre = int(entree.get())
        resultat = 2 * nombre
        messagebox.showinfo("Résultat", f"Le double de {nombre} est {resultat}")

    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un nombre entier valide.")



fenetre = tk.Tk()
fenetre.title("Calculateur de double")
fenetre.geometry("300x150")


cadre = tk.Frame(fenetre, padx=20, pady=20)
cadre.pack(expand=True)

label = tk.Label(cadre, text="Entrez un nombre entier:")
label.pack(pady=(0, 10))

entree = tk.Entry(cadre, width=15)
entree.pack(pady=(0, 10))
entree.focus_set()

entree.bind("<Return>", lambda event: calculer_double())

bouton = tk.Button(cadre, text="Calculer le double", command=calculer_double)
bouton.pack()

# Lancer la boucle principale
fenetre.mainloop()