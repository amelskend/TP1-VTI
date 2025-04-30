import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Chargement et conversion


image_origin = cv2.imread('img.jpg')  
if image_origin is None:
    print("Erreur ")
    exit()

# Convertir l'image en niveaux de gris


image_gris = cv2.cvtColor(image_origin, cv2.COLOR_BGR2GRAY)


# Afficher l'image originale et l'image en niveaux de gris


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Image en Couleur")
plt.imshow(cv2.cvtColor(image_origin, cv2.COLOR_BGR2RGB))  
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Image en Niveaux de Gris")
plt.imshow(image_gris, cmap='gray')
plt.axis('off')

plt.show()

# 2. Analyse initiale
# Afficher l'image en niveaux de gris et son histogramme
plt.figure(figsize=(10, 5))

# Affichage de l'image en niveaux de gris
plt.subplot(1, 2, 1)
plt.title("Image en Niveaux de Gris")
plt.imshow(image_gris, cmap='gray')
plt.axis('off')

# Construction de l'histogramme
plt.subplot(1, 2, 2)
plt.title("Histogramme de l'Image en Niveaux de Gris")
plt.hist(image_gris.ravel(), bins=256, range=[0, 256], color='black')
plt.xlabel("Intensité des pixels")
plt.ylabel("Nombre de pixels")

plt.tight_layout()
plt.show()

# 3. Application des traitements
# Étirement de la dynamique
img_etir = cv2.normalize(image_gris, None, 0, 255, cv2.NORM_MINMAX)

# Normalisation 
borne_min, borne_max = 20, 200
img_norm = cv2.normalize(image_gris, None, borne_min, borne_max, cv2.NORM_MINMAX)

# Égalisation d'histogramme
img_eg = cv2.equalizeHist(image_gris)

# Affichage des résultats des traitements
plt.figure(figsize=(15, 5))

# Étirement de la dynamique
plt.subplot(1, 3, 1)
plt.title("Étirement de la Dynamique")
plt.imshow(img_etir, cmap='gray')
plt.axis('off')

# Normalisation
plt.subplot(1, 3, 2)
plt.title("Normalisation")
plt.imshow(img_norm, cmap='gray')
plt.axis('off')

# Égalisation d'histogramme
plt.subplot(1, 3, 3)
plt.title("Égalisation d'Histogramme")
plt.imshow(img_eg, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

# 4. Affichage comparatif
# Affichage comparatif des images et histogrammes
plt.figure(figsize=(15, 10))

# Image originale
plt.subplot(2, 4, 1)
plt.title("Image Originale")
plt.imshow(image_gris, cmap='gray')
plt.axis('off')

# Étirement de la dynamique
plt.subplot(2, 4, 2)
plt.title("Étirement de la Dynamique")
plt.imshow(img_etir, cmap='gray')
plt.axis('off')

# Normalisation
plt.subplot(2, 4, 3)
plt.title("Normalisation")
plt.imshow(img_norm, cmap='gray')
plt.axis('off')

# Égalisation d'histogramme
plt.subplot(2, 4, 4)
plt.title("Égalisation d'Histogramme")
plt.imshow(img_eg, cmap='gray')
plt.axis('off')

# Histogramme original
plt.subplot(2, 4, 5)
plt.title("Histogramme Original")
plt.hist(image_gris.ravel(), bins=256, range=[0, 256], color='black')
plt.xlabel("Intensité")
plt.ylabel("Pixels")

# Histogramme étirement
plt.subplot(2, 4, 6)
plt.title("Histogramme Étirement")
plt.hist(img_etir.ravel(), bins=256, range=[0, 256], color='black')
plt.xlabel("Intensité")
plt.ylabel("Pixels")

# Histogramme normalisation
plt.subplot(2, 4, 7)
plt.title("Histogramme Normalisation")
plt.hist(img_norm.ravel(), bins=256, range=[0, 256], color='black')
plt.xlabel("Intensité")
plt.ylabel("Pixels")

# Histogramme égalisation
plt.subplot(2, 4, 8)
plt.title("Histogramme Égalisation")
plt.hist(img_eg.ravel(), bins=256, range=[0, 256], color='black')
plt.xlabel("Intensité")
plt.ylabel("Pixels")

plt.tight_layout()
plt.show()
