import cv2
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import colorchooser

# 1.1 Charger une image format JPG en utilisant OpenCV
image = cv2.imread("images/image.jpg") # Charger l'image

if image is None:
    print("Erreur : Impossible de charger l'image") # Vérifier si l'image a été chargée correctement
else:
    # 1.2 Afficher l'image originale avec Matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convertir l'image de BGR à RGB
    plt.imshow(image_rgb)
    plt.title("Image Originale")
    plt.axis("off") 
    plt.show()

    # 2.1 Convertir l'image en niveaux de gris
    # a. Avec la moyenne des canaux RGB
    gray_avg = np.mean(image_rgb, axis=2).astype(np.uint8)  # Moyenne des canaux RGB

    # b. Avec la formule pondérée de la CEI
    gray_weighted = (0.299 * image_rgb[:, :, 0] + 
                     0.587 * image_rgb[:, :, 1] + 
                     0.114 * image_rgb[:, :, 2]).astype(np.uint8)

    # 2.2 Comparer les deux résultats
    # Afficher l'image en niveaux de gris moyenne
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(gray_avg, cmap="gray")
    plt.title("Conversion Moyenne RGB")
    plt.axis("off")

    # Afficher l'image en niveaux de gris pondérée
    plt.subplot(1, 2, 2)
    plt.imshow(gray_weighted, cmap="gray")
    plt.title("Conversion Pondérée CEI ")
    plt.axis("off")

    plt.show()

    # 3.1 Inverser les couleurs de l'image (Négatif)
    
    image_inverted = np.zeros_like(image_rgb)  # Initialiser une image vide de la même taille

    # Parcourir chaque pixel de l'image
    for i in range(image_rgb.shape[0]):  # Parcourir les lignes
        for j in range(image_rgb.shape[1]):  # Parcourir les colonnes
            image_inverted[i, j] = 255 - image_rgb[i, j]  # Inverser les couleurs

    # 3.2 Afficher l'image inversée
    plt.imshow(image_inverted)
    plt.title("Image Inversée (Négatif)")
    plt.axis("off")
    plt.show()

    # 4.1 Modifier la luminosité
    # Définir une valeur constante pour ajuster la luminosité
    augmenter = 30  
    deminuer = -30  

    # Augmenter la luminosité
    image_brighter = np.clip(image_rgb + augmenter, 0, 255).astype(np.uint8)

    # Diminuer la luminosité
    image_darker = np.clip(image_rgb.astype(np.int16) + deminuer, 0, 255).astype(np.uint8)

    # 4.2 Afficher les images obtenues
    plt.figure(figsize=(15, 5))

    # Image avec luminosité augmentée
    plt.subplot(1, 2, 1)
    plt.imshow(image_brighter)
    plt.title("Luminosité Augmentée")
    plt.axis("off")

    # Image avec luminosité diminuée
    plt.subplot(1, 2, 2)
    plt.imshow(image_darker)
    plt.title("Luminosité Diminuée")
    plt.axis("off")

    plt.show()

def choisir_couleur(num):
    couleur = colorchooser.askcolor(title="Choisissez une couleur")[1]
    if couleur:
        if num == 1:
            couleur1_entry.delete(0, tk.END)
            couleur1_entry.insert(0, couleur)
            couleur1_affiche.config(bg=couleur)
        elif num == 2:
            couleur2_entry.delete(0, tk.END)
            couleur2_entry.insert(0, couleur)
            couleur2_affiche.config(bg=couleur)

def additionner_couleurs():
    try:
        c1 = root.winfo_rgb(couleur1_entry.get())
        c2 = root.winfo_rgb(couleur2_entry.get())
        couleur_resultat = tuple(min((c1[i] + c2[i]) // 256, 255) for i in range(3))
        hex_resultat = "#{:02x}{:02x}{:02x}".format(*couleur_resultat)
        couleur_resultat_label.config(bg=hex_resultat)
    except:
        couleur_resultat_label.config(text="Erreur", bg="white")

# Interface principale
root = tk.Tk()
root.title("Sélecteur de Couleurs")

# Couleur 1
tk.Label(root, text="Couleur 1 :").grid(row=0, column=0, pady=5, sticky='e')
couleur1_entry = tk.Entry(root, width=10)
couleur1_entry.grid(row=0, column=1)
couleur1_affiche = tk.Label(root, width=5, bg="white", relief="solid")
couleur1_affiche.grid(row=0, column=2, padx=5)
tk.Button(root, text="Choisir", command=lambda: choisir_couleur(1)).grid(row=0, column=3)

# Couleur 2
tk.Label(root, text="Couleur 2 :").grid(row=1, column=0, pady=5, sticky='e')
couleur2_entry = tk.Entry(root, width=10)
couleur2_entry.grid(row=1, column=1)
couleur2_affiche = tk.Label(root, width=5, bg="white", relief="solid")
couleur2_affiche.grid(row=1, column=2, padx=5)
tk.Button(root, text="Choisir", command=lambda: choisir_couleur(2)).grid(row=1, column=3)

# Bouton Additionner
tk.Button(root, text="Additionner", command=additionner_couleurs).grid(row=2, column=1, pady=10)

# Couleur résultante
couleur_resultat_label = tk.Label(root, text="", bg="white", width=20, height=2, relief="ridge")
couleur_resultat_label.grid(row=3, column=0, columnspan=4, pady=10)

root.mainloop()

